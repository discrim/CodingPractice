from numpy import asarray, newaxis

aa = asarray([1, 2, 3, 4, 5, 6, 7, 8]).reshape(2, 2, 2)
print(aa)
print(aa.mean(axis=2))
bb = aa[:, 0, 0][:, newaxis, newaxis]
print(bb)
cc = aa / bb
print(cc)