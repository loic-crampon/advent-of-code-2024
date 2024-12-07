# Guard Gallivant - Part I
import os
import sys

def print_grid (grid):
    for l in range(len(grid)):
        for c in range(len(grid[l])):
            print(grid[l][c], end='')
        print()

def find_start_point (grid, symbol):
    for l in range(len(grid)):
        for c in range(len(grid[l])):
            if grid[l][c] == symbol:
                return (l, c)

def next_direction (grid, direction, position):
    # 1 = UP / 2 = RIGHT / 3 = DOWN / 4 = LEFT
    if (direction == 1):
        if (position[0] - 1 < 0):
            return 0
        elif (grid[position[0] - 1][position[1]] == "#"):
            return 2
        else:
            return 1
    elif (direction == 2):
        if (position[1] + 1 >= len(grid[position[0]])):
            return 0
        elif (grid[position[0]][position[1] + 1] == "#"):
            return 3
        else:
            return 2
    elif (direction == 3):
        if (position[0] + 1 >= len(grid)):
            return 0
        elif (grid[position[0] + 1][position[1]] == "#"):
            return 4
        else:
            return 3
    else:
        if (position[1] - 1 < 0):
            return 0
        elif (grid[position[0]][position[1] - 1] == "#"):
            return 1
        else:
            return 4

def count_visited_district (grid, symbol):
    count = 0
    for l in range(len(grid)):
        for c in range(len(grid[l])):
            if grid[l][c] == symbol:
                count += 1
    return count

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

grid = []

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        grid.append(line.strip())
        line = file.readline()

guard_point = find_start_point(grid, "^")
direction = 1

#print_grid (grid)
#print (guard_point)

while (direction != 0):
    direction = next_direction(grid, direction, guard_point)
    grid[guard_point[0]] = grid[guard_point[0]][:guard_point[1]] + "X" + grid[guard_point[0]][guard_point[1] + 1:]
    # 1 = UP / 2 = RIGHT / 3 = DOWN / 4 = LEFT
    if (direction == 1):
        guard_point = (guard_point[0] - 1, guard_point[1])
    if (direction == 2):
        guard_point = (guard_point[0], guard_point[1] + 1)
    if (direction == 3):
        guard_point = (guard_point[0] + 1, guard_point[1])
    if (direction == 4):
        guard_point = (guard_point[0], guard_point[1] - 1)

print(count_visited_district(grid, 'X'))