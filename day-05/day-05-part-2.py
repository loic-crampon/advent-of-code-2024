# Print Queue - Part I
import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

def is_correct_update(update, rules):
    is_correct = True
    first_page_ind = 0
    while (first_page_ind < len(update) - 1) and is_correct:
        second_page_ind = first_page_ind + 1
        while (second_page_ind < len(update)) and is_correct:
            if [update[second_page_ind], update[first_page_ind]] in rules:
                is_correct = False
            second_page_ind += 1
        first_page_ind += 1
    return is_correct

def reordering_update(update, rules):
    current_update = update[:]
    while not(is_correct_update(current_update, rules)):
        first_page_ind = 0
        while (first_page_ind < len(current_update) - 1):
            second_page_ind = first_page_ind + 1
            while (second_page_ind < len(current_update)):
                if [current_update[second_page_ind], current_update[first_page_ind]] in rules:
                    temp = current_update[second_page_ind]
                    current_update[second_page_ind] = current_update[first_page_ind]
                    current_update[first_page_ind] = temp
                    second_page_ind += 1
                second_page_ind += 1
            first_page_ind += 1
    return current_update
        
read_page_ordering_rules = True
page_ordering_rules = []
updates = []

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        if (read_page_ordering_rules):
            if (line.strip() != ''):
                page_ordering_rules.append([int(x) for x in line.strip().split('|')])
            else:
                read_page_ordering_rules = False
        else:
            updates.append([int(x) for x in line.strip().split(",")])
        line = file.readline()

sum_middle_page = 0

for update in updates:
    if not(is_correct_update(update, page_ordering_rules)):
        reordered_update = reordering_update(update, page_ordering_rules)
        sum_middle_page += reordered_update[int(len(reordered_update) / 2)]

print(sum_middle_page)