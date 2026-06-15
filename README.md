# Multi-vector low-energy cardiac stimulation

This repository contains code, scripts, processed data and figure-generation material associated with the manuscript:

**Multi-Vector Low-Energy Cardiac Stimulation Recruits Direction-Dependent Vascular and Boundary Hotspots**

## Repository contents

```text
code/
  cardiaxFull/                 Finite-element cardiac electrophysiology code
  CenterlinesToGeometry/       Scripts for vascular centerline/geometric processing
scripts/
  run_protocols/               Shell scripts with the stimulation protocols
  make_figures/                Python scripts used to generate plots and assemble figures
data/
  processed_activation_times/  CSV tables used for activation-time analyses
  vascular_trees/              Vascular-tree centerlines, points and connectivity files
  meshes/                      Instructions for obtaining large mesh files from the release asset
figures/
  final/                       Rendered figures
  source_panels/               Image panels used by the figure scripts
environment/
  requirements.txt             Python packages for figure scripts
  dependencies.md              Notes on Python and simulation-code dependencies
```

## Processed data

The main processed activation-time tables are available in:

```text
data/processed_activation_times/activation_times_protocol3_from_figure_scripts.csv
data/processed_activation_times/activation_times_protocol3_summary.csv
data/processed_activation_times/activation_times_ventricular_section_results_txt.csv
```

These files support the activation-time summaries and comparisons reported in the manuscript.

## Large mesh files

The large ventricular-section mesh files are distributed as a GitHub release asset named:

```text
large_meshes.zip
```

After downloading it, unzip it in the repository root. The files should appear as:

```text
data/meshes/teste.xml
data/meshes/testeNoTree.xml
data/meshes/arvoreCoracao.trelis
```

## Running figure scripts

Install the Python dependencies:

```bash
pip install -r environment/requirements.txt
```

Then run the desired script from the repository root, for example:

```bash
python scripts/make_figures/Times_Directions.py
python scripts/make_figures/BoxPlotBorderTree.py
```

Some figure scripts assemble panels from images in `figures/source_panels/`; if needed, adjust the relative paths in the script to match your local working directory.

## Simulation scripts

The shell scripts in `scripts/run_protocols/` record the command-line stimulation protocols used with the monodomain solver. The environment variable `MESH_DIR` can be used to point the scripts to the local folder containing the mesh files:

```bash
export MESH_DIR=/path/to/mesh/files
bash scripts/run_protocols/script_arvore_4_dir.sh
```

## Citation

If you use this repository, please cite the associated manuscript.
