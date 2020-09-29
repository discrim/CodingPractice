def test1():
    from numpy import newaxis, arange, meshgrid
    tt = arange(5)
    xx, yy = meshgrid(tt, tt)
    d3 = xx[:, newaxis, :] - yy[:, :, newaxis]
    print("xx: \n", xx)
    print("yy: \n", yy)
    print("d3: \n", d3)

def test2():
    from numpy import ones, arange, asarray, newaxis
    aa = arange(4)
    bb = asarray([aa, aa, aa, aa])
    print("bb: ", bb)
    mm = bb.mean(axis=1)
    print("mm: ", mm)
    mm = bb.mean(axis=1)[:, newaxis]
    print("mm: ", mm)

if __name__ == '__main__':
    # test1()
    test2()