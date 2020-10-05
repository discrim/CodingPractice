from numpy import asarray, block, zeros, zeros_like, newaxis
from scipy.linalg import expm as expM

def skew( v ):
    """
    Convert a 3-vector to a skew matrix such that
      dot(skew(x),y) = cross(x,y)
  
    The function is vectorized, such that:
    INPUT:
      v -- N... x 3 -- input vectors
    OUTPUT:
      N... x 3 x 3
  
    For example:
    >>> skew([[1,2,3],[0,0,1]])
    array([[[ 0,  3, -2],
          [-3,  0,  1],
          [ 2, -1,  0]],
    <BLANKLINE>
         [[ 0,  1,  0],
          [-1,  0,  0],
          [ 0,  0,  0]]])
    """
    v = asarray(v).T
    z = zeros_like(v[0,...])
    return asarray([
        [ z, -v[2,...], v[1,...]],
        [v[2,...], z, -v[0,...] ],
        [-v[1,...], v[0,...], z ] ]).T

def se3toSE3(tw):
    """
    Convert twist to rigid body motion in homogeneous representation
    
    INPUT:
      tw -- 6 -- twist: 3 rotation speeds, 3 translation 
      
    OUTPUT: SKW
      SKW -- 4 x 4 -- a homogenous transformation in SE(3); last row 0,0,0,1 
    """
    tw = asarray(tw)
    assert tw.ndim == 1 and tw.size == 6
    # Rigid body placement of the antennae
    T = block([
        [expM(skew(tw[:3])), tw[3:,newaxis]],
        [ zeros((1,3)), 0]
    ])
    return T

if __name__ == '__main__':
    tw = [1, 0, 0, 2, 2, 2]
    TT = se3toSE3( tw )
    print(TT)