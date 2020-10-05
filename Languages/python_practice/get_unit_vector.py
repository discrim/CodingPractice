from numpy import zeros, asarray, newaxis, block
from numpy.random import randn
from scipy.linalg import norm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure, figaspect, show

num_elem = 16
origin = zeros( (3, 1) )
aa = zeros( ( 4, num_elem ) )
aa[:3, :] = randn( 3, num_elem )
aa /= norm( aa, axis=0 )
aa[3, :] = 1
print(aa)

fig = figure( 1, figsize=figaspect(1) * 1.5 )
ax = fig.add_subplot( 111, projection='3d' )
for nn in range( num_elem ):
    line = block( [origin, aa[:3, newaxis, nn]] )
    ax.plot( line[0], line[1], line[2] )
show()