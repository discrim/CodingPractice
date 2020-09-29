from numpy.random import rand

aa = rand(10)
aa.sort()

bb = enumerate(aa)
for ii in bb:
    print(ii)