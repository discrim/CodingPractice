from numpy import asarray, arctan2, pi

rect = asarray([[1, -1, -1, 1], [1, 1, -1, -1]]).T
ang = arctan2(rect[:, 1], rect[:, 0]) * 180 / pi
print(ang)