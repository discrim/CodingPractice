from numpy import zeros, asarray

aa = zeros((3, 3, 3))
for ii in range(27):
    aa[ii // 9, (ii % 9) // 3, ii % 3] = ii
#print(aa)
#print(aa.T)
print(aa[:, 0, :])
print(aa[:, 0, :].T)
