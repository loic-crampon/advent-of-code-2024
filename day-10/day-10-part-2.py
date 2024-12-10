# Hoof It - Part II
import os
import sys

def find_path(nines, map, height, width, l, c, next_value):
    if (map[l][c] == 9):
        nines.append((l, c))
    if (l > 0) and (map[l-1][c] == next_value):
        find_path(nines, map, height, width, l - 1, c, map[l-1][c] + 1)
    if (l < height - 1) and (map[l+1][c] == next_value):
        find_path(nines, map, height, width, l + 1, c, map[l+1][c] + 1)
    if (c > 0) and (map[l][c-1] == next_value):
        find_path(nines, map, height, width, l, c - 1, map[l][c-1] + 1)
    if (c < width - 1) and (map[l][c+1] == next_value):
        find_path(nines, map, height, width, l, c + 1, map[l][c+1] + 1)

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

map = []

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        map.append([int(x) for x in list(line.strip())])
        line = file.readline()

height = len(map)
width = len(map[0])

trailheads_sum = 0

for l in range(height):
    for c in range(width):
        if (map[l][c] == 0):
            nines = []
            find_path(nines, map, height, width, l, c, 1)
            trailheads_sum += len(nines)

print(trailheads_sum)