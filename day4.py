import re

content = open('content/day4.txt', 'r')
lines = content.readlines()

lineArray = []
lineData = []
pointTotal = cardTotal = 0

for line in lines:
    lineArray.append([1, line.replace('\n', ''), 0])

itr = 0
for line in lineArray:
    lineCount = line[0]
    lineData = line[1]

    while lineCount > 0:
        lineTotal = matchingNumberCount= 0
        winningNumbers = inputNumbers = ''
        
        prefix = re.findall(r'(Card\s+\d+\:\s)', lineData)[0]

        trimmedLineData = lineData.replace(prefix, '')
        dividerIndex = int(trimmedLineData.index('|'))
        winningNumbers = trimmedLineData[:dividerIndex].split()
        inputNumbers = trimmedLineData[dividerIndex + 2:].split()

        for input in inputNumbers:
            if input in winningNumbers:
                matchingNumberCount += 1

        if matchingNumberCount == 1:
            lineTotal = 1
        elif matchingNumberCount > 1:
            lineTotal += pow(2, matchingNumberCount - 1)

        while matchingNumberCount >= 0:
            if matchingNumberCount == 0:
                lineArray[itr + matchingNumberCount][2] = lineTotal
            elif itr + matchingNumberCount < len(lineArray):
                lineArray[itr + matchingNumberCount][0] += 1
            
            matchingNumberCount -= 1

        lineCount -= 1

    itr += 1


for line in lineArray:
    pointTotal += line[2]
    cardTotal += line[0]
    
print('Point total: ' + str(pointTotal))
print('Card total: ' + str(cardTotal))