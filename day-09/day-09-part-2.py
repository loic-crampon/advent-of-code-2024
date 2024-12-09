# Disk Fragmenter - Part II
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

def size_of_file(disk_map):
    files = {}
    for i in range(len(disk_map)):
        if (i % 2 == 0):
            files[str(i//2)] = disk_map[i]
    return files

def find_first_free_block(blocks, size):
    size_block = 0
    for i in range(len(blocks)):
        if (blocks[i] == "."):
            size_block += 1
        else:
            size_block = 0
        if (size_block == size):
            return i - size_block + 1
    return -1

def defrag(blocks, files):
    disk_blocks = blocks[:]
    free_i = 0
    curr_i = len(disk_blocks) - 1
    while curr_i >= 0:
        if (disk_blocks[curr_i] != '.'):
            size_of_file = files[disk_blocks[curr_i]]
            free_i = find_first_free_block(disk_blocks, size_of_file)
            if (free_i < curr_i) and(free_i != -1):
                disk_blocks = disk_blocks[:free_i] + disk_blocks[curr_i - size_of_file + 1:curr_i + 1] + disk_blocks[free_i + size_of_file:curr_i - size_of_file + 1] + size_of_file*["."] + disk_blocks[curr_i + 1:]
            curr_i = curr_i - size_of_file
        else:
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

files = size_of_file(disk_map)

defrag = defrag(blocks, files)

print(checksum(defrag))