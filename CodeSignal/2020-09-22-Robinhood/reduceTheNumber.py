# Seems working

def reduceTheNumber(number, k):
    stnum = str(number)
    
    newlst = []
    while(len(stnum) > k):
        chunks = [stnum[ii:ii + k] for ii in range(0, len(stnum), k)]
        for ii, elem in enumerate(chunks):
            ssum = 0
            for digit in elem:
                ssum += int(digit)
            chunks[ii] = str(ssum)
        stnum = "".join(chunks)
    return stnum
        

if __name__ == "__main__":
    print(reduceTheNumber('1111122222', 3))
    print(reduceTheNumber('1111122222', 5))