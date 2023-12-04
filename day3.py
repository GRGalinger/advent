import re
from functools import reduce

content = open('content/day3.txt', 'r')
lines = content.readlines()
total = 0

lineArray = []
symbolArray = ['/', '%', '#', '*', '$', '=', '@', '+', '-', '&']

for line in lines:
    lineArray.append(line)
    
includedArray = [] # to help see whihc numbers are included

# PART 1
itr = 0
for line in lineArray:
    indexesUsed = []
   
    numbers = re.findall(r'(\d+)', line)

    for number in numbers:
        included = False

        #initialize number length
        numLength = len(number)

        regex = '(\D|^)(' + str(number) + ')(\D|$)'

        index = re.search(regex, line).start()
        index2 = re.findall(regex, line)

        if not index2[0][0]:
            index = 0
        else:
            if index + 1 < len(line):
                index += 1

        if index in indexesUsed:
            index = line.rindex(number)

        # CURRENT LINE
        # in the current line, check the index before
        if index > 0:
            beforeIndex = line[index - 1]

            if beforeIndex in symbolArray:
                total += int(number)
                includedArray.append(number)
                indexesUsed.append(index)
                continue

        # in the current line, check the index after
        if index + numLength < len(line):
            afterIndex = line[index + numLength]

            if afterIndex in symbolArray:
                total += int(number)
                includedArray.append(number)
                indexesUsed.append(index)
                continue

        # ABOVE LINE
        #if it is not the first loop, then we can check the row above
        if(itr != 0):
            aboveLine = lineArray[itr - 1]
            
            if index > 0:
                beforeIndex = aboveLine[index - 1]
              
                if beforeIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    indexesUsed.append(index)
                    continue

            if index + numLength < len(line):
                afterIndex = aboveLine[index + numLength]
              
                if afterIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    indexesUsed.append(index)
                    continue

            while numLength > 0:
                numLength -= 1
                inbetweenIndex = aboveLine[index + numLength]

                if inbetweenIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    indexesUsed.append(index)
                    included = True
                    break

        if included:
            continue

        # reset number length       
        numLength = len(number)
        
        # BELOW LINE
        # check row below
        if itr + 1 < len(lineArray):
            belowLine = lineArray[itr + 1] 

            if index > 0:
                beforeIndex = belowLine[index - 1]

                if beforeIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    indexesUsed.append(index)
                    continue
            
            if index + numLength < len(line):
                afterIndex = belowLine[index + numLength]
                
                if afterIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    indexesUsed.append(index)
                    continue
        
            while numLength > 0:
                numLength -= 1
                
                inbetweenIndex = belowLine[index + numLength]
                if inbetweenIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    indexesUsed.append(index)
                    break

        if included:
            continue

    itr += 1

