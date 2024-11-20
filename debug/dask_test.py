from dask.distributed import Client
import dask.array as da
import xarray as xr
import numpy as np
from pathlib import Path


# Real data
paths = [
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19500101-19501231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19510101-19511231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19520101-19521231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19530101-19531231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19540101-19541231.nc',
]

# Dummy data
small_shape = (365, 1280, 2560)
big_shape = (366, 1280, 2560)
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
#     if "2" in str(path):
#         shape = big_shape
#     else:
#         shape = small_shape
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
#     if "2" in str(path):
#         shape = big_shape
#     else:
#         shape = small_shape
#     arr = da.random.random(shape, chunks=chunks)
#     da.to_zarr(arr, path)
#     print("Saved", path)
# print()


# Actual test code
# client = Client('tcp://127.0.0.1:35073')
# print("Using client", client)
# print()


# good
# arrs = [
#     da.random.random(big_shape, chunks=chunks) if "2" in str(p) else
#     da.random.random(small_shape, chunks=chunks) for p in zarr_paths
# ]

# bad
# arrs = [da.from_zarr(p) for p in zarr_paths]

# good
# dss = [xr.open_dataset(p, chunks={"time": 10, "lat": -1, "lon": -1}) for p in nc_paths]
# arrs = [ds.x.data for ds in dss]

# bad
dss = [xr.open_dataset(p, chunks={"time": 10, "lat": -1, "lon": -1}) for p in paths]
arrs = [ds.tas.data for ds in dss]


arr = da.concatenate(arrs, axis=0)
weights = da.ones_like(arr, chunks=arr.chunks)
avg = da.sum(arr * weights, axis=(1, 2)) / da.sum(weights, axis=(1, 2))
print("arr", arr)
print("weights", weights)
print("avg", avg)
print(avg.compute())
