# Garden Groups - Part II
import os
import sys

def print_garden(garden, width, height):
    for l in range(height):
        for c in range(width):
            print(garden[l][c], end="")
        print()

def area_size (garden, width, heigth, l, c, plant):
    if (l >= 0) and (l < heigth) and (c >= 0) and (c < width) and (garden[l][c] == plant):
        garden[l][c] = '.'
        return 1

def area_cost (garden, width, heigth, l, c, plant):
    if (l >= 0) and (l < heigth) and (c >= 0) and (c < width) and (garden[l][c] == plant):
        garden[l][c] = plant.lower()
        borders = []
        if (l == 0):
            borders.append("U" + str(l) + "B")
        else:
            if (garden[l - 1][c] != plant) and (garden[l - 1][c] != plant.lower()):
                borders.append("U" + str(l) + "B")
        if c == 0:
            borders.append("L" + str(c) + "B")
        else:
            if (garden[l][c - 1] != plant) and (garden[l][c - 1] != plant.lower()):
                borders.append("L" + str(c) + "B")
        if l == height - 1:
            borders.append("D" + str(l) + "B")
        else:
            if (garden[l + 1][c] != plant) and (garden[l + 1][c] != plant.lower()):
                borders.append("D" + str(l) + "B")
        if c == width - 1:
            borders.append("R" + str(c) + "B")
        else:
            if (garden[l][c + 1] != plant) and (garden[l][c + 1] != plant.lower()):
                borders.append("R" + str(c) + "B")
        return [borders] + area_cost(garden, width, height, l + 1, c, plant) + area_cost(garden, width, height, l - 1, c, plant) + area_cost(garden, width, height, l, c + 1, plant) + area_cost(garden, width, height, l, c - 1, plant)
    else:
        return []
    
def border_length (costs):
    return len(set([element for sous_liste in costs for element in sous_liste]))

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
            print(garden[l][c])
            costs = area_cost(garden, width, height, l, c, garden[l][c])
            print(costs)
            print(len(costs))
            print(border_length(costs))
            total_cost += len(costs) * border_length(costs)

print(total_cost)
