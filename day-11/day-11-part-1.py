# Plutonian Pebbles - Part I
import os
import sys
import functools

@functools.cache
def blink_stone(stone, iteration, max_iteration):
    if iteration == max_iteration:
        return 1
    if (stone == '0'):
        return blink_stone('1', iteration + 1, max_iteration)
    elif (len(stone) % 2 == 0):
        return blink_stone(str(int(stone[:len(stone)//2])), iteration + 1, max_iteration) + blink_stone(str(int(stone[len(stone)//2:])), iteration + 1, max_iteration)
    else:
        return blink_stone(str(int(stone) * 2024), iteration + 1, max_iteration)

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

stones = []
times = 25

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        stones += line.strip().split(" ")
        line = file.readline()

number_of_stones = 0

for stone in stones:
    number_of_stones += blink_stone(stone, 0, times)

print(number_of_stones)