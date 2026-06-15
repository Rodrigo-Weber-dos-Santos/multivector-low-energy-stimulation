# Dependencies

## Figure scripts

The plotting scripts use Python 3 with:

- NumPy
- SciPy
- Matplotlib
- OpenPyXL, only for scripts that read `.xlsx` files

A simple setup is:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r environment/requirements.txt
```

On Windows PowerShell, the activation command is:

```powershell
.venv\Scripts\Activate.ps1
```

## Simulation code

The `code/cardiaxFull` directory contains the finite-element cardiac electrophysiology code used for the simulations. The original build notes are in `code/cardiaxFull/README.md`. The main external dependencies are PETSc, HDF5, Boost, Armadillo, BLAS/LAPACK, CMake and a C++ compiler.
