import string

def pick_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if letter in vowels:
        return True
    else:
        return False


def main1():
    abc_code = range(97, 123)
    print(abc_code)
    abc_char = [chr(elem) for elem in abc_code]
    print(abc_char)
    vowels = filter(pick_vowels, abc_char)
    # Same as vowels = [item for item in abc_char if pick_vowels(item)]
    
    print(list(vowels))

def myfilter(letter):
    pass


def main2():
    mystr = "\xb0"
    print(mystr)


if __name__ == '__main__':
    #main1()
    main2()