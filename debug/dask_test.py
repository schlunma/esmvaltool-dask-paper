from dask.distributed import Client
import dask.array as da


client = Client('tcp://127.0.0.1:40365')
print("Using client", client)
print()

array = da.ones((3000, 1280, 2560), chunks=("auto", -1, -1))
weights_2d = da.ones((1280, 2560))

weights_3d = da.broadcast_to(weights_2d, shape=array.shape, chunks=array.chunks)

avg = da.average(array, axis=(1, 2), weights=weights_3d)

print("array", array)
print("weights_2d", weights_2d)
print("weights_3d", weights_3d)
print("avg", avg)

print(avg.compute())



# arr = da.ones((1280, 2560))
# broad_arr = 

# n = 11
# small_shape = (365, 1280, 2560)
# large_shape = (n * small_shape[0], *small_shape[1:])
# chunks = (10, 1280, 2560)
# # chunks = (-1, "auto", "auto")

# # x = da.ones(large_shape, chunks=chunks)

# arrs = [da.ones(small_shape, chunks=chunks) for _ in range(n)]
# # arrs = [da.ones(small_shape) for _ in range(n)]
# x = da.concatenate(arrs, axis=0)

# w = da.ones(x.shape, chunks=x.chunksize)
# print("x", x, x.chunks)
# print("w", w, w.chunks)

# y = da.average(x, axis=(1, 2), weights=w)
# print("y", y, y.chunks)

# print(y.compute())
