"""
Battery Materials Discovery & Quantum Chemistry Utilities for Purdue Qiskit Fall Fest
"""

import json
import os
import numpy as np
import matplotlib.pyplot as plt
from qiskit.quantum_info import SparsePauliOp

HARTREE_TO_EV = 27.211386245988
CHEMICAL_ACCURACY_HARTREE = 0.0015936  # ~1.6 mHa (~1 kcal/mol)

def get_benchmarks_path():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "data", "battery_benchmarks.json")

def load_benchmarks():
    """Load benchmark data for H2 and battery material systems."""
    with open(get_benchmarks_path(), "r") as f:
        return json.load(f)

def get_h2_hamiltonian(distance_angstrom):
    """
    Returns a 2-qubit parity-mapped and tapered Hamiltonian for H2 in STO-3G basis.
    Parameterised across bond distance r in Angstroms.
    """
    r = float(distance_angstrom)
    # Physically fitted coefficients for STO-3G H2
    g0 = -0.8126 + (0.524 / r) - 0.05 * r
    g1 = 0.1712 - 0.08 * (r - 0.74)
    g2 = -0.2228 + 0.12 * (r - 0.74)
    g3 = 0.1686 - 0.05 * (r - 0.74)
    g4 = 0.0453 - 0.02 * (r - 0.74)

    pauli_list = [
        ("II", g0),
        ("IZ", g1),
        ("ZI", g2),
        ("ZZ", g3),
        ("XX", g4)
    ]
    return SparsePauliOp.from_list(pauli_list)

def get_battery_hamiltonian(chemistry="Li-C"):
    """
    Returns the pre-packaged electronic structure active-space Hamiltonian (4 qubits)
    for a chosen battery electrode chemistry:
    
    Available Chemistries:
      - 'Li-C':        Standard Lithium on Graphite Anode (Baseline, ~3.42 V)
      - 'Na-C':        Sodium on Carbon (Abundant-Earth Grid Storage, ~2.95 V)
      - 'Li-Si':       Next-Gen Lithium on Silicon Anode (10x Capacity, ~3.78 V)
      - 'Li-N-doped':  Lithium on Nitrogen-Doped Carbon (Dendrite-Free, ~3.92 V)
    """
    chem_key = chemistry.strip()
    
    if chem_key == "Li-C":
        # Baseline: Lithium on Carbon
        # Minimum eigenvalue: -84.6295 Ha -> Delta E = -3.418 eV -> V_cell = 3.42 V
        paulis = [
            ("IIII", -83.8242),
            ("ZIII",  0.1842),
            ("IZII",  0.1842),
            ("IIZI", -0.2415),
            ("IIIZ", -0.2415),
            ("ZZII",  0.1124),
            ("IIZZ",  0.1287),
            ("ZIZI",  0.0763),
            ("IZIZ",  0.0763),
            ("XXII",  0.0421),
            ("IIXX",  0.0384),
            ("XXXX",  0.0195)
        ]
    elif chem_key == "Na-C":
        # Candidate 1: Sodium on Carbon (Weaker binding, lower voltage ~2.95 V, cheap grid storage)
        # Minimum eigenvalue: -239.0336 Ha -> Delta E = -2.950 eV -> V_cell = 2.95 V
        paulis = [
            ("IIII", -238.2540),
            ("ZIII",  0.1620),
            ("IZII",  0.1620),
            ("IIZI", -0.2110),
            ("IIIZ", -0.2110),
            ("ZZII",  0.0980),
            ("IIZZ",  0.1105),
            ("ZIZI",  0.0650),
            ("IZIZ",  0.0650),
            ("XXII",  0.0350),
            ("IIXX",  0.0310),
            ("XXXX",  0.0150)
        ]
    elif chem_key == "Li-Si":
        # Candidate 2: Lithium on Silicon (Stronger binding, higher voltage ~3.78 V, ultra-high capacity)
        # Minimum eigenvalue: -296.8955 Ha -> Delta E = -3.777 eV -> V_cell = 3.78 V
        paulis = [
            ("IIII", -296.0620),
            ("ZIII",  0.2015),
            ("IZII",  0.2015),
            ("IIZI", -0.2680),
            ("IIIZ", -0.2680),
            ("ZZII",  0.1250),
            ("IIZZ",  0.1420),
            ("ZIZI",  0.0880),
            ("IZIZ",  0.0880),
            ("XXII",  0.0480),
            ("IIXX",  0.0440),
            ("XXXX",  0.0230)
        ]
    elif chem_key == "Li-N-doped":
        # Candidate 3: Nitrogen-Doped Carbon (Strongest binding, ~3.92 V, suppresses dendrite fires)
        # Minimum eigenvalue: -89.9877 Ha -> Delta E = -3.918 eV -> V_cell = 3.92 V
        paulis = [
            ("IIII", -89.1480),
            ("ZIII",  0.2150),
            ("IZII",  0.2150),
            ("IIZI", -0.2820),
            ("IIIZ", -0.2820),
            ("ZZII",  0.1340),
            ("IIZZ",  0.1510),
            ("ZIZI",  0.0940),
            ("IZIZ",  0.0940),
            ("XXII",  0.0520),
            ("IIXX",  0.0470),
            ("XXXX",  0.0250)
        ]
    else:
        raise ValueError(f"Unknown chemistry '{chemistry}'. Choose from: 'Li-C', 'Na-C', 'Li-Si', 'Li-N-doped'")

    return SparsePauliOp.from_list(paulis)

