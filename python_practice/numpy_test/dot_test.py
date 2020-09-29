from numpy import asarray, dot, ones

aa = asarray([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
irange = range(aa.shape[0])
jrange = range(aa.shape[1])
bb = asarray([[0.1, 0.2], [0.3, 0.4]])
krange = range(bb.shape[0])

print("dot(aa, bb):\n", dot(aa, bb))

for ii in irange:
    for jj in jrange:
        for kk in krange:
            print("[%d, %d, %d]: %f" %
                  (ii, jj, kk, sum(aa[ii, jj, :] * bb[:, kk])))

print(aa.T)

oo = ones((2, 3, 4, 5))
print("oo.shape: ", oo.shape)
print("oo.T.shape: ", oo.T.shape)
