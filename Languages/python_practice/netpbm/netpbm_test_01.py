from numpy import array, all, asarray
from netpbmfile import imwrite, imread, NetpbmFile

data = array([[0, 1], [65534, 65535]], dtype="uint16")
imwrite("_tmp.pgm", data)

image = imread("_tmp.pgm")
assert all(image == data)

with NetpbmFile("_tmp.pgm") as pgm:
    print(pgm.axes)
    print(pgm.shape)
    print(pgm.dtype)
    print(pgm.maxval)
    print(pgm.magicnum)
    image = pgm.asarray()