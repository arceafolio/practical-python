# pcost.py
#
# Exercise 1.27

import csv
import sys
def ReadFile(filename):
    file = open(filename)
    f = csv.reader(file)
    header = next(f)
    cost = 0
    for line in f:
        try:
            #row = line.split(',')
            cost = cost + int(line[1]) * float(line[2])
        except ValueError:
            print("Couldn't handle " , line)
    # print(f'Total cost', cost)
    file.close()
    return cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = ReadFile(filename)
print('Total cost', cost)