# 🔋 The Next-Gen Battery Race: Materials Discovery with Qiskit
### *Purdue Qiskit Fall Fest Hackathon Challenge*

[![Qiskit Version](https://img.shields.io/badge/Qiskit-1.2+-6929C4.svg?style=flat-square&logo=qiskit&logoColor=white)](https://qiskit.org/)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%20%7C%203.11%20%7C%203.12-3776AB.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Purdue University](https://img.shields.io/badge/Purdue-Qiskit%20Fall%20Fest-CEB888.svg?style=flat-square&logoColor=black)](https://www.purdue.edu/)
[![Open In Colab](https://img.shields.io/badge/Colab-Tutorial-F9AB00.svg?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/RockyTaco/Purdue-QSO-QFF-Quantum-Battery/blob/main/notebooks/01_tutorial_hydrogen_vqe.ipynb)
[![Open In Colab](https://img.shields.io/badge/Colab-Submission_Notebook-F9AB00.svg?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/github/RockyTaco/Purdue-QSO-QFF-Quantum-Battery/blob/main/notebooks/02_challenge_submission.ipynb)

Welcome to the **Battery Materials Discovery Challenge**! In this challenge, your team will use quantum simulation to design and evaluate the atomic interfaces powering the clean energy revolution—from green hydrogen fuel cells to next-generation electric vehicle (EV) and grid batteries.

---

## ⚡ The Application: Why Materials Matter

Today's commercial EV batteries rely on **Lithium intercalated into Graphite (Li–C)**, delivering roughly 3.4 to 3.7 Volts. While reliable, this chemistry is hitting fundamental walls:

1. **Scarcity & Cost:** Lithium extraction is geographically concentrated and environmentally destructive.
2. **Capacity Limits:** Graphite can only hold one lithium atom for every six carbon atoms (LiC₆).
3. **Safety & Degradation:** Fast charging causes metallic lithium needles ("dendrites") to grow, shorting the battery and causing fires.

To build the next generation of energy storage, scientists are racing to find **alternative elements and electrode materials**:
* Can cheap, table-salt-derived **Sodium (Na)** replace lithium for large-scale grid storage?
* Can a **Silicon (Si)** anode store 10× more energy for 1,000-mile EV range?
* Can **heteroatom-doped carbon (N-doped)** trap ions more securely to prevent battery fires?

> [!NOTE]
> Because electron correlation at molecular interfaces is fundamentally quantum mechanical, classical supercomputers struggle to calculate binding energies accurately. You will use **Qiskit** and the **Variational Quantum Eigensolver (VQE)** to simulate these atomic bonds and discover what makes a superior battery!

---

## 🗺️ Challenge Roadmap

```
┌───────────────────────────────────────────────────────────────────┐
│                THE NEXT-GEN BATTERY DISCOVERY RACE                │
└─────────────────────────────────┬─────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────┐
│ PART 1: THE TRAINING GROUND (10 pts)                              │
│ Molecular Hydrogen (H2) PES Sweep                                 │
├───────────────────────────────────────────────────────────────────┤
│ • Learn how molecular systems map to quantum circuits             │
│ • Run VQE with Qiskit StatevectorEstimator                        │
│ • Reconstruct potential energy curve and find Re (~0.735 Å)       │
│ • Achieve chemical accuracy (<= 1.6 mHa) against exact FCI        │
└─────────────────────────────────┬─────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────┐
│ PART 2: THE INDUSTRY BENCHMARK (20 pts)                           │
│ Lithium-Graphite (Li-C) Commercial Anode                          │
├───────────────────────────────────────────────────────────────────┤
│ • Simulate today's standard EV battery anode                      │
│ • Calculate quantum binding energy: Delta_E_bind                  │
│ • Derive open-circuit cell voltage: V_cell = -Delta_E / (z*e)     │
│ • Establish industry baseline benchmark: ~3.42 Volts              │
└─────────────────────────────────┬─────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────┐
│ PART 3: NOVEL MATERIALS DISCOVERY (45 pts)                        │
│ "Can You Find a Better Chemistry? Can You Prove It?"              │
├───────────────────────────────────────────────────────────────────┤
│ Move beyond standard graphite! Test alternative chemistries:      │
│                                                                   │
│ • Sodium-Ion (Na-C): Abundant, low-cost grid storage              │
│ • Silicon Anode (Li-Si): 10x capacity for extended EV range       │
│ • N-Doped Carbon (Li-C_N): Polar heteroatoms for fire safety      │
│ • Custom Candidate: Explore metals (Mg, Ca, Al, Zn) & hosts       │
│                                                                   │
│ Deliverable: Run VQE on your candidate, compute the new cell      │
│ voltage, build a Showdown Comparison, and defend your design!     │
└─────────────────────────────────┬─────────────────────────────────┘
                                  │
                                  ▼
┌───────────────────────────────────────────────────────────────────┐
│ PART 4: PRESENTATION & SCIENTIFIC DEFENSE (25 pts)                │
│ Pitch and defend your discovered material to the judges           │
└───────────────────────────────────────────────────────────────────┘
```

---

## 💡 What Does "Better" Mean in Battery Engineering?

In real-world battery development, no single material is "best" at everything. **"Better" depends on your design objective:**

| Engineering Dimension | Candidate Chemistry | How It Improves on the Baseline (Li–C) |
| :--- | :---: | :--- |
| **1. Maximum Cell Voltage (V_cell)** | **Silicon Anode (`'Li-Si'`)** | Delivers higher voltage (~3.78 V) and holds up to 10× more lithium atoms per gram, unlocking longer electric vehicle range. |
| **2. Cost & Raw Material Abundance** | **Sodium-Ion (`'Na-C'`)** | Replaces expensive, scarce Lithium with cheap, abundant Sodium. Drops voltage to ~2.95 V, but reduces raw cell material costs by >80% for stationary solar/wind grid storage. |
| **3. Safety & Fire Prevention** | **Nitrogen-Doped (`'Li-N-doped'`)** | Nitrogen atoms create polar trapping sites that bind lithium tightly (~3.92 V), preventing metallic lithium dendrites from piercing the separator. |

> [!IMPORTANT]
> **Your Part 3 Mission:** Choose an engineering objective (Voltage Maximization, Grid-Scale Cost Optimization, or Fast-Charging Safety), simulate your chosen material with VQE, and quantitatively prove why it outperforms the baseline along that dimension!

---

## 🚀 Getting Started

No quantum chemistry drivers (like PySCF) or compilers are required! All molecular Hamiltonians, classical benchmark references, and visualizers are pre-packaged in `utils/` and `data/`.

### Option A: Local Setup (Recommended)
```bash
# 1. Clone your private team repository
git clone <your-private-repo-url>
cd fallfest-ev-battery

# 2. Set up virtual environment
python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

# 3. Install Qiskit dependencies
pip install -r requirements.txt
```

### Option B: Google Colab
You can run this challenge directly in your browser:
* 📓 **[Launch Tutorial Notebook on Colab](https://colab.research.google.com/github/RockyTaco/Purdue-QSO-QFF-Quantum-Battery/blob/main/notebooks/01_tutorial_hydrogen_vqe.ipynb)**
* 🚀 **[Launch Official Submission Notebook on Colab](https://colab.research.google.com/github/RockyTaco/Purdue-QSO-QFF-Quantum-Battery/blob/main/notebooks/02_challenge_submission.ipynb)**

Inside Colab, simply run:
```python
!pip install qiskit>=1.2.0 qiskit-aer>=0.14.0 matplotlib numpy scipy
```

---

## 🎯 The Four Challenge Stages

### Part 1: The Training Ground — Molecular Hydrogen (H₂) `[10 Points]`
* **Goal:** Understand how quantum circuits find lowest-energy states (ground states).
* **Step-by-Step Instructions:**
  1. Load the pre-packaged H₂ Hamiltonian across bond distances R ∈ [0.4, 2.5] Å using `get_h2_hamiltonian(r)`.
  2. Build a parameterized ansatz (`EfficientSU2`) with 2 qubits and linear entanglement.
  3. Run VQE using Qiskit's `StatevectorEstimator` with SciPy's `SLSQP` or `COBYLA` optimizer.
  4. Plot the potential energy curve, find the equilibrium bond distance R_e ≈ 0.735 Å, and verify chemical accuracy (≤ 1.6 mHa) using `check_part1()`.

### Part 2: The Industry Benchmark — Lithium on Carbon (Li–C) `[20 Points]`
* **Goal:** Simulate the commercial standard EV battery anode.
* **The Physics:**
  When lithium intercalates into the electrode host material, binding energy is released:

```math
\Delta E_{\text{bind}} = E(\text{Bound Complex}) - \left[ E(\text{Host}) + E(\text{Metal}) \right]
```

  From the thermodynamic Nernst relation ($\Delta G = -z F E_{\text{cell}}$), this binding energy directly dictates the **theoretical battery cell voltage**:

```math
V_{\text{cell}} = -\frac{\Delta E_{\text{bind}}}{z \cdot e} \quad (\text{Industry Target for Li–C: } \approx 3.42\text{ V})
```

  where $z$ is the ion charge valence ($z = 1$ for Li⁺, Na⁺, K⁺; $z = 2$ for Mg²⁺, Ca²⁺, Zn²⁺; $z = 3$ for Al³⁺).
* **Step-by-Step Instructions:**
  1. Load the pre-packaged 4-qubit Li–C Hamiltonian using `get_battery_hamiltonian('Li-C')`.
  2. Optimize your VQE circuit to find the ground state energy E(Li–C).
  3. Compute ΔE_bind and V_cell using `calculate_battery_voltage()`.
  4. Verify your baseline voltage using `check_part2()`.

### Part 3: Novel Materials Discovery & Custom Model Design `[45 Points]`
* **Goal:** Design and evaluate your own alternative battery chemistry to solve a real-world energy storage problem.
* **The Materials Discovery Pipeline (What, How, and Why):**
  * **What to find:** The ground state energy E_bound of your intercalated metal-electrode system. From this, compute the binding energy ΔE_bind and open-circuit cell voltage:
    `V_cell = -ΔE_bind / (z · e)`
  * **How to build your model:** Use the custom builder `build_custom_battery_model(metal=..., host=..., distance_angstrom=...)` or construct your own Hamiltonian with `create_custom_hamiltonian()`:
    * **Metals:** Lithium (`'Li'`), Sodium (`'Na'`), Potassium (`'K'`), Magnesium (`'Mg'`), Calcium (`'Ca'`), Aluminum (`'Al'`), or Zinc (`'Zn'`).
    * **Hosts:** Graphite (`'Carbon'`), Silicon (`'Silicon'`), Nitrogen-Doped Carbon (`'N-doped-Carbon'`), Boron-Doped Carbon (`'B-doped-Carbon'`), or Sulfur (`'Sulfur'`).
    * **Geometry:** Tune the interatomic binding distance in Angstroms ($r$) to observe how physical lattice expansion affects battery voltage!
  * **Why it matters:** The strength and stability of this bond dictates energy density, safety against fires, and cost.
* **Scoring Breakdown for Part 3 (45 pts total):**
  * 🔹 **VQE Implementation & Convergence (15 pts):** Clean ansatz configuration, optimizer convergence curve, and variational ground-state energy computation.
  * 🔹 **Materials Discovery & Distance Sweep (15 pts):** Thoughtful selection of element/host pairs, exploring how lattice spacing ($r$) changes binding energy, and identifying physical trends.
  * 🔹 **Quantitative Verification & Showdown (15 pts):** Accurate electrochemical cell voltage calculation via `check_part3()`, comparison against the Li–C baseline, and generated showdown chart (`plot_materials_showdown()`).
* **Step-by-Step Instructions:**
  1. Build your custom material model using `build_custom_battery_model()`.
  2. Run VQE to find its ground state energy and calculate its new cell voltage using `check_part3()`.
  3. Generate the side-by-side **Materials Showdown Comparison** bar chart with `plot_materials_showdown()`.
  4. Fill in the Part 4 Scientific Defense table comparing your custom candidate against the baseline.

### Part 4: Presentation & Scientific Defense `[25 Points]`
* **Goal:** Defend your discovered battery chemistry to the judges. With AI tools widely available, the presentation and oral defense is the ultimate test of whether your team truly understands the physics, simulation results, and practical trade-offs.
* **What to prepare (Slide Deck / Oral Pitch):**
  1. Which engineering dimension did you prioritize (voltage, cost, safety), and why?
  2. How do your quantum simulation numbers verify your hypothesis?
  3. What is the practical trade-off of your material for real-world manufacturing and adoption?
* **Judge Defense Q&A Guide (Sample Questions Judges Will Ask):**
  * ❓ *"Why did you choose your specific ansatz and optimizer, and how do you know your VQE didn't get trapped in a local minimum?"*
  * ❓ *"If your candidate material delivers a higher cell voltage than Li–C, what physical or manufacturing downside did you sacrifice to achieve it?"*
  * ❓ *"How does the bond distance r affect binding energy and cell voltage, and why does over-expanding the host degrade performance?"*
  * ❓ *"For multivalent ions like Mg²⁺ or Al³⁺, why is the cell voltage divided by the valence z, and what advantage does multivalent transfer give in volumetric capacity?"*

---

## 🛠️ Troubleshooting & Pro-Tips

> [!TIP]
> **Pro-Tip (Warm Starting):** When looping over bond distances in Part 1, pass the optimal angles from distance $i$ as the `initial_params` for distance $i+1$! Because molecular geometry changes smoothly, optimal parameters are very close to the previous point, cutting your optimization time by **70%**.

> [!TIP]
> **Optimizer Settings:** Set `options={'maxiter': 50, 'ftol': 1e-5}` in SciPy's `minimize`. 50 iterations is plenty for smooth convergence and keeps your notebook snappy.

> [!NOTE]
> **Why is the Cell Voltage Negative of Binding Energy?**
> A chemical bond forms spontaneously when energy is released (ΔE < 0). In electrochemistry, by convention, battery cell voltage is defined as positive:
>
> **V_cell = -ΔE_bind / (z · e)**
>
> A binding energy of -3.42 eV with z = 1 yields a cell voltage of +3.42 Volts. For multivalent ions (Mg²⁺, Al³⁺, Zn²⁺), transferring multiple electrons per atom yields higher volumetric energy density even at moderate voltages!

---

## 🏆 Judging Rubric (100 Points)

| Category | Points | What Judges Look For |
| :--- | :---: | :--- |
| **Part 1: Hydrogen PES & Chemical Accuracy** | **10 pts** | Correct equilibrium bond distance R_e ≈ 0.735 Å, smooth PES curve, agreement with exact classical FCI within 1.6 mHa. |
| **Part 2: Lithium Baseline Voltage** | **20 pts** | Accurate calculation of binding energy ΔE_bind and cell voltage V_cell ≈ 3.42 V, clean VQE optimization. |
| **Part 3: Novel Discovery & Quantitative Correctness** | **45 pts** | **15 pts:** VQE convergence & ansatz implementation<br>**15 pts:** Materials exploration depth & distance sweep<br>**15 pts:** Quantitative verification & showdown bar chart |
| **Part 4: Presentation & Scientific Defense** | **25 pts** | Clear slide deck and oral defense explaining the physical trade-offs, answering judge questions with deep conceptual understanding. |

---

## 📤 Submission Instructions

1. Click **"Use this template"** at the top of this repository to create a **Private Repository** for your team: `qff26-battery-<team_name>`.
2. Add the hackathon judges as collaborators on GitHub.
3. Complete all work in `notebooks/02_challenge_submission.ipynb`. Ensure all plots and outputs are visible!
4. Submit your team's GitHub repository link and presentation slides via the **[Official Submission Form](https://forms.gle/qMA5vMGVBeEmbKMa9)** before the deadline.
