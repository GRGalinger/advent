with open('day0.txt') as f: s = f.read()

floor = 0
iteration = 0

for letter in s:
    iteration += 1

    if(letter == '('):
        floor += 1
    else:
        floor -= 1

    if(floor == -1):
        break

print(iteration)