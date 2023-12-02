import re
import numpy as np

content = open('content/day1.txt', 'r')
lines = content.readlines()
calibrationValue = 0

def findStringIntegers(line):
    indexArray = []
    onesArray = [m.start() for m in re.finditer('one', line)]
    twosArray = [m.start() for m in re.finditer('two', line)]
    threesArray = [m.start() for m in re.finditer('three', line)]
    foursArray = [m.start() for m in re.finditer('four', line)]
    fivesArray = [m.start() for m in re.finditer('five', line)]
    sixesArray = [m.start() for m in re.finditer('six', line)]
    sevensArray = [m.start() for m in re.finditer('seven', line)]
    eightsArray = [m.start() for m in re.finditer('eight', line)]
    ninesArray = [m.start() for m in re.finditer('nine', line)]

    for ones in onesArray:
        indexArray.append([ones, 1])

    for twos in twosArray:
        indexArray.append([twos, 2])

    for threes in threesArray:
        indexArray.append([threes, 3])

    for fours in foursArray:
        indexArray.append([fours, 4])

    for fives in fivesArray:
        indexArray.append([fives, 5])

    for sixes in sixesArray:
        indexArray.append([sixes, 6])

    for sevens in sevensArray:
        indexArray.append([sevens, 7])

    for eights in eightsArray:
        indexArray.append([eights, 8])

    for nines in ninesArray:
        indexArray.append([nines, 9])

    if(len(indexArray) == 0):
        return False
  
    if(len(indexArray) == 1):
        return indexArray
    
    lowestIndex = 0
    highestIndex = 0
    lowestValue = 0
    highestValue = 0
    overWritten = False

    for i in indexArray:
        if(i[0] < lowestIndex):
            lowestIndex = i[0]
        elif(lowestIndex == 0 and overWritten == False):
            lowestIndex = i[0]
            overWritten = True

        if(i[0] > highestIndex):
            highestIndex = i[0]
        
    for i in indexArray:
        if(i[0] == lowestIndex):
            lowestValue = i[1]

        if(i[0] == highestIndex):
            highestValue = i[1]

    final = []
    final.append([lowestIndex, lowestValue])
    final.append([highestIndex, highestValue])

    return final

for line in lines:
    lowestValue = ''
    highestValue = ''

    lowestIndex = 0
    highestIndex = 0

    # find first integer occurance
    for letter in line:
        if(letter.isdigit()):
            lowestValue = letter
            lowestIndex = line.index(lowestValue)
            break

    lineReverse = line[::-1]

    # find last integer occurance
    for letter in lineReverse:
        if(letter.isdigit()):
            highestValue = letter
            highestIndex = line.rindex(highestValue)
            break

    # add occurances to array - only add last occurance if the index is differeant than the first
    integerOccurances = []
    integerOccurances.append([lowestIndex, int(lowestValue)])
    if(lowestIndex != highestIndex):
        integerOccurances.append([highestIndex, int(highestValue)])

    # find occurances of string integers - combine with
    stringOccurances = findStringIntegers(line)
    if(stringOccurances):
        allOccurances = np.concatenate((integerOccurances, stringOccurances), axis = 0)
    else:
        allOccurances = integerOccurances

    lowestIndex = 0
    highestIndex = 0
    lowestValue = 0
    highestValue = 0

    # evaluate lowest index:value pair and highest index:value pair
    itr = 0
    for index in allOccurances:
        if(index[0] < lowestIndex):
            lowestIndex = index[0]
            lowestValue = index[1]
        elif(lowestIndex == 0 and itr == 0):
            lowestIndex = index[0]
            lowestValue = index[1]
            highestValue = index[1]
    
        if(index[0] > highestIndex):
            highestIndex = index[0]
            highestValue = index[1]

        itr += 1
    
    # concatentate values, convert to integer, add to running sum
    lineSum = int(str(lowestValue) + str(highestValue)) 
    calibrationValue += lineSum
   
print(calibrationValue)