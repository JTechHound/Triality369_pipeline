#!/usr/bin/env bash
# ================================================================
# TRIALITY369_PIPELINE — DEPENDENCY DEPLOYMENT SCRIPT
# Adapted 2026-10-05 from Triality-Manifest-Build's converged deploy.sh.
# Package matrix trimmed to what this repo's modules import:
#   numpy / matplotlib (master library, QML cores, visualizers,
#   unification core, simulation_runtime)
#   pytest (test suite)
# No cloud (boto3), lab-instrument (pyvisa), or quantum-SDK (qiskit)
# layers: this repo has no code that imports them.
# ================================================================
# [REPAIRED] line-break joins: "$VENV_NAME/bin/activate",
#   "${UNIFIED_LIBRARIES[@]}".
set -e

VENV_NAME=".venv"
REQ_FILE="requirements.txt"

echo "=== STARTING TRIALITY369 DEPENDENCY COMPILATION ==="

# 1. Initialize Hermetic Python Environment
if [ -d "$VENV_NAME" ]; then
    echo "[WARN] Purging old version footprints to insulate network..."
    rm -rf "$VENV_NAME"
fi
python3 -m venv "$VENV_NAME"
source "$VENV_NAME/bin/activate"
pip install --upgrade pip setuptools wheel

# 2. Define the Package Matrix
UNIFIED_LIBRARIES=(
    "numpy>=1.24.0"
    "matplotlib>=3.7.0"   # Curve plotters, visualizers, ASCII/figure output
    "pytest>=7.3.0"       # Automated test matrix
)

# 3. Stream and Write out the synchronized requirements.txt manifest
echo "# Triality369_pipeline Requirements Ledger" > "$REQ_FILE"
for lib in "${UNIFIED_LIBRARIES[@]}"; do
    echo "$lib" >> "$REQ_FILE"
done
echo "[SUCCESS] requirements.txt generated cleanly."

# 4. Deploy combined matrix package layers straight to disk
echo "[INSTALL] Ingesting component packages..."
pip install -r "$REQ_FILE"

echo -e "\n========================================================================"
echo -e "TRIALITY369 INFRASTRUCTURE INSTANTIATED SUCCESSFULLY"
echo -e "Active Environment Activation String: \033[1;36msource .venv/bin/activate\033[0m"
echo -e "========================================================================"
