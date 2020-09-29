from numpy import asarray
from numpy.random import randn
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.pyplot import figure, show

numpts = 5
aa = randn( 3, numpts )

fig = figure( 1 )
ax = fig.add_subplot( 111, projection='3d' )
for current in aa.T:
    ax.scatter( current[0], current[1], current[2] )
show()