# Warehouse Woes - Part I
import os
import sys

def print_grid (grid, width, height):
    for l in range(height):
        for c in range(width):
            print(grid[l][c], end='')
        print()

def find_robot_position (grid, width, height):
    for l in range(height):
        for c in range(width):
            if (grid[l][c] == '@'):
                return (l, c)

def move (grid, point, robot, movement):
    lp, cp = point
    lr, cr = robot

    if (movement == "<"):
        lm, cm = (0, -1)
    elif (movement == "^"):
        lm, cm = (-1, 0)
    elif (movement == ">"):
        lm, cm = (0, 1)
    else:
        lm, cm = (1, 0)

    if (grid[lp][cp] == "@"):
        if (grid[lp + lm][cp + cm] == "#"):
            return (lr, cr)
        elif (grid[lp + lm][cp + cm] == "."):
            grid[lp + lm][cp + cm] = "@"
            grid[lp][cp] = '.'
            return (lp + lm, cp + cm)
        else:
            return move(grid, (lp + lm, cp + cm), robot, movement)
    elif (grid[lp][cp] == 'O'):
        if (grid[lp + lm][cp + cm] == "#"):
            return robot
        elif (grid[lp + lm][cp + cm] == "."):
            grid[lp + lm][cp + cm] = "O"
            grid[lp][cp] = '.'
            return move(grid, robot, robot, movement)
        else:
            return move(grid, (lp + lm, cp + cm), robot, movement)

def sum_of_box_distance (grid, width, height):
    sum = 0
    for l in range(height):
        for c in range(width):
            if (grid[l][c] == 'O'):
                sum += l * 100 + c
    return sum

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

grid = []
read_grid = True
moves = ''

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        if (line.strip() == ''):
            read_grid = False
        if (read_grid):
            grid.append(list(line.strip()))
        else:
            moves += line.strip()
        line = file.readline()

height = len(grid)
width = len(grid[0])
robot = find_robot_position(grid, width, height)

for m in moves:
    robot = move (grid, robot, robot, m)

print(sum_of_box_distance(grid, width, height))