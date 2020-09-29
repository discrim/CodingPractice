def pairSummingToPowerOfTwo(a):
    le = len(a)
    count = 0
    for ii in range(le):
        for jj in range(ii, le):
            if (isPowerOfTwo(a[ii] + a[jj])):
                print(ii, jj)
                count += 1
    return count


def isPowerOfTwo(nn):
    return (nn and (not (nn & (nn - 1))))


if __name__ == "__main__":
    print(pairSummingToPowerOfTwo([1, -1, 2, 3]))