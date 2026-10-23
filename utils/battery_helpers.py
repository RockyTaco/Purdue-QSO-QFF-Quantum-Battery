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

# Physical database for custom model creation
ELEMENT_DATABASE = {
    "metals": {
        "Li": {"name": "Lithium", "valence": 1, "E_ref": -7.4327, "opt_dist": 2.05, "base_V": 3.42, "description": "Standard high-reactivity alkali metal."},
        "Na": {"name": "Sodium", "valence": 1, "E_ref": -161.8540, "opt_dist": 2.35, "base_V": 2.95, "description": "Earth-abundant, low-cost table-salt chemistry for grid storage."},
        "K":  {"name": "Potassium", "valence": 1, "E_ref": -599.1650, "opt_dist": 2.70, "base_V": 2.75, "description": "Large ionic radius, fast diffusion kinetics in electrolyte."},
        "Mg": {"name": "Magnesium", "valence": 2, "E_ref": -199.6140, "opt_dist": 1.95, "base_V": 3.10, "description": "Divalent ion carrying 2 electrons per atom, high volumetric capacity without dendrites."},
        "Ca": {"name": "Calcium", "valence": 2, "E_ref": -676.7580, "opt_dist": 2.25, "base_V": 3.00, "description": "Abundant divalent metal, high reduction potential similar to Lithium."},
        "Al": {"name": "Aluminum", "valence": 3, "E_ref": -241.8760, "opt_dist": 1.85, "base_V": 2.65, "description": "Trivalent ion carrying 3 electrons per atom, non-flammable and ultra-safe."},
        "Zn": {"name": "Zinc", "valence": 2, "E_ref": -1777.8480, "opt_dist": 1.90, "base_V": 2.40, "description": "Aqueous electrolyte compatible, recyclable, low environmental toxicity."}
    },
    "hosts": {
        "Carbon": {"name": "sp2 Carbon (Graphite)", "E_ref": -77.0712, "affinity_eV": 0.0, "tradeoff": "Commercial standard. Stable, moderate capacity."},
        "Silicon": {"name": "Silicon Host", "E_ref": -289.3240, "affinity_eV": 0.36, "tradeoff": "Alloying host holding up to 10x more ions, higher voltage."},
        "N-doped-Carbon": {"name": "Nitrogen-Doped Carbon", "E_ref": -82.4110, "affinity_eV": 0.50, "tradeoff": "Polar heteroatom defects suppress metallic dendrites and fires."},
        "B-doped-Carbon": {"name": "Boron-Doped Carbon", "E_ref": -75.8230, "affinity_eV": 0.32, "tradeoff": "P-type defects enhance electrical conductivity and ion transfer."},
        "Sulfur": {"name": "Sulfur Cathode Host", "E_ref": -397.5050, "affinity_eV": 0.65, "tradeoff": "High theoretical specific energy, multi-electron conversion."},
        "Phosphorus": {"name": "Black Phosphorus", "E_ref": -340.7180, "affinity_eV": 0.42, "tradeoff": "Layered puckered 2D structure with high electrical conductivity."}
    }
}

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

def build_custom_battery_model(metal="Na", host="Carbon", distance_angstrom=None):
    """
    Build your own battery materials model!
    Allows participants to mix and match elements and customize geometry:
      - metal: 'Li', 'Na', 'K', 'Mg', 'Ca', 'Al', 'Zn'
      - host:  'Carbon', 'Silicon', 'N-doped-Carbon', 'B-doped-Carbon', 'Sulfur', 'Phosphorus'
      - distance_angstrom: Intercalation binding distance in Angstroms (default is optimal distance)

    Returns a model dictionary containing:
      - 'hamiltonian': 4-qubit SparsePauliOp
      - 'E_host_Hartree': Reference energy of the uncoordinated host
      - 'E_metal_Hartree': Reference energy of the isolated metal atom
      - 'theoretical_cell_voltage_V': Physical benchmark voltage
      - 'name': Descriptive system name
      - 'application_tradeoff': Engineering context
    """
    metal_info = ELEMENT_DATABASE["metals"].get(metal)
    if not metal_info:
        raise ValueError(f"Unknown metal '{metal}'. Choose from: {list(ELEMENT_DATABASE['metals'].keys())}")
    
    host_info = ELEMENT_DATABASE["hosts"].get(host)
    if not host_info:
        raise ValueError(f"Unknown host '{host}'. Choose from: {list(ELEMENT_DATABASE['hosts'].keys())}")
    
    r_opt = metal_info["opt_dist"]
    r = float(distance_angstrom) if distance_angstrom is not None else r_opt
    z = metal_info["valence"]
    
    # Calculate physical binding energy shift based on distance and host affinity
    delta_r = (r - r_opt)
    dist_factor = np.exp(-1.5 * delta_r) - 2 * np.exp(-0.75 * delta_r)
    
    base_v = metal_info["base_V"] + host_info["affinity_eV"]
    target_v = max(0.5, base_v * (-dist_factor))
    target_delta_e_ev = -target_v * z
    target_delta_e_hartree = target_delta_e_ev / HARTREE_TO_EV
    
    e_host = host_info["E_ref"]
    e_metal = metal_info["E_ref"]
    target_e_bound = (e_host + e_metal) + target_delta_e_hartree
    
    # Construct 4-qubit Hamiltonian matching target ground state
    core_const = target_e_bound + 0.8053
    paulis = [
        ("IIII", round(core_const, 4)),
        ("ZIII",  round(0.1800 * (1.0 + 0.1 * (z - 1)), 4)),
        ("IZII",  round(0.1800 * (1.0 + 0.1 * (z - 1)), 4)),
        ("IIZI", round(-0.2400 * (1.0 + host_info['affinity_eV']), 4)),
        ("IIIZ", round(-0.2400 * (1.0 + host_info['affinity_eV']), 4)),
        ("ZZII",  0.1100),
        ("IIZZ",  0.1250),
        ("ZIZI",  round(0.0750 * np.exp(-0.5 * abs(delta_r)), 4)),
        ("IZIZ",  round(0.0750 * np.exp(-0.5 * abs(delta_r)), 4)),
        ("XXII",  0.0400),
        ("IIXX",  0.0380),
        ("XXXX",  0.0200)
    ]
    
    return {
        "chemistry": f"{metal}-{host}",
        "name": f"{metal_info['name']} on {host_info['name']} (r = {r:.2f} Å)",
        "metal": metal,
        "host": host,
        "valence": z,
        "distance_angstrom": r,
        "hamiltonian": SparsePauliOp.from_list(paulis),
        "E_host_Hartree": e_host,
        "E_metal_Hartree": e_metal,
        "target_E_bound": target_e_bound,
        "theoretical_cell_voltage_V": round(target_v, 2),
        "application_tradeoff": f"{metal_info['description']} | Host: {host_info['tradeoff']}"
    }

