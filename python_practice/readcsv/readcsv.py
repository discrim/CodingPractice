import csv

if 1:
    with open('output3.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            #print(', '.join(row))
            print(row)


if 0:
    csvfile = open('output3.txt', newline='')
    csv_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    print(csv_reader)

