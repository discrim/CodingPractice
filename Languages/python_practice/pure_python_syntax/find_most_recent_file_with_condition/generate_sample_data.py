from time import sleep

num_files = 10

for ii in range(num_files):
    with open("sample_data/sample_{:02d}.txt".format(ii), mode="w") as outfile:
        outfile.write("This is {:02d}th file.".format(ii))
    sleep(0.1)