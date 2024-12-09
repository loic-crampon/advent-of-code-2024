# Disk Fragmenter - Part I
import os
import sys

def map_to_blocks(disk_map):
    blocks = []
    for i in range(len(disk_map)):
        # files
        if (i % 2 == 0):
            blocks += disk_map[i]*[str(i//2)]
        # free spaces
        else:
            blocks += disk_map[i]*["."]
    return blocks

def find_first_free_block(blocks, start):
    for i in range(start, len(blocks)):
        if (blocks[i] == "."):
            return i
        
def defrag(blocks):
    disk_blocks = blocks[:]
    free_i = 0
    curr_i = len(disk_blocks) - 1
    while curr_i >= 0 and free_i < curr_i - 1:
        if (disk_blocks[curr_i] != '.'):
            free_i = find_first_free_block(disk_blocks, free_i)
            tmp = disk_blocks[free_i]
            disk_blocks[free_i] = disk_blocks[curr_i]
            disk_blocks[curr_i] = tmp
        curr_i = curr_i - 1
    return disk_blocks

def checksum(blocks):
    sum = 0
    for i in range(len(blocks)):
        if (blocks[i] != '.'):
            sum += int(blocks[i]) * i
    return sum

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

disk_map = []

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        disk_map = [int(x) for x in list(line.strip())]
        line = file.readline()

blocks = map_to_blocks(disk_map)

defrag = defrag(blocks)

print(checksum(defrag))