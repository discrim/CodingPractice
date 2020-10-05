def countFromList1(lst):
    st = set(lst)
    histo = dict()
    for key in st:
        histo[key] = 0
    
    for ii in range(len(lst)):
        histo[lst[ii]] +=1 
    
    return histo

def countFromList2(st, lst):
    histo = dict()
    for key in st:
        histo[key] = 0
    for ii in range(len(lst)):
        histo[lst[ii]] += 1
    return histo

def countFromList3(target, lst):
    count = 0
    for elem in lst:
        if target == elem:
            count += 1
    return count

if __name__ == '__main__':
    lst = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 6]
    st = set(lst)
    print(countFromList1(lst))
    print(countFromList2(st, lst))
    print(countFromList3(1, lst))
    print(lst.count(1))