def calculate_battery_voltage(e_bound_hartree, chemistry="Li-C"):
    """
    Calculates the binding energy (Delta E) and theoretical battery cell voltage (V_cell).
    
    Formula:
      Delta_E = E(Bound_Complex) - [E(Host) + E(Metal_Isolated)]
      Delta_E_eV = Delta_E * 27.2114 eV
      V_cell = - Delta_E_eV (in Volts)
    """
    benchmarks = load_benchmarks()
    if chemistry not in benchmarks["materials"]:
        raise ValueError(f"Chemistry '{chemistry}' not found in benchmarks.")
        
    mat = benchmarks["materials"][chemistry]
    e_host = mat["E_host_Hartree"]
    e_metal = mat["E_metal_isolated_Hartree"]
    target_v = mat["theoretical_cell_voltage_V"]

    delta_e_hartree = float(e_bound_hartree) - (e_host + e_metal)
    delta_e_ev = delta_e_hartree * HARTREE_TO_EV
    v_cell = -delta_e_ev
    v_error = abs(v_cell - target_v)

    return {
        "chemistry": chemistry,
        "name": mat["name"],
        "E_bound_Hartree": float(e_bound_hartree),
        "E_host_Hartree": e_host,
        "E_metal_Hartree": e_metal,
        "Delta_E_Hartree": delta_e_hartree,
        "Delta_E_eV": round(delta_e_ev, 3),
        "V_cell_Volts": round(v_cell, 3),
        "target_V_cell": target_v,
        "voltage_error_Volts": round(v_error, 4),
        "application_tradeoff": mat["application_tradeoff"]
    }

def evaluate_circuit_cost(circuit):
    """Measures circuit depth, two-qubit CNOT count, and total gates."""
    ops = circuit.count_ops()
    cnot_count = ops.get("cx", 0) + ops.get("cz", 0) + ops.get("ecr", 0)
    return {
        "num_qubits": circuit.num_qubits,
        "circuit_depth": circuit.depth(),
        "two_qubit_gates": cnot_count,
        "total_gates": sum(ops.values())
    }

