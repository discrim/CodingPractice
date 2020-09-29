from numpy import asarray, newaxis

ant_spc = 0.04
xx = sorted( [1.5, 0.5, -0.5, -1.5] * 4, reverse=True)
xx = list( asarray( xx ) * ant_spc )
yy = list( asarray( [1.5, 0.5, -0.5, -1.5] * 4 ) * ant_spc )
zz = [0] * 16
ww = [1] * 16
antf = asarray( [xx, yy, zz, ww] )
antf[0, :] = antf[0, :] + 5
ant_cen = antf.mean(1)[:, newaxis]

print(antf)
print(ant_cen)