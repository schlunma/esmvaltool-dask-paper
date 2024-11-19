import iris
import iris.analysis
from iris.cube import CubeList
from dask.distributed import Client
import dask.array as da
from iris.fileformats.netcdf.loader import CHUNK_CONTROL

paths = [
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19500101-19501231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19510101-19511231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19520101-19521231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19530101-19531231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19540101-19541231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19550101-19551231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19560101-19561231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19570101-19571231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19580101-19581231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19590101-19591231.nc',
    '/work/bd0854/DATA/ESMValTool2/CMIP6_DKRZ/HighResMIP/MIROC/NICAM16-9S/highresSST-present/r1i1p1f1/day/tas/gr/v20190830/tas_day_NICAM16-9S_highresSST-present_r1i1p1f1_gr_19600101-19601231.nc',
]


client = Client('tcp://127.0.0.1:46269')
print("Using client", client)
print()

# Load
cubes = CubeList([])
for i, path in enumerate(paths):
    # with CHUNK_CONTROL.set(time=-1):
    with CHUNK_CONTROL.from_file():
        cube = iris.load_cube(path)
    cube.attributes = {}
    cubes.append(cube)

# Concatenate
cube = cubes.concatenate_cube()
print("after concat", cube.lazy_data(), cube.lazy_data().chunks)

# Operation
weights = da.ones(cube.shape, dtype=cube.dtype, chunks=cube.lazy_data().chunks)
print("weights", weights, weights.chunks)
# cube = cube.collapsed(['latitude', 'longitude'], iris.analysis.MEAN)  # works, clean task graph
cube = cube.collapsed(['latitude', 'longitude'], iris.analysis.MEAN, weights=weights)  # memory leak, very complicated task graph
print("after stats", cube.lazy_data(), cube.lazy_data().chunks)

# Compute
print(cube.data)
