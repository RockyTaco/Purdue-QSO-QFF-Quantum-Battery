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

Today's commercial EV batteries rely on **Lithium intercalated into Graphite ($Li-C$)**, delivering roughly $3.4\text{ to }3.7\text{ Volts}$. While reliable, this chemistry is hitting fundamental walls:

1. **Scarcity & Cost:** Lithium extraction is geographically concentrated and environmentally destructive.
2. **Capacity Limits:** Graphite can only hold one lithium atom for every six carbon atoms ($LiC_6$).
3. **Safety & Degradation:** Fast charging causes metallic lithium needles ("dendrites") to grow, shorting the battery and causing fires.

To build the next generation of energy storage, scientists are racing to find **alternative elements and electrode materials**:
* Can cheap, table-salt-derived **Sodium ($Na$)** replace lithium for large-scale grid storage?
* Can a **Silicon ($Si$)** anode store $10\times$ more energy for 1,000-mile EV range?
* Can **heteroatom-doped carbon ($N$-doped)** trap ions more securely to prevent battery fires?

> [!NOTE]
> Because electron correlation at molecular interfaces is fundamentally quantum mechanical, classical supercomputers struggle to calculate binding energies accurately. You will use **Qiskit** and the **Variational Quantum Eigensolver (VQE)** to simulate these atomic bonds and discover what makes a superior battery!

---

## 🗺️ Challenge Roadmap

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │                     THE NEXT-GEN BATTERY DISCOVERY RACE                     │
 └──────────────────────────────────────┬──────────────────────────────────────┘
                                        │
        ┌───────────────────────────────┴───────────────────────────────┐
        ▼                                                               ▼
