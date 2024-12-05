import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

def xmas_line (grid, l, c):
    return (c < len(grid[l]) - 3) and (grid[l][c] == 'X') and (grid[l][c+1] == 'M') and (grid[l][c+2] == 'A') and (grid[l][c+3] == 'S')

def xmas_line_reverse (grid, l, c):
    return (c < len(grid[l]) - 3) and (grid[l][c] == 'S') and (grid[l][c+1] == 'A') and (grid[l][c+2] == 'M') and (grid[l][c+3] == 'X')

def xmas_column (grid, l, c):
    return (l < len(grid) - 3) and (grid[l][c] == 'X') and (grid[l+1][c] == 'M') and (grid[l+2][c] == 'A') and (grid[l+3][c] == 'S')

def xmas_column_reverse (grid, l, c):
    return (l < len(grid) - 3) and (grid[l][c] == 'S') and (grid[l+1][c] == 'A') and (grid[l+2][c] == 'M') and (grid[l+3][c] == 'X')

def xmas_diagonal_down (grid, l, c):
    return (l < len(grid) - 3) and (c < len(grid[l]) - 3) and (grid[l][c] == 'X') and (grid[l+1][c+1] == 'M') and (grid[l+2][c+2] == 'A') and (grid[l+3][c+3] == 'S')

def xmas_diagonal_down_reverse (grid, l, c):
    return (l < len(grid) - 3) and (c < len(grid[l]) - 3) and (grid[l][c] == 'S') and (grid[l+1][c+1] == 'A') and (grid[l+2][c+2] == 'M') and (grid[l+3][c+3] == 'X')

def xmas_diagonal_up (grid, l, c):
    return (l < len(grid) - 3) and (c < len(grid[l]) - 3) and (grid[l][c+3] == 'X') and (grid[l+1][c+2] == 'M') and (grid[l+2][c+1] == 'A') and (grid[l+3][c] == 'S')

def xmas_diagonal_up_reverse (grid, l, c):
    return (l < len(grid) - 3) and (c < len(grid[l]) - 3) and (grid[l][c+3] == 'S') and (grid[l+1][c+2] == 'A') and (grid[l+2][c+1] == 'M') and (grid[l+3][c] == 'X')

def nb_xmas_at_coord (grid, l, c):
    nb = 0
    if xmas_line(grid, l, c):
        nb += 1
    if xmas_line_reverse(grid, l, c):
        nb += 1
    if xmas_column(grid, l, c):
        nb += 1
    if xmas_column_reverse(grid, l, c):
        nb += 1
    if xmas_diagonal_down(grid, l, c):
        nb += 1
    if xmas_diagonal_down_reverse(grid, l, c):
        nb += 1
    if xmas_diagonal_up(grid, l, c):
        nb += 1
    if xmas_diagonal_up_reverse(grid, l, c):
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
        nb_xmas += nb_xmas_at_coord(grid, l, c)

print(nb_xmas)