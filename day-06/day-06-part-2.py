# Guard Gallivant - Part II
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

def next_direction (grid, historic, direction, position):
    # 1 = UP / 2 = RIGHT / 3 = DOWN / 4 = LEFT
    if (direction == 1):
        if (position[0] - 1 < 0):
            return 0
        elif (grid[position[0] - 1][position[1]] == "#"):
            if (historic[position[0]][position[1] + 2] == '2'):
                return -1
            else:
                return 2
        elif (historic[position[0] - 1][position[1]] == '1'):
            return -1
        else:
            return direction
    elif (direction == 2):
        if (position[1] + 1 >= len(grid[position[0]])):
            return 0
        elif (grid[position[0]][position[1] + 1] == "#"):
            if (historic[position[0] + 1][position[1]] == '3'):
                return -1
            else:
                return 3
        elif (historic[position[0]][position[1] + 1] == '2'):
            return -1
        else:
            return direction
    elif (direction == 3):
        if (position[0] + 1 >= len(grid)):
            return 0
        elif (grid[position[0] + 1][position[1]] == "#"):
            if (historic[position[0]][position[1] - 1] == '4'):
                return -1
            else:
                return 4
        elif (historic[position[0] + 1][position[1]] == '3'):
            return -1
        else:
            return direction
    else:
        if (position[1] - 1 < 0):
            return 0
        elif (grid[position[0]][position[1] - 1] == "#"):
            if (historic[position[0] - 1][position[1]] == '1'):
                return -1
            else:
                return 1
        elif (historic[position[0]][position[1] - 1] == '4'):
            return -1
        else:
            return direction

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

count_infinite_loop = 0

for l in range(len(grid)):
    for c in range(len(grid[l])):
        guard_point = find_start_point(grid, "^")
        direction = 1
        current_grid = grid[:]
        if (l, c) != guard_point and current_grid[l][c] != '#':
            current_grid[l] = current_grid[l][:c] + "#" + current_grid[l][c + 1:]
        historic_grid = current_grid[:]

        while (direction > 0):
            if (historic_grid[guard_point[0]][guard_point[1]] == '.'):
                historic_grid[guard_point[0]] = historic_grid[guard_point[0]][:guard_point[1]] + str(direction) + historic_grid[guard_point[0]][guard_point[1] + 1:]
            current_grid[guard_point[0]] = current_grid[guard_point[0]][:guard_point[1]] + str(direction) + current_grid[guard_point[0]][guard_point[1] + 1:]
            direction = next_direction(current_grid, historic_grid, direction, guard_point)
            # 1 = UP / 2 = RIGHT / 3 = DOWN / 4 = LEFT
            if (direction == 1) and (current_grid[guard_point[0] - 1][guard_point[1]] != "#"):
                guard_point = (guard_point[0] - 1, guard_point[1])
            if (direction == 2) and (current_grid[guard_point[0]][guard_point[1] + 1] != "#"):
                guard_point = (guard_point[0], guard_point[1] + 1)
            if (direction == 3) and (current_grid[guard_point[0] + 1][guard_point[1]] != "#"):
                guard_point = (guard_point[0] + 1, guard_point[1])
            if (direction == 4) and (current_grid[guard_point[0]][guard_point[1] - 1] != "#"):
                guard_point = (guard_point[0], guard_point[1] - 1)

        if (direction == -1):
            count_infinite_loop += 1

print(count_infinite_loop)