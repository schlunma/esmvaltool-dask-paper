# esmvaltool-dask-paper

Additional material to reproduce the results of Schlund et al. (2025). Results
are based on ESMValTool v2.8.0 and v2.11.0 (see details
[here](#Conda-environment-files-envs)).

## Quick Start

To install the exact same set of dependencies for ESMValTool versions 2.8.0 and
2.11.0 as used in the paper, conda environment files are provided (`envs/`).

ESMValTool recipes can be run with

```bash
esmvaltool run --config_file <path/to/config-user.yml> <path/to/recipe.yml>
```

Recipes (`recipes/`) and configuration (`config/`) files are available in this
repository. If absolute paths to diagnostic scripts are given in a recipe,
these paths need to be adapted so that they to point to the files given in this
repository. Dask configuration files need to be located at
`~/.esmvaltool/dask.yml`.

All recipes are run on a compute node on [DKRZ's
Levante](https://docs.dkrz.de/doc/levante/) to avoid interference from
processes run by other uses (which would be the case on a shared node). This
ensures that all results are comparable. The following `salloc` has been used
to reserve the resources:

```bash
salloc --x11 --account=<ACCOUNT_ID> --partition=compute --nodes=1 --mem=0 --time=08:00:00"
```

## Contents

### Configuration files (`config/`)

- `config-user.yml`: ESMValTool [user configuration
  file](https://docs.esmvaltool.org/projects/ESMValCore/en/v2.11.1/quickstart/configure.html#user-configuration-file),
  can be specified for an esmvaltool run via the command line argument
  `--config_file`.
- `dask_*.yml`: ESMValTool [Dask configuration
  files](https://docs.esmvaltool.org/projects/ESMValCore/en/v2.11.1/quickstart/configure.html#dask-distributed-configuration)
  for the different setups investigated in the paper. Must be put into
  `~/.esmvaltool/dask.yml`.

### ESMValTool diagnostic scripts (`diag_scripts/`)

[ESMValTool diagnostic
scripts](https://docs.esmvaltool.org/en/v2.11.0/develop/diagnostic.html#diagnostic)
used in the paper. Absolute paths to diagnostic scripts in the recipes need to
be adapted so that the paths point to these files.


### Conda environment files (`envs/`)

Contains [Conda environment
files](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
that can be used to install the exact set of dependencie for ESMValTool
versions 2.8.0 and 2.11.0 that have been used to conduct the analysis of this
paper.

### Figures and files to produce them (`figs/`)

Contains figures and corresponding files to produce them.

### ESMValTool recipes (`recipes/`)

[ESMValTool
recipes](https://docs.esmvaltool.org/projects/ESMValCore/en/v2.11.1/recipe/index.html)
used in the paper. Absolute paths to diagnostic scripts in the recipes need to
be adapted so that the paths point to the diagnostic scripts given in this
repository.

- `recipe_section-3-1_multi-model-analysis_*.yml`: Reproduce multi-model
  analysis presented in Section 3.1 of the paper.
- `recipe_section-3-2_high-res-model-analysis_*.yml`: Reproduce high-resolution
  model analysis presented in Section 3.2 of the paper.
- `_recipe_section-3-3_single-preprocessors_*.yml`: Reproduce individual
  preprocessor analysis presented in Section 3.3 of the paper.

*Note*: Different recipes for the different ESMValTool versions exist to
account for small API changes between ESMValTool v2.8.0 and v2.11.0.
