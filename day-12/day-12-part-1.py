# Garden Groups - Part I
import os
import sys

def print_garden(garden, width, height):
    for l in range(height):
        for c in range(width):
            print(garden[l][c], end="")
        print()

def area_cost (garden, width, heigth, l, c, plant):
    if (l >= 0) and (l < heigth) and (c >= 0) and (c < width) and (garden[l][c] == plant):
        garden[l][c] = plant.lower()
        border = 0
        if l == 0:
            border += 1
        else:
            if (garden[l - 1][c] != plant) and (garden[l - 1][c] != plant.lower()):
                border += 1
        if c == 0:
            border += 1
        else:
            if (garden[l][c - 1] != plant) and (garden[l][c - 1] != plant.lower()):
                border += 1
        if l == height - 1:
            border += 1
        else:
            if (garden[l + 1][c] != plant) and (garden[l + 1][c] != plant.lower()):
                border += 1
        if c == width - 1:
            border += 1
        else:
            if (garden[l][c + 1] != plant) and (garden[l][c + 1] != plant.lower()):
                border += 1
        return [border] + area_cost(garden, width, height, l + 1, c, plant) + area_cost(garden, width, height, l - 1, c, plant) + area_cost(garden, width, height, l, c + 1, plant) + area_cost(garden, width, height, l, c - 1, plant)
    else:
        return []

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

garden = []

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        garden.append(list(line.strip()))
        line = file.readline()

height = len(garden)
width = len(garden[0])

total_cost = 0

for l in range(height):
    for c in range(width):
        if (garden[l][c] != garden[l][c].lower()):
            costs = area_cost(garden, width, height, l, c, garden[l][c])
            total_cost += len(costs) * sum(costs)

print(total_cost)
