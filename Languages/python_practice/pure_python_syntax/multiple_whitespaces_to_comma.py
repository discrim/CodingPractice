def ws2cm(str):
    import re
    str = re.sub('\s+', ',', str)
    return str


if __name__ == '__main__':
    str1 = "Monty Python's   Adventure  Yeah"
    print(ws2cm(str1))