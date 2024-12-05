import os
import sys
import re

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

def mult (str):
    valeurs = [int(x) for x in str.replace("mul(", "").replace(")", "").split(",")]
    return valeurs[0] * valeurs[1]

sum = 0

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        multiplications = re.findall(pattern, line) 
        for multiplication in multiplications:
            sum += mult(multiplication)
        line = file.readline()

print(sum)