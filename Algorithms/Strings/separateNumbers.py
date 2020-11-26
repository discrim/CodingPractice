def separateNumbers(s):
    result = None
    for idx in range(1, len(s) // 2 + 1):
        start_num = s[:idx]
        if sweep(s, start_num):
            result = "YES " + start_num
    if result == None:
        result = "NO"
    print(result)

def sweep(s, start_num):
    if not s:
        return True
    if s.startswith(start_num):
        begin_idx = len(start_num)
        return sweep(s[begin_idx:], str(int(start_num) + 1))
    return False


if __name__ == "__main__":
    inputs = ["1234", "91011", "99100", "101103", "010203", "13", "1", "99910001001", "7891011", "9899100", "999100010001"]
    for inp in inputs:
        separateNumbers(inp)