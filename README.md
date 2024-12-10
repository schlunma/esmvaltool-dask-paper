# esmvaltool-dask-paper

Additional material to reproduce the results of Schlund et al. (2025).

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
