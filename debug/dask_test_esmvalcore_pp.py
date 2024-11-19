from iris.cube import CubeList
from dask.distributed import Client
import esmvalcore.preprocessor as pp

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


client = Client('tcp://127.0.0.1:35609')
print("Using client", client)
print()

# Load
cubes = CubeList([])
for path in paths:
    new_cubes = pp.load(path)
    cubes.extend(new_cubes)

# Concatenate
cube = pp.concatenate(cubes)
print("after concat", cube.lazy_data())

# Operation
# cube = pp.area_statistics(cube, operator='mean', weights=False)  # works, clean task graph
cube = pp.area_statistics(cube, operator='mean')  # memory leak, more complicated task graph
print("after stats", cube.lazy_data())

# Compute
print(cube.data)
