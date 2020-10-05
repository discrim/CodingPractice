def digitSum(dec):
    if dec // 10 == 0:
        return dec
    else:
        return dec % 10 + digitSum(dec // 10)

if __name__ == '__main__':
    print(digitSum(48961))