import re


def find_nth(haystack: str, needle: str, n: int) -> int:
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start


content = open('content/day3.txt', 'r')
lines = content.readlines()
total = 0

lineArray = []
symbolArray = ['/', '%', '#', '*', '$', '=', '@', '+', '-', '&']

for line in lines:
    lineArray.append(line)
    

# test = ['951', '193', '562', '971', '754', '562', '262', '668', '781', '621', '115', '249', '470', '227', '57', '769', '839', '968', '876', '491', '807', '297', '305', '883', '470', '505', '245', '682', '415', '982', '180', '205', '135', '286', '418', '362', '444', '815', '722', '336', '37', '283', '329', '433', '153', '435', '108', '814']
# testTotal = 0
# for num in test:
#     testTotal += int(num)

# print(testTotal)

# 489
# 152
# 180
# 147
# 239
# 186
# 48
# 681
# 935
# 512
# 874
# 540
# 249
# 957
# 857
# 89
# 97

includedArray = []

itr = 0
for line in lineArray:
    indexesUsed = []
   
    numbers = re.findall(r'(\d+)', line)
   
    # print(numbers)
    for number in numbers:
        included = False

        # if number != '272':
        #     continue
        # else:
        #     print('num: ' + number)
        
        #initialize number length
        numLength = len(number)

        # index = line.index(number)

        regex = '(\D|^)(' + str(number) + ')(\D|$)'
        # print(regex)
        index = re.search(regex, line).start()
        if index != 0 and index + 1 < len(line):
            index += 1

        # print(index)
        

        # if index != None:
        #     index += 1
        # else:
        #     index = line.index(number)


        
        # print(testing)
        # print(line[testing])
        # # for test in testing:
        # #     print('test: ' + test)

        # quit()


        # if index in indexesUsed:
        #     index = line.rindex(number)
       
        
        # indexesUsed.append(index)
        

        # we have a number at index 0 with length of 3
        # this means we need to check for symbols in:
            # the row above at indexes: index - 1, index through index + length
            # current row at indexes: index - 1, index + numLength
            # row below at indexes: index - 1, index through index + length


        # in the current line, check the index before
        if index > 0:
            beforeIndex = line[index - 1]

            if beforeIndex in symbolArray:
                total += int(number)
                includedArray.append(number)
                continue

        # in the current line, check the index after
        if index + numLength < len(line):
            afterIndex = line[index + numLength]

            if afterIndex in symbolArray:
                total += int(number)
                includedArray.append(number)
                continue

    
        #if it is not the first loop, then we can check the row above
        if(itr != 0):
            aboveLine = lineArray[itr - 1]
            
            if index > 0:
                beforeIndex = aboveLine[index - 1]
                print('before: ' + beforeIndex)

                if beforeIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    continue

            if index + numLength < len(line):
                afterIndex = aboveLine[index + numLength]
                print('after: ' + afterIndex)
            
                if afterIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    continue

            while numLength > 0:
                numLength -= 1
                inbetweenIndex = aboveLine[index + numLength]

                if inbetweenIndex in symbolArray:
                    print('between: ' + inbetweenIndex)

                    total += int(number)
                    includedArray.append(number)
                    included = True
                    break

        if included:
            continue

        # reset number length       
        numLength = len(number)
        
        # check row below
        if itr + 1 < len(lineArray):
            belowLine = lineArray[itr + 1] 

            if index > 0:
                beforeIndex = belowLine[index - 1]

                if beforeIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    continue

            if index + numLength < len(line):
                afterIndex = belowLine[index + numLength]
                
                if afterIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    continue
        
            while numLength > 0:
                numLength -= 1
                
                inbetweenIndex = belowLine[index + numLength]

                if inbetweenIndex in symbolArray:
                    total += int(number)
                    includedArray.append(number)
                    break

            if included:
                continue


    # print(includedArray)
    # quit()
    itr += 1

       

       

print('\n')
print(includedArray)
print(total)