from timeit import timeit

#a = str(input('Enter a string divisible by 3: '))
#assert len(a) % 3 == 0, 'String not divisible by 3'

#b = a.replace('aba', 'KKK')
#print(b)
a = 'abababababab'
setup = "a = 'abababababab'"

t1 = timeit(
stmt="""
b = ''
for i in range(len(a) // 3):
    tmp = a[i*3:i*3+3]
    tmp = tmp.replace('aba', 'KKK')
    b += tmp
#print(b)
""",
setup=setup)
print(t1)

t2 = timeit(
stmt="""
b = ''
for i in range(len(a) // 3):
    b += a[i*3:i*3 + 3].replace('aba', 'KKK')
#print(b)
""",
setup=setup)
print(t2)

t3 = timeit(
stmt="""
b = ''.join([a[i*3:i*3 + 3].replace('aba', 'KKK') for i in range(len(a) // 3)])
#print(b)
""",
setup=setup)
print(t3)