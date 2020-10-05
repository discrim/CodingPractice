from mpl_toolkits.mplot3d import Axes3D
from pylab import figure, show
import numpy as np

p1 = [[1], [2], [3]]
p2 = [[2], [3], [6]]
pp = np.concatenate((p1, p2), axis=1)
print(pp)

fig = figure(0)

ax = fig.add_subplot(111, projection='3d')

ax.plot3D(p1[0], p1[1], p1[2], '+r')
ax.plot3D(p2[0], p2[1], p2[2], '+b')
ax.plot3D(pp[0], pp[1], pp[2], 'g')

show()
