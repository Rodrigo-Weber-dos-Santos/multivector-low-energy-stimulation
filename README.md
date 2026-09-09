# Multi-vector low-energy cardiac stimulation

This repository contains code, scripts, processed data, and figure-generation material associated with the manuscript:

**Multi-Vector Low-Energy Cardiac Stimulation Recruits Direction-Dependent Vascular and Boundary Hotspots**

## Repository contents

```text
code/
  cardiaxFull/                 C++ finite-element cardiac electrophysiology solver
  BidovsMono/                  Monodomain/bidomain comparison workflow
  CenterlinesToGeometry/       Python scripts for vascular centerline/geometric processing
scripts/
  run_protocols/               Shell scripts documenting the stimulation protocols
  make_figures/                Python scripts used to generate plots and assemble manuscript figures
data/
  processed_activation_times/  CSV and spreadsheet inputs used for activation-time analyses
  vascular_trees/              Vascular-tree centerlines, points and connectivity files
  meshes/                      Instructions for obtaining large mesh files from the release asset
figures/
  submission_2/                Latest figures for the submitted manuscript
  submission_1/                Earlier submitted-manuscript figure set
  source_panels/               Image panels used by the figure scripts
environment/
  requirements.txt             Python packages for figure scripts
  dependencies.md              Notes on Python and simulation-code dependencies
LICENSE                        MIT License for source code
LICENSE-DATA                   CC BY 4.0 license notice for data and figures
```

## Code directories

- `code/cardiaxFull/` contains the full Cardiax finite-element solver used for cardiac electrophysiology simulations, including monodomain/bidomain and related PDE components.
- `code/CenterlinesToGeometry/` contains the vascular-tree centerline and geometry-processing utilities used to prepare vessel structures.
- `code/BidovsMono/` contains the corrected monodomain/bidomain comparison workflow added for the manuscript revision. It includes the scikit-fem execution driver, the ten Tusscher--Panfilov ionic model, plotting scripts, archived corrected outputs, and the two generated comparison figures.

## Processed data

The main processed activation-time tables are available in:

```text
data/processed_activation_times/activation_times_protocol3_from_figure_scripts.csv
data/processed_activation_times/activation_times_protocol3_summary.csv
data/processed_activation_times/activation_times_ventricular_section_results_txt.csv
```

These files support the activation-time summaries and comparisons reported in the manuscript.

## Manuscript figures

The latest figure set for the submitted manuscript is available in:

```text
figures/submission_2/
```

This directory contains the figures referenced by the revised manuscript. The previous submitted figure set is retained in `figures/submission_1/`, and reusable image panels used by the figure-generation scripts are retained in `figures/source_panels/`.

The monodomain/bidomain comparison workflow also keeps its generated PDF and PNG outputs in `code/BidovsMono/figures/`; the manuscript-ready copies are included in `figures/submission_2/`.

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

The figure scripts load their local Matplotlib style files relative to the script location. Some scripts assemble panels from images in `figures/source_panels/`; if needed, adjust the image input paths in the script to match your local working directory.

## monodomain/bidomain comparison

The revision workflow in `code/BidovsMono/` can be run independently from that directory:

```bash
cd code/BidovsMono
python -m pip install -r requirements.txt
python run_corrected_skfem.py
```

This generates the corrected field sweep, activation maps, archived arrays, and comparison figures in `code/BidovsMono/out_corrected/` and `code/BidovsMono/figures/`. See `code/BidovsMono/README.md` for the exact plotting command used for the final 2 x 2 activation-map figure.

## Simulation scripts

The shell scripts in `scripts/run_protocols/` record the command-line stimulation protocols used with the monodomain solver. They can be launched from the repository root. By default, they look for meshes in `data/meshes/`; set `MESH_DIR` to use another mesh directory. If the `monodomain` executable is not on your `PATH`, set `MONODOMAIN` to the built solver executable:

```bash
export MONODOMAIN=/path/to/monodomain
export MESH_DIR=/path/to/mesh/files
bash scripts/run_protocols/script_arvore_4_dir.sh
```

## License

Source code in this repository is distributed under the MIT License. See `LICENSE`.

Research data, generated figures, and other non-code research outputs provided in the `data/` and `figures/` directories are distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) License. See `LICENSE-DATA`.

Third-party files included in the source tree retain their existing copyright and license notices.

## Citation

If you use this repository, please cite it using the metadata in `CITATION.cff`, which lists the manuscript-associated title, authors, and affiliations.
