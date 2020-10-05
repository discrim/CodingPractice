import sys
print(sys.stdin.encoding)
print(sys.stdout.encoding)

s1 = 'alphabet'
s2 = '한글'

print(s1 == 'alphabet')
print(s1 != 'alphabet')
print(s1 == 'betalpha')
print(s1 != 'betalpha')

print(s2 == '한글')
print(s2 != '한글')
print(s2 == '글')
print(s2 != '글')