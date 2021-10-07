# https://www.geeksforgeeks.org/how-to-generate-2-d-gaussian-array-using-numpy/
# https://www.geeksforgeeks.org/perspective-transformation-python-opencv/

import numpy as np
import matplotlib.pyplot as plt

# x좌표, y좌표 초기화. 각각 -1부터 1까지를 11개로 나눔.
x, y = np.meshgrid(np.linspace(-1, 1, 11), np.linspace(-1, 1, 11))
dst = np.sqrt(x * x + y * y)
print(x.shape, y.shape)
print(x)
print(y)
print(dst.shape)
print(dst)

# 가우스 분포 인자 (분산, 평균) 초기화.
sigma = 1
mu = 0

# 가우스 분포 계산
gauss = np.exp(-0.5 * ((dst - mu) / sigma) ** 2)
print(gauss)

plt.imshow(gauss)
plt.show()