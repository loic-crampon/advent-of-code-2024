import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

def xmas_diagonal_down (grid, l, c):
    return (l < len(grid) - 2) and (c < len(grid[l]) - 2) and (grid[l][c] == 'M') and (grid[l+1][c+1] == 'A') and (grid[l+2][c+2] == 'S')

def xmas_diagonal_down_reverse (grid, l, c):
    return (l < len(grid) - 2) and (c < len(grid[l]) - 2) and (grid[l][c] == 'S') and (grid[l+1][c+1] == 'A') and (grid[l+2][c+2] == 'M')

def xmas_diagonal_up (grid, l, c):
    return (l < len(grid) - 2) and (c < len(grid[l]) - 2) and (grid[l][c+2] == 'M') and (grid[l+1][c+1] == 'A') and (grid[l+2][c] == 'S')

def xmas_diagonal_up_reverse (grid, l, c):
    return (l < len(grid) - 2) and (c < len(grid[l]) - 2) and (grid[l][c+2] == 'S') and (grid[l+1][c+1] == 'A') and (grid[l+2][c] == 'M')

def x_mas_at_coord (grid, l, c):
    nb = 0
    if xmas_diagonal_down(grid, l, c) and xmas_diagonal_up(grid, l, c):
        nb += 1
    elif xmas_diagonal_down_reverse(grid, l, c) and xmas_diagonal_up(grid, l, c):
        nb += 1
    elif xmas_diagonal_down(grid, l, c) and xmas_diagonal_up_reverse(grid, l, c):
        nb += 1
    elif xmas_diagonal_down_reverse(grid, l, c) and xmas_diagonal_up_reverse(grid, l, c):
        nb += 1
    return nb

grid = []
nb_xmas = 0

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        grid.append(line.strip())
        line = file.readline()

for l in range(len(grid)):
    for c in range(len(grid[0])):
        nb_xmas += x_mas_at_coord(grid, l, c)

print(nb_xmas)