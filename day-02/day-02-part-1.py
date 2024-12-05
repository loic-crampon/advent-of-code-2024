import os
import sys

filename = "input.txt"
if (len(sys.argv) > 1):
    filename = sys.argv[1]
filelocation = os.path.dirname(os.path.abspath(__file__)) + "/" + filename

reportSafe = 0

with open(filelocation, "r") as file:
    line = file.readline()
    while line:
        report = [int(x) for x in line.strip().split(" ")]
        if (report == sorted(report) or report == sorted(report, reverse=True)):
            safe = True
            i = 0
            while ((i < len(report) - 1) and safe):
                if abs(report[i] - report[i+1]) < 1 or abs(report[i] - report[i+1]) > 3:
                    safe = False
                i += 1
            if (safe):
                reportSafe += 1
        line = file.readline()

print(reportSafe)