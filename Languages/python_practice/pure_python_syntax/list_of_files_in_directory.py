from os import listdir

myfiles = listdir("D:/Desktop/MDP/wavesdotpy/2020-06-03_measure_30deg")
print(myfiles)
txtfiles = [ff for ff in myfiles if ff.endswith(".txt")]
print(txtfiles)