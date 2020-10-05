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
    
    REQUIREMENTS:
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

if __name__ == '__main__':
    aa = asarray([[1, 2, 3], [4, 5, 6]])
    print(skew(aa))
    bb = asarray([1, 2, 3])
    print(skew(bb))