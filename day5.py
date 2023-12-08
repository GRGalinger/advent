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
rangedSeedsArray = []

itr = 0
for seed in seedsArray:
    if itr % 2 == 0:
        seedStart = int(seedsArray[itr])
        seedRange = int(seedsArray[itr + 1])
        seedEnd = seedStart + seedRange
        seedRange = list(set(range(seedStart, seedEnd)))
        rangedSeedsArray += seedRange
        
    itr += 1


rangedSeedsArray = list(set(rangedSeedsArray))

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



# for line in fertilizerToWaterArray:
#     print(line)


# quit()


soilsArray = []
fertilizersArray = []
watersArray = []
lightsArray = []
temperaturesArray = []
humiditiesArray = []
locationsArray = []

for seed in rangedSeedsArray:
    seedAccountedFor = False

    for line in seedToSoilArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == seed:
            soilsArray.append(int(destinationStart))
            seedAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(seed) and int(sourceStart) <= int(seed):
            soilsArray.append(int(seed) + (abs(int(destinationStart) - int(sourceStart))))         
            seedAccountedFor = True
            break

    if seedAccountedFor == False:
        soilsArray.append(seed)
        


# for soil in soilsArray:
#     print('soil value: ' + str(soil))

# quit()

for soil in soilsArray:
    soilAccountedFor = False

    for line in soilToFertilizerArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == soil:
            fertilizersArray.append(int(destinationStart))
            soilAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(soil) and int(sourceStart) <= int(soil):
            fertilizersArray.append(int(soil) + (int(destinationStart) - int(sourceStart)))       
            soilAccountedFor = True
            break

    if soilAccountedFor == False:
        fertilizersArray.append(soil)


# for line in fertilizersArray:
#     print('fertilizer: ' + str(line))

# quit()

for fertilizer in fertilizersArray:
    fertilizerAccountedFor = False

    # print('fertilizer: ' + str(fertilizer))

    for line in fertilizerToWaterArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == fertilizer:
            watersArray.append(int(destinationStart))
            fertilizerAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(fertilizer) and int(sourceStart) <= int(fertilizer):
            watersArray.append(int(fertilizer) + (int(destinationStart) - int(sourceStart)))         
            fertilizerAccountedFor = True
            break

    if fertilizerAccountedFor == False:
        watersArray.append(fertilizer)
        continue






for water in watersArray:
    waterAccountedFor = False

    for line in waterToLightArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == water:
            lightsArray.append(int(destinationStart))
            waterAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(water) and int(sourceStart) <= int(water):
            lightsArray.append(int(water) + (int(destinationStart) - int(sourceStart)))         
            waterAccountedFor = True
            break

    if waterAccountedFor == False:
        lightsArray.append(water)
        continue



# for line in lightsArray:
#     print(line)


for light in lightsArray:
    lightAccountedFor = False

    for line in lightToTemperatureArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == light:
            temperaturesArray.append(int(destinationStart))
            lightAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(light) and int(sourceStart) <= int(light):
            temperaturesArray.append(int(light) + (int(destinationStart) - int(sourceStart)))         
            lightAccountedFor = True
            break

    if lightAccountedFor == False:
        temperaturesArray.append(light)
        continue



# for line in temperaturesArray:
#     print(line)


for temperature in temperaturesArray:
    temperatureAccountedFor = False

    for line in temperatureToHumidityArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == temperature:
            humiditiesArray.append(int(destinationStart))
            temperatureAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(temperature) and int(sourceStart) <= int(temperature):
            humiditiesArray.append(int(temperature) + (int(destinationStart) - int(sourceStart)))         
            temperatureAccountedFor = True
            break

    if temperatureAccountedFor == False:
        humiditiesArray.append(temperature)
        continue


# for line in humiditiesArray:
#     print(line)

# quit()

for humidity in humiditiesArray:
    humidityAccountedFor = False

    for line in humidityToLocationArray:
        destinationStart = int(line[0])
        sourceStart = int(line[1])
        rangeLength = int(line[2])

        if sourceStart == humidity:
            locationsArray.append(int(destinationStart))
            humidityAccountedFor = True
            break

        elif int(sourceStart + rangeLength) >= int(humidity) and int(sourceStart) <= int(humidity):
            locationsArray.append(int(humidity) + (int(destinationStart) - int(sourceStart)))         
            humidityAccountedFor = True
            break

    if humidityAccountedFor == False:
        locationsArray.append(humidity)
        continue



print(rangedSeedsArray)
print(soilsArray)
print(fertilizersArray)
print(watersArray)
print(lightsArray)
print(temperaturesArray)
print(humiditiesArray)
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