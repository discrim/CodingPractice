from numpy import asarray, block, newaxis, zeros
from scipy.linalg import expm

from numpy import asarray, zeros_like
def skew(vectors):
    """
    Convert input row vector(s) into corresponding
    skew-symmetric matrix (or skew matrix) for easy cross product.
    A square matrix is skew matrix iff -A = A.T
    Especially in 3 x 3 matrix, given a = [[x, y, z]],
    its skew matrix for cross product is
        skew(a) = [a]_cross = [[ 0, -z,  y],
                               [ z,  0, -x],
                               [-y,  x,  0]]
    so for any row vector b,
    cross(a, b) = dot(skew(a), b) is satisfied.
    
    REQUIRMENTS:
        from numpy import asarray, zeros_like
    
    PARAMETERS:
        vectors -- N x 3 --
            N row vectors with 3 columns each.
    
    RETURN:
        -- N x 3 x 3 --
        Corresponding skew-symmetric matrix.
    """
    vv = asarray(vectors)
    zz = zeros_like(vv[..., 0])
    return asarray([[ zz,
                      vv[..., 2],
                     -vv[..., 1]],
                    [-vv[..., 2],
                      zz,
                      vv[..., 0]],
                    [ vv[..., 1],
                     -vv[..., 0],
                      zz      ]]).T

def se3toSE3(tw):
    """
    Convert twist to rigid body motion in homogeneous representation
    
    REQUIRMENTS:
        from numpy import asarray, block, newaxis, zeros
        from scipy.linalg import expm
    
    INPUT:
        tw -- 6 -- twist: 3 rotation speeds, 3 translation 
      
    OUTPUT:
        -- 4 x 4 -- a homogenous transformation in SE(3)
        The last row is 0,0,0,1.
    """
    tw = asarray(tw)
    assert tw.ndim == 1 and tw.size == 6
    # Rigid body placement of antennae and hypotheses.
    return block([[expm(skew(tw[:3])), tw[3:, newaxis]],
                  [zeros((1, 3)), 1]                   ])

if __name__ == '__main__':
    print(se3toSE3((0, 0, 0, 5, 5, 0)))