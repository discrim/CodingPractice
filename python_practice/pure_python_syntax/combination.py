A = ['a', 'b', 'c']
B = ['d', 'e', 'f', 'g']

for x in A:
    for y in B:
        print(x + y)

print([x + y for x in A for y in B])
