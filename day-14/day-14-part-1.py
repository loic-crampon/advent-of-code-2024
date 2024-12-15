# Restroom Redoubt - Part I
import os
import sys
import math

def calc_final_position(robot, height, width, seconds):
    init_x, init_y = robot['initial']
    vel_x, vel_y = robot['velocity']
    next_x = (init_x + vel_x * seconds) % width
    next_y = (init_y + vel_y * seconds) % height
    return (next_x, next_y)

def nb_in_quarters(height, width, robots):
    quarters = [0, 0, 0, 0]
    for robot in robots:
        x, y = robot['final']
        if (x >= 0) and (x < width//2) and (y >= 0) and (y < height//2):
            quarters[0] += 1
        if (x > width//2) and (x < width) and (y >= 0) and (y < height//2):
            quarters[1] += 1
        if (x > width//2) and (x < width) and (y > height//2) and (y < height):
            quarters[2] += 1
        if (x >= 0) and (x < width//2) and (y > height//2) and (y < height):
            quarters[3] += 1
    return quarters

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

robots = []
#height = 7
height = 103
#width = 11
width = 101
seconds = 100

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        split = line.strip().split(" ")
        robot = {
            'initial': tuple(int(x) for x in split[0].replace("p=","").split(",")),
            'velocity': tuple(int(x) for x in split[1].replace("v=","").split(","))
        }
        robots.append(robot)
        line = file.readline()

for robot in robots:
    robot['final'] = calc_final_position(robot, height, width, seconds)

print(math.prod(nb_in_quarters(height, width, robots)))