lines = open('content/day5.txt', 'r').readlines()
lineArray = []
seedsArray = []

for line in lines:
    lineArray.append(line)

seedsArray = lineArray[0].strip().split(' ')[1:]

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

for seed in seedsArray:
    seed = int(seed)

    for a, b, c in seedToSoilArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= seed < b + c:
            soils.append(seed - b + a)
            break
    else:
        soils.append(seed)

for soil in soils:
    soil = int(soil)

    for a, b, c in soilToFertilizerArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= soil < b + c:
            fertilizers.append(soil - b + a)
            break
    else:
        fertilizers.append(soil)

for fertilizer in fertilizers:
    fertilizer = int(fertilizer)

    for a, b, c in fertilizerToWaterArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= fertilizer < b + c:
            waters.append(fertilizer - b + a)
            break
    else:
        waters.append(fertilizer)

for water in waters:
    water = int(water)

    for a, b, c in waterToLightArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= water < b + c:
            lights.append(water - b + a)
            break
    else:
        lights.append(water)

for light in lights:
    light = int(light)

    for a, b, c in lightToTemperatureArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= light < b + c:
            temperatures.append(light - b + a)
            break
    else:
        temperatures.append(light)

for temperature in temperatures:
    temperature = int(temperature)

    for a, b, c in temperatureToHumidityArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= temperature < b + c:
            humidities.append(temperature - b + a)
            break
    else:
        humidities.append(temperature)

for humidity in humidities:
    humidity = int(humidity)

    for a, b, c in humidityToLocationArray:
        a = int(a)
        b = int(b)
        c = int(c)
        
        if b <= humidity < b + c:
            locations.append(humidity - b + a)
            break
    else:
        locations.append(humidity)

print(min(locations))
quit()