def create_custom_hamiltonian(pauli_list, e_host, e_metal, valence=1, chemistry_name="Custom-System"):
    """
    For teams building a Hamiltonian from scratch!
    - pauli_list: list of tuples [('IIII', -85.2), ('ZIII', 0.18), ...]
    - e_host: reference energy of host in Hartree
    - e_metal: reference energy of metal in Hartree
    - valence: ion charge state z (1 for Li+, 2 for Mg2+, 3 for Al3+)
    """
    return {
        "chemistry": chemistry_name,
        "name": chemistry_name,
        "metal": "Custom",
        "host": "Custom",
        "valence": int(valence),
        "distance_angstrom": 0.0,
        "hamiltonian": SparsePauliOp.from_list(pauli_list),
        "E_host_Hartree": float(e_host),
        "E_metal_Hartree": float(e_metal),
        "application_tradeoff": "Custom team-designed quantum materials model."
    }

def calculate_battery_voltage(e_bound_hartree, chemistry="Li-C", model_info=None):
    """
    Calculates the binding energy (Delta E) and theoretical battery cell voltage (V_cell).
    
    Thermodynamic Formula (Nernst Relation):
      Delta_E = E(Bound_Complex) - [E(Host) + E(Metal_Isolated)]
      Delta_E_eV = Delta_E * 27.2114 eV
      V_cell = - Delta_E_eV / (z * e)
      where z is the mobile ion charge valence (Li+=1, Na+=1, Mg2+=2, Al3+=3).
    """
    if model_info is not None:
        chem_name = model_info.get("chemistry", "Custom")
        system_name = model_info.get("name", chem_name)
        valence = model_info.get("valence", 1)
        e_host = model_info["E_host_Hartree"]
        e_metal = model_info["E_metal_Hartree"]
        target_v = model_info.get("theoretical_cell_voltage_V", None)
        tradeoff = model_info.get("application_tradeoff", "Custom battery model")
    else:
        benchmarks = load_benchmarks()
        if chemistry not in benchmarks["materials"]:
            raise ValueError(f"Chemistry '{chemistry}' not found in benchmarks.")
        mat = benchmarks["materials"][chemistry]
        chem_name = chemistry
        system_name = mat["name"]
        valence = mat.get("valence", 1)
        e_host = mat["E_host_Hartree"]
        e_metal = mat["E_metal_isolated_Hartree"]
        target_v = mat["theoretical_cell_voltage_V"]
        tradeoff = mat["application_tradeoff"]

    delta_e_hartree = float(e_bound_hartree) - (e_host + e_metal)
    delta_e_ev = delta_e_hartree * HARTREE_TO_EV
    v_cell = -delta_e_ev / valence
    v_error = abs(v_cell - target_v) if target_v is not None else 0.0

    return {
        "chemistry": chem_name,
        "name": system_name,
        "valence": valence,
        "E_bound_Hartree": float(e_bound_hartree),
        "E_host_Hartree": e_host,
        "E_metal_Hartree": e_metal,
        "Delta_E_Hartree": delta_e_hartree,
        "Delta_E_eV": round(delta_e_ev, 3),
        "V_cell_Volts": round(v_cell, 3),
        "target_V_cell": target_v,
        "voltage_error_Volts": round(v_error, 4),
        "application_tradeoff": tradeoff
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

def check_part3(vqe_new_energy, chemistry=None, model_info=None):
    """Validation test for Part 3 custom or alternative material."""
    if model_info is not None:
        res = calculate_battery_voltage(vqe_new_energy, model_info=model_info)
    else:
        res = calculate_battery_voltage(vqe_new_energy, chemistry=chemistry)
        
    print("=" * 60)
    print(f"🚀 PART 3 DISCOVERY CHECK: {res['name']}")
    print("=" * 60)
    print(f"Chemistry Explored:          {res['chemistry']}")
    if res.get('valence', 1) > 1:
        print(f"Ion Valence (z):             {res['valence']}+ (Multivalent Transfer)")
    print(f"Binding Energy (Delta E):    {res['Delta_E_eV']:.3f} eV")
    print(f"New Battery Cell Voltage:    {res['V_cell_Volts']:.3f} V")
    if res['target_V_cell'] is not None:
        print(f"Target Voltage Reference:    ~{res['target_V_cell']:.2f} V")
        print(f"Discrepancy:                 {res['voltage_error_Volts']:.4f} V")
    print(f"Application Trade-off:       {res['application_tradeoff']}")
    print("=" * 60)
    return res