┌──────────────────────────────────────┐  ┌──────────────────────────────────────┐
│ PART 1: THE TRAINING GROUND (10 pts) │  │ PART 2: THE INDUSTRY BENCHMARK       │
│ Molecular Hydrogen (H₂) PES Sweep    │  │ Lithium-Graphite (Li–C) Anode (20 pts│
├──────────────────────────────────────┤  ├──────────────────────────────────────┤
│ • Learn how molecules become circuits│  │ • Simulate today's standard EV anode │
│ • Run VQE with StatevectorEstimator  │  │ • Calculate binding energy: ΔE_bind  │
│ • Plot equilibrium bond well (0.74 Å)│  │ • Derive cell voltage: V_cell = -ΔE/e│
│ • Achieve chemical accuracy (1.6 mHa)│  │ • Benchmark established: ~3.42 Volts │
└──────────────────────────────────────┘  └──────────────────────────────────────┘
                                        │
                                        ▼
        ┌───────────────────────────────────────────────────────────────┐
        │ PART 3: NOVEL MATERIALS DISCOVERY (45 pts)                    │
        │ "Can You Find a Better Chemistry? Can You Prove It?"          │
        ├───────────────────────────────────────────────────────────────┤
        │ Move beyond standard graphite! Test alternative elements:     │
        │                                                               │
        │ • 🌊 Sodium-Ion (Na–C): Abundant, ultra-cheap grid storage    │
        │ • 💎 Silicon Anode (Li–Si): 10x capacity for extreme EV range │
        │ • 🔥 N-Doped Carbon (Li–C_N): Enhanced binding, fire-safe     │
        │ • 🧪 Advanced Candidate: Custom geometry / elemental model    │
        │                                                               │
        │ Deliverable: Run VQE on your candidate, compute the new cell  │
        │ voltage, build a Showdown Comparison, and defend your design! │
        └───────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
        ┌───────────────────────────────────────────────────────────────┐
        │ PART 4: PRESENTATION & SCIENTIFIC DEFENSE (25 pts)            │
        │ Present and defend your discovered material to the judges     │
        └───────────────────────────────────────────────────────────────┘
```

---

## 💡 What Does "Better" Mean in Battery Engineering?

In real-world battery development, no single material is "best" at everything. **"Better" depends on your design objective:**

| Engineering Dimension | Candidate Chemistry | How It Improves on the Baseline ($Li-C$) |
| :--- | :---: | :--- |
| **1. Maximum Cell Voltage ($V_{\text{cell}}$)** | **Silicon Anode (`'Li-Si'`)** | Delivers higher voltage ($\sim 3.78\text{ V}$) and holds up to $10\times$ more lithium atoms per gram, unlocking longer electric vehicle range. |
| **2. Cost & Raw Material Abundance** | **Sodium-Ion (`'Na-C'`)** | Replaces expensive, scarce Lithium with cheap, abundant Sodium. Drops voltage to $\sim 2.95\text{ V}$, but reduces raw cell material costs by $>80\%$ for stationary solar/wind grid storage. |
| **3. Safety & Fire Prevention** | **Nitrogen-Doped (`'Li-N-doped'`)** | Nitrogen atoms create polar trapping sites that bind lithium tightly ($\sim 3.92\text{ V}$), preventing metallic lithium dendrites from piercing the separator. |

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

### Part 1: The Training Ground — Molecular Hydrogen ($H_2$) `[10 Points]`
* **Goal:** Understand how quantum circuits find lowest-energy states (ground states).
* **Step-by-Step Instructions:**
  1. Load the pre-packaged $H_2$ Hamiltonian across bond distances $R \in [0.4, 2.5]\text{ \AA}$ using `get_h2_hamiltonian(r)`.
  2. Build a parameterized ansatz (`EfficientSU2`) with 2 qubits and linear entanglement.
  3. Run VQE using Qiskit's `StatevectorEstimator` with SciPy's `SLSQP` or `COBYLA` optimizer.
  4. Plot the potential energy curve, find the equilibrium bond distance $R_e \approx 0.735\text{ \AA}$, and verify chemical accuracy ($\le 1.6\text{ mHa}$) using `check_part1()`.

### Part 2: The Industry Benchmark — Lithium on Carbon ($Li-C$) `[20 Points]`
* **Goal:** Simulate the commercial standard EV battery anode.
* **The Physics:**
  When lithium binds into the electrode host material, energy is released:
  $$\Delta E_{\text{bind}} = E(Li\text{-}C) - \left[ E(C\text{-host}) + E(Li) \right]$$
  This binding energy directly dictates the **theoretical battery cell voltage**:
  $$V_{\text{cell}} = -\frac{\Delta E_{\text{bind}}}{e} \quad (\text{Industry Target: } \approx 3.42\text{ V})$$
* **Step-by-Step Instructions:**
  1. Load the pre-packaged 4-qubit $Li-C$ Hamiltonian using `get_battery_hamiltonian('Li-C')`.
  2. Optimize your VQE circuit to find the ground state energy $E(Li\text{-}C)$.
  3. Compute $\Delta E_{\text{bind}}$ and $V_{\text{cell}}$ using `calculate_battery_voltage()`.
  4. Verify your baseline voltage using `check_part2()`.

### Part 3: Novel Materials Discovery & Verification `[45 Points]`
* **Goal:** Discover and evaluate an alternative battery chemistry that solves a real-world energy storage problem.
* **Step-by-Step Instructions:**
  1. Choose a candidate chemistry from the table (`'Na-C'`, `'Li-Si'`, `'Li-N-doped'`, or a custom model).
  2. Load the Hamiltonian with `get_battery_hamiltonian(chosen_chemistry)`.
  3. Run VQE to find its ground state energy and calculate its new cell voltage using `check_part3()`.
  4. Generate the side-by-side **Materials Showdown Comparison** bar chart with `plot_materials_showdown()`.
  5. Fill in the Part 4 Scientific Defense table comparing your candidate against the baseline.

### Part 4: Presentation & Scientific Defense `[25 Points]`
* **Goal:** Defend your discovered battery chemistry to the judges. With AI tools widely available, the presentation and oral defense is the ultimate test of whether your team truly understands the physics, simulation results, and practical trade-offs.
* **What to prepare:**
  1. Which engineering dimension did you prioritize (voltage, cost, safety), and why?
  2. How do the quantum simulation numbers verify your hypothesis?
  3. What is the practical trade-off of your material for real-world manufacturing and adoption?

---

## 🛠️ Troubleshooting & Pro-Tips

> [!TIP]
> **Pro-Tip (Warm Starting):** When looping over bond distances in Part 1, pass the optimal angles from distance $i$ as the `initial_params` for distance $i+1$! Because molecular geometry changes smoothly, optimal parameters are very close to the previous point, cutting your optimization time by **70%**.

> [!TIP]
> **Optimizer Settings:** Set `options={'maxiter': 50, 'ftol': 1e-5}` in SciPy's `minimize`. 50 iterations is plenty for smooth convergence and keeps your notebook snappy.

> [!NOTE]
> **Why is the Cell Voltage Negative of Binding Energy?**
> A chemical bond forms spontaneously when energy is released ($\Delta E < 0$). In electrochemistry, by convention, battery cell voltage is defined as positive ($V = -\Delta E / e$). A binding energy of $-3.42\text{ eV}$ yields a cell voltage of $+3.42\text{ Volts}$.

---

## 🏆 Judging Rubric (100 Points)

| Category | Points | What Judges Look For |
| :--- | :---: | :--- |
| **Part 1: Hydrogen PES & Chemical Accuracy** | **10 pts** | Correct equilibrium bond distance $R_e$, smooth PES curve, agreement with exact classical FCI within $1.6\text{ mHa}$. |
| **Part 2: Lithium Baseline Voltage** | **20 pts** | Accurate calculation of binding energy $\Delta E_{\text{bind}}$ and cell voltage $V_{\text{cell}} \approx 3.42\text{ V}$, clean optimization. |
| **Part 3: Novel Discovery & Quantitative Correctness** | **45 pts** | Successful quantum simulation of an alternative battery chemistry, correct energy convergence, and verified voltage calculations. |
| **Part 4: Presentation & Scientific Defense** | **25 pts** | Clear slide deck and oral defense explaining the physical trade-offs, proving deep understanding of the results beyond AI assistance. |

---

## 📤 Submission Instructions

1. Click **"Use this template"** at the top of this repository to create a **Private Repository** for your team: `qff26-battery-<team_name>`.
2. Add the hackathon judges as collaborators on GitHub.
3. Complete all work in `notebooks/02_challenge_submission.ipynb`. Ensure all plots and outputs are visible!
4. Submit your private repository link and presentation slides via the hackathon submission portal before the deadline.
