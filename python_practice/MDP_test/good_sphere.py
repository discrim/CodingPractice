from numpy import empty, arange, sqrt, newaxis, pi, cos
from numpy.random import randn
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure, figaspect, show

def sph1(n,zmin):
    good = empty((4,n),float)
    bad = arange(n,dtype=int)
    while len(bad):
        # Add random points to replace all "bad" points
        np = randn(3,len(bad))
        np /= sqrt((np*np).sum(0))[newaxis,:]
        # Find which new points are ok
        ok = np[2,:]>zmin
        # Store them
        good[:3,bad[ok]] = np[:,ok]
        # Update list of bad points
        bad = bad[~ok]
    good[3,:] = 1
    return good

def sph2(n,polar_angle):
    good = empty((4,n),float)
    bad = arange(n,dtype=int)
    while len(bad):
        # Add random points to replace all "bad" points
        np = randn(3,len(bad))
        np /= sqrt((np*np).sum(0))[newaxis,:]
        # Find which new points are ok
        ok = np[2,:]>cos(polar_angle)
        # Store them
        good[:3,bad[ok]] = np[:,ok]
        # Update list of bad points
        bad = bad[~ok]
    good[3,:] = 1
    return good

sp1 = sph1(400, 0.8)
fig = figure(1, figsize=figaspect(1) * 1.5)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.scatter3D(sp1[0], sp1[1], sp1[2])

sp2 = sph2(400, 130 * pi / 180) 
fig = figure(2, figsize=figaspect(1) * 1.5)
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.scatter3D(sp2[0], sp2[1], sp2[2])

show()