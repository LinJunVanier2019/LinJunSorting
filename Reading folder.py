
import csv

def make():
    lis = []
    temp_lis = []
    with open ("yagmai.txt") as tf:
        rtf = csv.reader(tf, delimiter = ",")
        for line in rtf:
            for p in range (len(line)):
                temp_lis.append(int(line[p]))
            lis.extend(temp_lis)
            temp_lis = []
    return lis

print (make())
