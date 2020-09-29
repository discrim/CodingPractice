from numpy import arange, meshgrid
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure, show

class SphereGrid:
    def __init__( self, center, radius, spacing ):
        pass
        
if __name__ == '__main__':
    xx = arange(4)
    yy = arange(4)
    zz = arange(4)
    XX, YY, ZZ= meshgrid(xx, yy, zz)
    fig = figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter3D(XX, YY, ZZ)
    show()