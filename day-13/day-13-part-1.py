# Claw Contraption - Part I
import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

def find_min_token (a, b, dest):
    det = a[0]*b[1] - b[0]*a[1]
    if (det == 0):
        return 0

    num_a = dest[0]*b[1] - dest[1]*b[0]
    num_b = dest[1]*a[0] - dest[0]*a[1]

    if (num_a % det == 0) and (num_b % det == 0):
        a = num_a // det
        b = num_b // det
        return 3*a + b
    else: 
        return 0

machines = []
machine = []
data_machine_line = 1

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        if (line.strip() == ""):
            machines.append(machine)
            machine = []
            data_machine_line = 1
        else:
            if (data_machine_line == 1) or (data_machine_line == 2):
                data_machine = line.strip().split(" ")
                machine.append((int(data_machine[2].replace("X+", "").replace(",", "")), int(data_machine[3].replace("Y+", ""))))
                data_machine_line += 1
            else:
                data_machine = line.strip().split(" ")
                machine.append((int(data_machine[1].replace("X=", "").replace(",", "")), int(data_machine[2].replace("Y=", ""))))
        line = file.readline()
    machines.append(machine)

total_tokens = 0

for machine in machines:
    total_tokens += find_min_token(machine[0], machine[1], machine[2])
    
print(total_tokens)