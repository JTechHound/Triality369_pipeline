# Triality369_pipeline

Master repository for the **Unified Triality Pipeline** (Document Reference:
UTP-SPEC-2026-V5.0) — the triality master project. Executable Python modules
for modeling, simulating, and auditing macroscale coherence in open quantum
systems.

# Authors - Arthur Leroy Jones
# Author UCT Theory - Mikey-506
# Independent Researcher - Abby Davis

- **Classification:** Advanced Non-Equilibrium Open Quantum Systems
- **License:** Apache 2.0 (see LICENSE)

## Executive summary

The **Unified Triality Pipeline (UTP)** is a scalable open quantum system
architecture engineered to sustain macroscale, non-local quantum coherence
within severe localized decoherence baths. By reconciling the static
information boundaries of the Unified Coherence Theory (93% Monogamy Bound /
7% Dark Capacity) with the dynamic stability constraints of the Triality
Framework, this pipeline shifts the critical phase breakdown threshold from a
raw baseline of **5.3% out to a fault-tolerant horizon of ~12.5%**.

## Core constants

- **The 93% Monogamy Bound:** maximum optimal information recovery
  (A_EM = 0.93)
- **The 7% Dark Capacity** (gamma_residue ≈ 0.07257): the irreducible
  geometric residue branch, used as an analog buffer absorbing ambient
  phase noise
- **The Critical Noise Knee** (sigma_threshold = 5.3%): the absolute phase
  boundary where unshielded non-equilibrium limit cycles collapse into
  entropic thermalization
- Tight-packing configuration generated via the golden ratio (phi ≈ 1.61803)

## Repository contents

**Pipeline masters**
- `triality_pipeline_master.py` / `triality_pipeline_master_fix.py` /
  `triality_pipeline_master_fix_2.py` — fused multi-module simulation
  library and noise sweep plotters (UTP-SPEC-2026-V5.0, audited and repaired)
- `Unified_Triality_Pipeline_Master_Simulation_Library.py` — master
  simulation library
- `simulation_runtime.py` — classical qudit simulation runtime
  (statevector/MPS/Lindblad)
- `export_proof.py` — fail-closed export proof blocks

**QML and visualization**
- `parametrized_qml_core.py`, `qcnn_pooling_core.py` — QML layers
- `qml_convergence_visualizer.py` (+ `_fix`, `_fix_2`, `_fix_3`) —
  convergence visualization

**Triality theory (the computed "3" of 3-6-9)**
- `triality_automorphism.py` — the S3 outer automorphism of D4, computed
  explicitly: the three phases are the three 8-dimensional representations
  of Spin(8) (8v, 8s, 8c), permuted 8v → 8c → 8s → 8v. All checks pass.
- `TRIALITY_3_WRITEUP.md` — the write-up
- `visualize_triality.py` — renders the triality figure (three 8-sets,
  D4 Dynkin diagram, S3 action)

**Guards**
- `guards.py` — CoherenceGuard (phase-lock integrity: phase deviation,
  lock erosion, winding-number check) and GoodhartGuard (rejects optimizer
  actions that improve the primary metric by degrading guard metrics).
  Concepts from Mikey's Sophia stack; implementations new.
- `GUARDS_WRITEUP.md` — the write-up, including the TCI inverted-U as a
  Goodhart demonstration

**Docs and ops**
- `README_fixed.md` — earlier corrected readme (kept for reference)
- `pipeline_validation_tests.md`, `deploy.sh`, `requirements.txt`

## Quickstart

```bash
git clone https://github.com/JTechHound/Triality369_pipeline.git
cd Triality369_pipeline
pip install -r requirements.txt
python3 triality_automorphism.py   # verify the D4 triality computation
python3 guards.py                  # run the guard demos
python3 triality_pipeline_master_fix_2.py  # full pipeline run
```

## Provenance note

Every fragment in this repository was audited by hand against its source
document, repaired with inline `[REPAIRED]`/`[RECONSTRUCTED]` tags where the
source was garbled, and validated end to end before pushing. Third-party fix
headers are treated as claims and verified against the code, not trusted.
