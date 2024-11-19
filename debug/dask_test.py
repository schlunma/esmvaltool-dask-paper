from dask.distributed import Client
import dask.array as da


client = Client('tcp://127.0.0.1:46269')
print("Using client", client)
print()

n = 11
small_shape = (365, 1280, 2560)
large_shape = (n * small_shape[0], *small_shape[1:])
# chunks = (10, 1280, 2560)
chunks = (-1, "auto", "auto")

# Works well, clean task graph
# x = da.ones(large_shape, chunks=chunks)

# Workers keep dying, very complicated dask graph
arrs = [da.ones(small_shape, chunks=chunks) for _ in range(n)]
# arrs = [da.ones(small_shape) for _ in range(n)]
x = da.concatenate(arrs, axis=0)

w = da.ones(x.shape, chunks=x.chunksize)
print("x", x, x.chunks)
print("w", w, w.chunks)

y = da.average(x, axis=(1, 2), weights=w)
print("y", y, y.chunks)

print(y.compute())
