def alternatingSort(a):
    leng = len(a)
    b = []
    for ii in range((leng + 1) // 2):
        b.append(a[ii])
        b.append(a[leng - ii - 1])
    if leng % 2 == 1:
        b.pop()
    
    print(b)
    
    for ii in range(leng - 1):
        if b[ii] >= b[ii + 1]:
            return False
    return True

if __name__ == "__main__":
    in1 = [-92, -23, 0, 45, 89, 96, 99, 95, 89, 41, -17, -48]
    print(alternatingSort(in1))