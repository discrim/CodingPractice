from glob import glob
from os.path import getctime

allfiles = glob("sample_data/*")

for elem in allfiles:
    print(elem)

allfiles = [(elem, getctime(elem)) for elem in allfiles]
for elem in allfiles:
    print(elem)

sorted_list = sorted(allfiles, key=lambda x: x[1], reverse=True)
for elem in sorted_list:
    print(elem)