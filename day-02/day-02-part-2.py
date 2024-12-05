import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

def is_safe(report):
    safe = False
    if (report == sorted(report) or report == sorted(report, reverse=True)):
        safe = True
        i = 0
        while ((i < len(report) - 1) and safe):
            if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
                safe = False
            i += 1
    return safe


reportSafe = 0

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        report = [int(x) for x in line.strip().split(" ")]
        if (is_safe(report)):
            reportSafe += 1
        else:
            i = 0
            safe = False
            while (i < len(report) and not(safe)):
                copy_of_report = report[:]
                copy_of_report.pop(i)
                if is_safe(copy_of_report):
                    reportSafe += 1
                    safe = True
                i += 1
        line = file.readline()

print(reportSafe)