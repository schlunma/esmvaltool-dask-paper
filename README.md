[![DOI][zenodo-doi-shield]][zenodo-doi]
[![DOI][paper-doi-shield]][paper-doi]

[zenodo-doi]: https://doi.org/10.5281/zenodo.14361733
[zenodo-doi-shield]: https://zenodo.org/badge/DOI/10.5281/zenodo.14361733.svg
[paper-doi]: https://doi.org/10.5194/gmd-2024-236
[paper-doi-shield]: https://zenodo.org/badge/DOI/10.5194/gmd-2024-236.svg

# esmvaltool-dask-paper

Additional material to reproduce the results of
[Schlund et al. (2025)](https://doi.org/10.5194/gmd-2024-236). Results
are based on ESMValTool v2.8.0 and v2.11.0.

## Quick Start

To install the exact same set of dependencies for ESMValTool versions 2.8.0 and
2.11.0 as used in the paper, conda environment files are provided (`envs/`).

ESMValTool recipes can be run with

```bash
esmvaltool run --config_file <path/to/config-user.yml> <path/to/recipe.yml>
```

Recipes (`recipes/`) and configuration (`config/`) files are available in this
repository (configuration files are tailored towards running the recipes on
[DKRZ's Levante](https://docs.dkrz.de/doc/levante/)). Output paths in the
configuration file might need to be adapted. If absolute paths to diagnostic
scripts are given in a recipe, these paths need to be adapted so that they to
point to the files given in this repository. The Dask configuration files need
to be renamed and put to `~/.esmvaltool/dask.yml` (one by one).

To reproduce the results on another machine, automatic downloads of CMIP data
can be enable in the configuration file, i.e.,

```yml
search_esgf: when_missing  # enable automatic downloads for CMIP data
download_dir: ~/climate_data  # directory where downloaded data is stored
```

All setups run on Levante use a compute node to avoid interference from
processes run by other uses (which would be the case on a shared node).  This
ensures that all results are comparable. The following `salloc` command has
been used to allocate the resources:

```bash
salloc --x11 --account=<ACCOUNT_ID> --partition=compute --nodes=1 --mem=0 --time=08:00:00"
```

## Contents

### Configuration files (`config/`)

Contains the following files:

- `config-user.yml`: ESMValTool [user configuration
  file](https://docs.esmvaltool.org/projects/ESMValCore/en/v2.11.1/quickstart/configure.html#user-configuration-file),
  can be specified for an ESMValTool run via the command line argument
  `--config_file`. Output paths might need to be adapted. The given
  configuration file can be used to run recipes on Levante. To use another
  machine, automatic download of CMIP data can be enabled (see above).
- `dask_*.yml`: ESMValTool [Dask configuration
  files](https://docs.esmvaltool.org/projects/ESMValCore/en/v2.11.1/quickstart/configure.html#dask-distributed-configuration)
  for the different setups investigated in the paper. Must be renamed and put
  into `~/.esmvaltool/dask.yml` (one by one). For the setup that uses 2 nodes,
  the scheduler needs to be started outside of ESMValTool to avoid waiting until
  resources are granted (see details in `dask_hpc_2_nodes.yml`).

### ESMValTool diagnostic scripts (`diag_scripts/`)

Contains [ESMValTool diagnostic
scripts](https://docs.esmvaltool.org/en/v2.11.0/develop/diagnostic.html#diagnostic)
used in the paper. Absolute paths to diagnostic scripts in the recipes need to
be adapted so that the paths point to these files.


### Conda environment files (`envs/`)

Contains [conda environment
files](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
that can be used to install the exact same set of dependencies for ESMValTool
versions 2.8.0 and 2.11.0 that have been used to conduct the analysis of this
paper.

### Figures and files to produce them (`figs/`)

Contains figures and corresponding files to produce them.

### ESMValTool recipes (`recipes/`)

Contains [ESMValTool
recipes](https://docs.esmvaltool.org/projects/ESMValCore/en/v2.11.1/recipe/index.html)
used in the paper. Absolute paths to diagnostic scripts in the recipes need to
be adapted so that the paths point to the diagnostic scripts given in this
repository.

- `recipe_section-3-1_multi-model-analysis_*.yml`: Reproduce multi-model
  analysis presented in Section 3.1 of the paper.
- `recipe_section-3-2_high-res-model-analysis_*.yml`: Reproduce high-resolution
  model analysis presented in Section 3.2 of the paper.
- `recipe_section-3-3_single-preprocessors_*.yml`: Reproduce individual
  preprocessor analysis presented in Section 3.3 of the paper.

*Note*: Different recipes for the different ESMValTool versions exist to
account for small API changes between ESMValTool v2.8.0 and v2.11.0.

### Scripts (`scripts/`)

Contains other scripts used to reproduce the results of the paper, e.g., to
extract ESMValTool runtimes from log files.
