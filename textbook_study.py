import numpy as np

divider = "\n====================================================\n"

integers = np.array([[1, 2, 3], [4, 5, 6]])

floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])

print(integers)
print(floats)

print("determine array datatype")
print(integers.dtype)
print(floats.dtype)
print(divider)

print("determine array dimensions")
print(integers.ndim)
print(floats.ndim)

print(integers.shape)
print(floats.shape)

print(integers.size)
print(floats.size)

np.random.randint
