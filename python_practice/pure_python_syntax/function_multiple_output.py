def quoNrem(dividend, divisor):
    return dividend // divisor, dividend % divisor

if __name__ == '__main__':
    a = quoNrem(13, 3)
    print(a)
