import re
import numpy as np

# part 1 maxes
maxRed = 12
maxGreen = 13 
maxBlue = 14

content = open('content/day2.txt', 'r')
lines = content.readlines()
total = 0
powerTotal = 0

for line in lines:
    impossible = False
    gameID = re.findall(r'Game\s(\d+)', line)[0]
    redMatches = re.findall(r'(\d+)\s(red)', line)
    blueMatches = re.findall(r'(\d+)\s(blue)', line)
    grennMatches = re.findall(r'(\d+)\s(green)', line)

    highestRedCount = 0
    for match in redMatches:
        if(int(match[0]) > highestRedCount):
            highestRedCount = int(match[0])

        if(int(match[0]) > maxRed):
            impossible = True

    highestGreenCount = 0
    for match in grennMatches:
        if(int(match[0]) > highestGreenCount):
            highestGreenCount = int(match[0])

        if(int(match[0]) > maxGreen):
            impossible = True

    highestBlueCount = 0
    for match in blueMatches:
        if(int(match[0]) > highestBlueCount):
            highestBlueCount = int(match[0])

        if(int(match[0]) > maxBlue):
            impossible = True

    # part 1 calculation
    if(impossible == False):
        total += int(gameID)

    # part 2 calculation
    powerTotal += (highestRedCount * highestGreenCount * highestBlueCount)

print(powerTotal)