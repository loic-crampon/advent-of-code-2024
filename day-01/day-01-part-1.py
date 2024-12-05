import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

listA = []
listB = []
result = 0

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        split = line.strip().split("   ")
        listA.append(int(split[0]))
        listB.append(int(split[1]))
        line = file.readline()

listA = sorted(listA)
listB = sorted(listB)

for i in range(len(listA)):
    result += abs(listA[i] - listB[i])

print(result)