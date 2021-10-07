from time import time

import numpy as np

repeat = 1
a = np.random.rand(1000, 500)

start_t = time()
for _ in range(repeat):
    np.sum(a, axis=1)
end_t = time()
print("np.sum: ", end_t - start_t)

start_t = time()
for _ in range(repeat):
    b = np.ones((500, 1))
    a @ b
end_t = time()
print("make 1 mat + matmul: ", end_t - start_t)