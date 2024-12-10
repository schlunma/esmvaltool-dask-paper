# esmvaltool-dask-paper

Additional material to reproduce the results of Schlund et al. (2025). Results
are based on ESMValTool v2.11.0 (see details
[here](#Conda-environment-files-`envs/`)).

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

### Conda environment files (`envs/`)

- `v2.8.0.yml`: [Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for ESMValTool version 2.8.0.
- `v2.11.0.yml`: [Conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html) for ESMValTool version 2.11.0.