# PART 2
gearRatio = 0
itr = 0
for line in lineArray:
    starIndexes = [i for i in range(len(line)) if line.startswith('*', i)]

    for star in starIndexes:
        adjacentNumbers = 0
        adjacentNumbersArray = []

        # above line
        aboveLineLeftIndex = aboveLineRightIndex = aboveLineCenterIndex = False

        #below line
        belowLineLeftIndex = belowLineRightIndex = belowLineCenterIndex = False

        # check index to the left and right of the star
        if star > 0:
            indexLeft = line[star - 1]
            
            if indexLeft.isdigit():
                adjacentNumbers += 1
                numString = str(indexLeft)

                if line[star - 2].isdigit():
                    numString = str(line[star - 2]) + numString

                    if line[star - 3].isdigit():
                        numString = str(line[star - 3]) + numString

                adjacentNumbersArray.append(int(numString))

        if star + 1 < len(line):
            indexRight = line[star + 1]

            if indexRight.isdigit():
                adjacentNumbers += 1
                numString = str(indexRight)

                if line[star + 2].isdigit():
                    numString = numString + str(line[star + 2])

                    if line[star + 3].isdigit():
                        numString = numString + str(line[star + 3])

                adjacentNumbersArray.append(int(numString))

        # if it's not the first loop, we can check the line above
        if itr > 0:
            lineAbove = lineArray[itr - 1]

            if star > 0:
                indexLeft = lineAbove[star - 1]
                
                if indexLeft.isdigit():
                    adjacentNumbers += 1
                    aboveLineLeftIndex = True
                    numString = str(indexLeft)

                    if lineAbove[star - 2].isdigit():
                        numString = str(lineAbove[star - 2]) + numString

                        if lineAbove[star - 3].isdigit():
                            numString = str(lineAbove[star - 3]) + numString

                    if lineAbove[star].isdigit():
                        numString = numString + str(lineAbove[star])

                        if lineAbove[star + 1].isdigit():
                            numString = numString + str(lineAbove[star + 1])

                            if lineAbove[star + 2].isdigit():
                                numString = numString + str(lineAbove[star + 2])


                    adjacentNumbersArray.append(int(numString))

                    # print('numstring: ' + numString)
                    # print(adjacentNumbersArray)
                    # quit()

            indexAbove = lineAbove[star]
            if indexAbove.isdigit() and aboveLineLeftIndex == False:
                aboveLineCenterIndex = True
                adjacentNumbers += 1
                numString = str(indexAbove)

                if lineAbove[star + 1].isdigit():
                    numString = numString + str(lineAbove[star + 1])
                    
                    if lineAbove[star + 2].isdigit():
                        numString = numString + str(lineAbove[star + 2])

                    
                adjacentNumbersArray.append(int(numString))

            if indexAbove.isdigit():
                aboveLineCenterIndex = True

            if star + 1 < len(line):
                indexRight = lineAbove[star + 1]

                if indexRight.isdigit() and aboveLineCenterIndex == False:
                    aboveLineRightIndex = True
                    adjacentNumbers += 1
                    numString = str(indexRight)

                    if lineAbove[star + 2].isdigit():
                        numString = numString + str(lineAbove[star + 2])
                    
                    if lineAbove[star + 3].isdigit():
                        numString = numString + str(lineAbove[star + 3])

                    adjacentNumbersArray.append(int(numString))

                # print('numstring: ' + numString)
                # print(adjacentNumbersArray)
                # quit()  

        # if it's not the last row, we can check the line below
        if itr + 1 < len(lineArray):
            lineBelow = lineArray[itr + 1]

            # LEFT INDEX
            if star > 0:
                indexLeft = lineBelow[star - 1]
                if indexLeft.isdigit():
                    adjacentNumbers += 1
                    belowLineLeftIndex = True

                    numString = str(indexLeft)

                    if lineBelow[star - 2].isdigit():
                        # print(str(lineBelow[star - 2]))
                        numString = str(lineBelow[star - 2]) + numString
                        # print(numString)

                        if lineBelow[star - 3].isdigit():
                            numString = str(lineBelow[star - 3]) + numString
                            # print(numString)

                    if lineBelow[star].isdigit():
                        numString = numString + str(lineBelow[star])

                        if lineBelow[star + 1].isdigit():
                            numString = numString + str(lineBelow[star + 1])

                            if lineBelow[star + 2].isdigit():
                                numString = numString + str(lineBelow[star + 2])


                    adjacentNumbersArray.append(int(numString))

            # CENTER INDEX
            indexBelow = lineBelow[star]
            if indexBelow.isdigit() and belowLineLeftIndex == False:
                belowLineCenterIndex = True
                adjacentNumbers += 1
                numString = str(indexBelow)

                if lineBelow[star + 1].isdigit():
                    numString = numString + str(lineBelow[star + 1])
                    
                    if lineBelow[star + 2].isdigit():
                        numString = numString + str(lineBelow[star + 2])

                adjacentNumbersArray.append(int(numString))

            if indexBelow.isdigit():
                belowLineCenterIndex = True

            # RIGHT INDEX
            if star + 1 < len(line):
                indexRight = lineBelow[star + 1]
                # print('index right: ' + str(indexRight))
                if indexRight.isdigit() and belowLineCenterIndex == False:
                    belowLineRightIndex = True
                    adjacentNumbers += 1

                    numString = str(indexRight)
                    # print('numstring: ' + str(numString))

                    if lineBelow[star + 2].isdigit():
                        numString = numString + str(lineBelow[star + 2])
                        # print('numstring: ' + str(numString))
                    
                    if lineBelow[star + 3].isdigit():
                        numString = numString + str(lineBelow[star + 3])
                        # print('numstring: ' + str(numString))

                    adjacentNumbersArray.append(int(numString))

        if adjacentNumbers == 2:
            gearRatio += reduce(lambda x, y: x*y, adjacentNumbersArray)
            
    itr += 1
    


print('PART NUMBER SUM: ' + str(total))
print('GEAR RATIO: ' + str(gearRatio))