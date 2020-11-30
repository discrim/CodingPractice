from torch import manual_seed
from torch.utils.data import random_split

lst0 = list(range(10))

manual_seed(23)

lst1, lst2 = random_split(lst0, [3, 7])
print(list(lst1))
print(list(lst2))

lst1, lst2 = random_split(lst0, [3, 7])
print(list(lst1))
print(list(lst2))

lst3, lst4, lst5 = random_split(lst0, [8, 1, 1])
print(list(lst3))
print(list(lst4))
print(list(lst5))