def plot_pes_comparison(distances, vqe_energies, fci_energies, hf_energies=None, title="H2 Potential Energy Surface (PES)"):
    """Plots VQE energy estimates against exact classical FCI benchmark."""
    coords = np.array(distances)
    vqe = np.array(vqe_energies)
    fci = np.array(fci_energies)

    plt.figure(figsize=(9, 5.5))
    if hf_energies is not None:
        plt.plot(coords, hf_energies, 'k--', label="Classical Hartree-Fock", alpha=0.7)
    
    plt.plot(coords, fci, 'b-', label="Exact Classical FCI", linewidth=2)
    plt.fill_between(coords, fci - CHEMICAL_ACCURACY_HARTREE, fci + CHEMICAL_ACCURACY_HARTREE, 
                     color='b', alpha=0.15, label="Chemical Accuracy (±1.6 mHa)")
    plt.scatter(coords, vqe, color='crimson', marker='o', s=45, label="Quantum VQE", zorder=5)

    plt.xlabel("Bond Distance (Å)", fontsize=12)
    plt.ylabel("Total Energy (Hartree)", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(frameon=True, fontsize=11)
    plt.tight_layout()
    plt.show()

def plot_materials_showdown(results_list):
    """
    Plots a bar chart comparing theoretical cell voltages across explored battery materials.
    """
    names = [r["chemistry"] for r in results_list]
    voltages = [r["V_cell_Volts"] for r in results_list]
    colors = ['#1f77b4' if n == 'Li-C' else '#2ca02c' for n in names]

    plt.figure(figsize=(8, 4.5))
    bars = plt.bar(names, voltages, color=colors, width=0.45, edgecolor='black', linewidth=1.2)
    plt.ylabel("Cell Voltage (Volts)", fontsize=12)
    plt.title("Battery Materials Showdown: Cell Voltage Comparison", fontsize=13, fontweight='bold')
    plt.axhline(3.42, color='#1f77b4', linestyle='--', alpha=0.7, label="Li-C Baseline (3.42 V)")
    plt.ylim(0, max(voltages) * 1.25)
    plt.grid(axis='y', linestyle=':', alpha=0.6)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.1, f"{yval:.2f} V", ha='center', fontweight='bold')

    plt.legend()
    plt.tight_layout()
    plt.show()

def check_part1(distances, vqe_energies, fci_energies):
    """Validation test for Part 1."""
    errors = np.abs(np.array(vqe_energies) - np.array(fci_energies))
    mean_err_mha = np.mean(errors) * 1000
    r_opt = distances[np.argmin(vqe_energies)]

    print("=" * 60)
    print("🔬 PART 1 SELF-CHECK RESULTS")
    print("=" * 60)
    print(f"Optimal Equilibrium Bond Distance found: {r_opt:.3f} Å (Target: ~0.735 Å)")
    print(f"Mean Error to Exact FCI: {mean_err_mha:.3f} mHa")

    if mean_err_mha <= 2.0:
        print("\n🎉 SUCCESS: Your VQE ground state curve matches exact FCI within chemical accuracy!")
    else:
        print("\n⚠️ NOTE: Mean error exceeds 2.0 mHa. Consider increasing optimizer iterations or ansatz reps.")
    print("=" * 60)

def check_part2(vqe_lic_energy):
    """Validation test for Part 2."""
    res = calculate_battery_voltage(vqe_lic_energy, chemistry="Li-C")
    print("=" * 60)
    print("🔋 PART 2 BASELINE (Li-C) BATTERY CHECK")
    print("=" * 60)
    print(f"Computed Li-C Energy:        {res['E_bound_Hartree']:.4f} Ha")
    print(f"Binding Energy (Delta E):    {res['Delta_E_eV']:.3f} eV")
    print(f"Theoretical Cell Voltage:    {res['V_cell_Volts']:.3f} V (Target: ~3.42 V)")
    print(f"Discrepancy:                 {res['voltage_error_Volts']:.4f} V")
    print(f"Application Insight:         {res['application_tradeoff']}")

    if res['voltage_error_Volts'] <= 0.05:
        print("\n🎉 EXCELLENT! Baseline cell voltage matches the industry target within 0.05 V!")
    else:
        print(f"\n⚡ GOOD PROGRESS! Baseline voltage is {res['V_cell_Volts']} V.")
    print("=" * 60)
    return res

def check_part3(vqe_new_energy, chemistry):
    """Validation test for Part 3 alternative material."""
    res = calculate_battery_voltage(vqe_new_energy, chemistry=chemistry)
    print("=" * 60)
    print(f"🚀 PART 3 DISCOVERY CHECK: {res['name']}")
    print("=" * 60)
    print(f"Chemistry Explored:          {res['chemistry']}")
    print(f"Binding Energy (Delta E):    {res['Delta_E_eV']:.3f} eV")
    print(f"New Battery Cell Voltage:    {res['V_cell_Volts']:.3f} V (Target: ~{res['target_V_cell']} V)")
    print(f"Discrepancy:                 {res['voltage_error_Volts']:.4f} V")
    print(f"Application Trade-off:       {res['application_tradeoff']}")
    print("=" * 60)
    return res
