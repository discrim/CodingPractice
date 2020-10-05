from mpl_toolkits.mplot3d import Axes3D
from numpy import (
    zeros, ones, arange, dot, newaxis, block, meshgrid, cross,
    asarray, zeros_like, sqrt, exp, argsort, arccos, where, c_
)
from scipy.linalg import norm, pinv, expm as expM
from numpy.random import randn, rand
from pylab import figure, show

# Antenna grid 
ant0 = ones((4,4,4))
# print(ant0)
ant0[:2] = meshgrid(arange(ant0.shape[2]),arange(ant0.shape[1]))
# print(ant0)
ant0[2,...]=0
# print(ant0)

#sz = (21,21,21)
sz = (1, 1, 1)
asz = asarray(sz)
xyz = ones( (4,)+sz )
#xyz = ones((4,))
print(xyz)
