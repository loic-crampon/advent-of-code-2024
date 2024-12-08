# Resonant Collinearity - Part I
import os
import sys

def get_antenna_position (map):
    antennas = {}
    for l in range(len(map)):
        for c in range(len(map[l])):
            if (map[l][c] != '.'):
                if map[l][c] not in antennas:
                    antennas[map[l][c]] = []
                antennas[map[l][c]].append((l, c))
    return antennas

def calc_antinodes (antennas, width_map, height_map):
    antinodes = []
    for key, values in antennas.items():
        if (len(values) > 1):
            for point_a in range(len(values) - 1):
                for point_b in range(point_a + 1, len(values)):
                    dist_x = values[point_a][0] - values[point_b][0]
                    dist_y = values[point_a][1] - values[point_b][1]

                    antiniode_a = (values[point_a][0] + dist_x, values[point_a][1] + dist_y)
                    if (antiniode_a[0] >= 0) and (antiniode_a[0] < width_map) and (antiniode_a[1] >= 0) and (antiniode_a[1] < height_map):
                        if antiniode_a not in antinodes:
                            antinodes.append(antiniode_a)

                    antiniode_b = (values[point_b][0] - dist_x, values[point_b][1] - dist_y)
                    if (antiniode_b[0] >= 0) and (antiniode_b[0] < width_map) and (antiniode_b[1] >= 0) and (antiniode_b[1] < height_map):
                        if antiniode_b not in antinodes:
                            antinodes.append(antiniode_b)
    return antinodes
                

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

map = []

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        map.append(list(line.strip()))
        line = file.readline()

width_map = len(map)
height_map = len(map[0])

antennas = get_antenna_position(map)
antinodes = calc_antinodes(antennas, width_map, height_map)

print(len(antinodes))