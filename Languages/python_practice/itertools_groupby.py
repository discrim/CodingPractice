from itertools import groupby

L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]

# Key function
func_take_zeroth = lambda x:x[0]

for key, group in groupby(L, func_take_zeroth):
    print(key + ": ", list(group))


a_list = [("Animal", "cat"),
          ("Animal", "dog"),
          ("Bird", "peacock"),
          ("Bird", "pigeon")]

an_iterator = groupby(a_list, lambda x:x[0])

print()

for key, group in an_iterator:
    key_and_groups = {key: list(group)}
    print(key_and_groups)

print()

an_iterator = groupby(a_list, lambda x:x[0])

for key, group in an_iterator:
    key_and_groups = {key: [elem[1] for elem in list(group)]}
    print(key_and_groups)