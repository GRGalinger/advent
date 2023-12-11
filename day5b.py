lines = open('content/day5.txt', 'r').readlines()
lineArray = []
seedsArray = []

for line in lines:
    lineArray.append(line)

inputs = lineArray[0].strip().split(' ')[1:]
seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((int(inputs[i]), int(inputs[i]) + int(inputs[i + 1])))


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

soils = []
fertilizers = []
waters = []
lights = []
temperatures = []
humidities = []
locations = []
 
while len(seeds) > 0:
    s, e = seeds.pop()
    for a, b, c in seedToSoilArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            soils.append((os - b + a, oe - b + a))
            if os > s:
                seeds.append((s, os))
            if e > oe:
                seeds.append((oe, e))
            break
    else:
        soils.append((s, e))
            
while len(soils) > 0:
    s, e = soils.pop()
    for a, b, c in soilToFertilizerArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            fertilizers.append((os - b + a, oe - b + a))
            if os > s:
                soils.append((s, os))
            if e > oe:
                soils.append((oe, e))
            break
    else:
        fertilizers.append((s, e))

while len(fertilizers) > 0:
    s, e = fertilizers.pop()
    for a, b, c in fertilizerToWaterArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            waters.append((os - b + a, oe - b + a))
            if os > s:
                fertilizers.append((s, os))
            if e > oe:
                fertilizers.append((oe, e))
            break
    else:
        waters.append((s, e))

while len(waters) > 0:
    s, e = waters.pop()
    for a, b, c in waterToLightArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            lights.append((os - b + a, oe - b + a))
            if os > s:
                waters.append((s, os))
            if e > oe:
                waters.append((oe, e))
            break
    else:
        lights.append((s, e))

while len(lights) > 0:
    s, e = lights.pop()
    for a, b, c in lightToTemperatureArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            temperatures.append((os - b + a, oe - b + a))
            if os > s:
                lights.append((s, os))
            if e > oe:
                lights.append((oe, e))
            break
    else:
        temperatures.append((s, e))

while len(temperatures) > 0:
    s, e = temperatures.pop()
    for a, b, c in temperatureToHumidityArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            humidities.append((os - b + a, oe - b + a))
            if os > s:
                temperatures.append((s, os))
            if e > oe:
                temperatures.append((oe, e))
            break
    else:
        humidities.append((s, e))

while len(humidities) > 0:
    s, e = humidities.pop()
    for a, b, c in humidityToLocationArray:
        a = int(a)
        b = int(b)
        c = int(c)
    
        os = max(s, b)
        oe = min(e, b + c)
        if os < oe:
            locations.append((os - b + a, oe - b + a))
            if os > s:
                humidities.append((s, os))
            if e > oe:
                humidities.append((oe, e))
            break
    else:
        locations.append((s, e))

print(min(locations)[0])