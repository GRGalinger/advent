import re
from operator import itemgetter
import numpy as np


content = open('content/day5.txt', 'r')
lines = content.readlines()


lineArray = []
seedsArray = []

for line in lines:
    lineArray.append(line)


seedsArray = lineArray[0].strip().split(' ')[1:]
# print(seedsArray)

seedToSoilStart = seedToSoilEnd = 0
soilToFertilizerStart = soilToFertilizerEnd = 0
fertilizerToWaterStart = fertilizerToWaterEnd = 0
waterToLightStart = waterToLightEnd = 0
lightToTemperatureStart = lightToTemperatureEnd = 0
temperatureToHumidityStart = temperatureToHumidityEnd = 0
humidityToLocationStart = 0
humidityToLocationEnd = len(lineArray) - 1

seedToSoilArray = []
soilToFertilizerArray = []
fertilizerToWaterArray = []
waterToLightArray = []
lightToTemperatureArray = []
temperatureToHumidityArray = []
humidityToLocationArray = []

itr = 0
for line in lineArray:
    if line.strip() == 'seed-to-soil map:':
        seedToSoilStart = itr + 1
        
    if line.strip() == 'soil-to-fertilizer map:':
        seedToSoilEnd = itr - 2
        soilToFertilizerStart = itr + 1

    if line.strip() == 'fertilizer-to-water map:':
        soilToFertilizerEnd = itr - 2
        fertilizerToWaterStart = itr + 1

    if line.strip() == 'water-to-light map:':
        fertilizerToWaterEnd = itr - 2
        waterToLightStart = itr + 1

    if line.strip() == 'light-to-temperature map:':
        waterToLightEnd = itr - 2
        lightToTemperatureStart = itr + 1

    if line.strip() == 'temperature-to-humidity map:':
        lightToTemperatureEnd = itr - 2
        temperatureToHumidityStart = itr + 1

    if line.strip() == 'humidity-to-location map:':
        temperatureToHumidityEnd = itr - 2
        humidityToLocationStart = itr + 1

    itr += 1


for x in range(seedToSoilStart, seedToSoilEnd + 1):
    seedToSoilArray.append(lineArray[x].strip().split(' '))

for x in range(soilToFertilizerStart, soilToFertilizerEnd + 1):
    soilToFertilizerArray.append(lineArray[x].strip().split(' '))

for x in range(fertilizerToWaterStart, fertilizerToWaterEnd + 1):
    fertilizerToWaterArray.append(lineArray[x].strip().split(' '))

for x in range(waterToLightStart, waterToLightEnd + 1):
    waterToLightArray.append(lineArray[x].strip().split(' '))

for x in range(lightToTemperatureStart, lightToTemperatureEnd + 1):
    lightToTemperatureArray.append(lineArray[x].strip().split(' '))

for x in range(temperatureToHumidityStart, temperatureToHumidityEnd + 1):
    temperatureToHumidityArray.append(lineArray[x].strip().split(' '))

for x in range(humidityToLocationStart, humidityToLocationEnd + 1):
    humidityToLocationArray.append(lineArray[x].strip().split(' '))


seedToSoilConversion = []
soilToFertilizerConversion = []
fertilizerToWaterConversion = []
waterToLightConversion = []
lightToTemperatureConversion = []
temperatureToHumidityConversion = []
humidityToLocationConversion = []

for line in seedToSoilArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        seedToSoilConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1


for line in soilToFertilizerArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        soilToFertilizerConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1

for line in fertilizerToWaterArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        fertilizerToWaterConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1

for line in waterToLightArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        waterToLightConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1

for line in lightToTemperatureArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        lightToTemperatureConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1

for line in temperatureToHumidityArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        temperatureToHumidityConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1

for line in humidityToLocationArray:
    destinationStart = int(line[0])
    sourceStart = int(line[1])
    rangeLength = int(line[2])
    
    itr = 0
    while itr < rangeLength:
        humidityToLocationConversion.append([str(sourceStart + itr), str(destinationStart + itr)])
        itr += 1


soilsArray = []
fertilizersArray = []
watersArray = []
lightsArray = []
temperaturesArray = []
humiditiesArray = []
locationsArray = []

for seed in seedsArray:
    seedAccountedFor = False

    # find line value in seedToSoilConversion
    for conversionLine in seedToSoilConversion:
        if conversionLine[0] == seed:
            soilsArray.append(conversionLine[1])
            seedAccountedFor = True
            continue
    
    if seedAccountedFor ==  False:
        soilsArray.append(seed)
print(soilsArray)

for soil in soilsArray:
    soilAccountedFor = False

    # find line value in soilToFertilizerConversion
    for conversionLine in soilToFertilizerConversion:
        if conversionLine[0] == soil:
            fertilizersArray.append(conversionLine[1])
            soilAccountedFor = True
            continue
    
    if soilAccountedFor ==  False:
        fertilizersArray.append(soil)
print(fertilizersArray)

for fertilizer in fertilizersArray:
    fertilizerAccountedFor = False

    # find line value in fertilizerToWaterConversion
    for conversionLine in fertilizerToWaterConversion:
        if conversionLine[0] == fertilizer:
            watersArray.append(conversionLine[1])
            fertilizerAccountedFor = True
            continue
    
    if fertilizerAccountedFor ==  False:
        watersArray.append(fertilizer)
print(watersArray)

for water in watersArray:
    waterAccountedFor = False

    # find line value in waterToLightConversion
    for conversionLine in waterToLightConversion:
        if conversionLine[0] == water:
            lightsArray.append(conversionLine[1])
            waterAccountedFor = True
            continue
    
    if waterAccountedFor ==  False:
        lightsArray.append(water)
print(lightsArray)

for light in lightsArray:
    lightAccountedFor = False

    # find line value in waterToLightConversion
    for conversionLine in lightToTemperatureConversion:
        if conversionLine[0] == light:
            temperaturesArray.append(conversionLine[1])
            lightAccountedFor = True
            continue
    
    if lightAccountedFor ==  False:
        temperaturesArray.append(light)
print(temperaturesArray)

for temperature in temperaturesArray:
    temperatureAccountedFor = False

    # find line value in waterToLightConversion
    for conversionLine in temperatureToHumidityConversion:
        if conversionLine[0] == temperature:
            humiditiesArray.append(conversionLine[1])
            temperatureAccountedFor = True
            continue
    
    if temperatureAccountedFor ==  False:
        humiditiesArray.append(temperature)
print(humiditiesArray)

for humidity in humiditiesArray:
    humidityAccountedFor = False

    # find line value in waterToLightConversion
    for conversionLine in humidityToLocationConversion:
        if conversionLine[0] == humidity:
            locationsArray.append(conversionLine[1])
            humidityAccountedFor = True
            continue
    
    if humidityAccountedFor ==  False:
        locationsArray.append(humidity)
print(locationsArray)

# quit()


# DESTINATION - SOURCE -LENGTH

# seed-to-soil map:
# 50 98 2
# 52 50 48

minimumLocation = locationsArray[0]
for location in locationsArray:
    if location < minimumLocation:
        minimumLocation = location

print(minimumLocation)