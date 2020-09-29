def main():
    n_tc = int(input()) # Number of test cases
    for nn in range(n_tc):
        n_elem = int(input()) # Number of integers in current case
        arr = list(map(int, input().rstrip().split()))
        result = longestArithmetic(arr)
        print('Case #%d: %d' % (nn + 1, result))

def longestArithmetic(arr):
    diff = []
    for ii in range(len(arr) - 1):
        diff.append(arr[ii + 1] - arr[ii])
    best_leng = longestEqual(diff) + 1
    return best_leng

def longestEqual(arr):
    best_leng = -1
    curr_leng = 1
    leng = 1
    for ii in range(len(arr) - 1):
        if arr[ii] == arr[ii + 1]:
            leng += 1
            best_leng = leng
        else:
            leng = 1
    return best_leng

if __name__ == "__main__":
    main()