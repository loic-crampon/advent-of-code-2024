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

def clear_mult (str):
    sum = 0
    good_mults = re.findall(pattern, str) 
    for m in good_mults:
        sum += mult(m)
    return sum

result = 0
data = ""

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        data += line
        line = file.readline()
        
dont_split = data.split("don't()")
result += clear_mult(dont_split[0])

for dont in dont_split[1:]:
    do_split = dont.split("do()")
    for do in do_split[1:]:
        result += clear_mult(do)

print(result)