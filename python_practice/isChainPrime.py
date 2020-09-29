def isPrime(num):
    if num > 1:
        for ii in range(2, num):
            if num % ii == 0:
                primecheck = False
                break
            else:
                primecheck = True
    else:
        primecheck = False
    return primecheck

def intSlice(num):
    sn = str(num)
    le = len(sn)
    lst = []
    for ii in range(1, le + 1):
        for jj in range(0, le + 1 - ii):
            test = sn[jj:jj + ii]
            test = int(test)
            lst.append(test)
    print(lst)
    return lst

def isChainPrime(num):
    lst = intSlice(num)
    for ii in lst:
        if isPrime(ii):
            primecheck = True
        else:
            primecheck = False
            break
    return primecheck

if __name__ == "__main__":
    print(isChainPrime(12345))