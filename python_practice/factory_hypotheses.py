class AbstractHypothesesFactory:
    def createHypotheses( self ):
        pass

class ConcreteHypothesesFactory( AbstractHypothesesFactory ):
    def createHypotheses( self, hypo_type ):
        if hypo_type == 'cube':
            return CubeHypotheses()
        elif hypo_type == 'sphere':
            return SphereHypotheses()

class AbstractHypotheses:
    def __init__( self ):
        self._xyzf = None
    
    def get_xyzf( self ):
        return self._xyzf

class CubeHypotheses( AbstractHypotheses ):
    def __init__( self ):
        self._xyzf = "Cube"

class SphereHypotheses( AbstractHypotheses ):
    def __init__( self ):
        self._xyzf = "Sphere"


if __name__ == '__main__':
    h1 = ConcreteHypothesesFactory().createHypotheses('cube')
    print(h1.get_xyzf())
