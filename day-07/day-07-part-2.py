# Bridge Repair - Part II
import os
import sys

OPERATORS = ['+', '*', '|']

def generate_combinations(n, valeurs):
    if n == 0:
        return [[]]
    combinations = []
    for val in valeurs:
        for sub_comb in generate_combinations(n - 1, valeurs):
            combinations.append([val] + sub_comb)
    return combinations

def valid_equation (equation):
    result = equation[0]
    values = equation[1:]

    operation_combinations = generate_combinations(len(values) - 1, OPERATORS)
    
    for opration_combination in operation_combinations:
        operation = values[0]
        for i in range(1, len(values)):
            if opration_combination[i-1] == '+':
                operation = operation + values[i] 
            elif opration_combination[i-1] == '*':
                operation = operation * values[i] 
            else:
                operation = int(str(operation) + str(values[i]))
        if operation == result:
            return result

    return 0

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

total_calibration = 0

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        equation = [int(n.replace(":","")) for n in line.strip().split(' ')]
        total_calibration += valid_equation (equation)
        line = file.readline()

print(total_calibration)