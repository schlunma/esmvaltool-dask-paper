from dask.distributed import Client
from dask_jobqueue import SLURMCluster
import dask.array as da
import xarray as xr
import numpy as np
from pathlib import Path
from pprint import pprint
from time import sleep


print("Start script")
sleep(5)
print("Start script for real")


# Real data
paths = [
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19500101-19501231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19510101-19511231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19520101-19521231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19530101-19531231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19540101-19541231.nc',
]

# Dummy data
shape = (365, 1280, 2560)
chunks = (10, -1, -1)
out_dir = Path("/scratch/b/b309141/tmp")
nc_paths = [
    out_dir / "1.nc",
    out_dir / "2.nc",
    out_dir / "3.nc",
    out_dir / "4.nc",
    out_dir / "5.nc",
]
zarr_paths = [
    out_dir / "1.zarr",
    out_dir / "2.zarr",
    out_dir / "3.zarr",
    out_dir / "4.zarr",
    out_dir / "5.zarr",
]

# print("Saving nc")
# for path in nc_paths:
#     arr = xr.DataArray(
#         da.random.random(shape, chunks=chunks),
#         name="x",
#         dims=("time", "lat", "lon"),
#     )
#     arr.to_netcdf(path)
#     print("Saved", path)
# print()

# print("Saving zarr")
# for path in zarr_paths:
#     arr = da.random.random(shape, chunks=chunks)
#     da.to_zarr(arr, path)
#     print("Saved", path)
# print()


# Actual test code
# cluster = SLURMCluster(queue="interactive", account="bd1179", cores=8, processes=2, n_workers=2, memory="8GB", interface="ib0", local_directory='/scratch/b/b309141/dask-tmp', walltime="00:30:00")
# client = Client(cluster.scheduler_address)
# # client = Client('tcp://127.0.0.1:37811')
# print("Using client", client)
# print()


# good
arrs = [da.random.random(shape, chunks=chunks) for _ in zarr_paths]

# bad
# arrs = [da.from_zarr(p) for p in zarr_paths]

# bad
# dss = [xr.open_dataset(p, chunks={"time": 10, "lat": -1, "lon": -1}) for p in nc_paths]
# arrs = [ds.x.data for ds in dss]

# bad
# dss = [xr.open_dataset(p, chunks={"time": 10, "lat": -1, "lon": -1}) for p in paths]
# arrs = [ds.tas.data for ds in dss]


arr = da.concatenate(arrs, axis=0)
weights = da.ones_like(arr, chunks=arr.chunks)
avg = da.sum(arr * weights, axis=(1, 2)) / da.sum(weights, axis=(1, 2))
print("arrs")
pprint(arrs)
print("arr", arr)
print("weights", weights)
print("avg", avg)
print(avg.dask)
print(avg.compute())
