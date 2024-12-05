import numpy as np

a = np.arange(4).reshape(2, 2)

print(a)

print(a.diagonal())
print(a.diagonal(1))
print(a.diagonal(-1))
