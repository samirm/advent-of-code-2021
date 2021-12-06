
with open('data/depths.txt') as file:
    lines = file.readlines()

    firstValue = lines[0]
    lastDepth = int(lines[0]) + int(lines[1]) + int(lines[2])
    increase = 0

    for index, item in enumerate(lines[1:-2]):
        slidingWindow = int(lines[index + 1]) + int(lines[index + 2]) + int(lines[index + 3])
        if slidingWindow > lastDepth: increase += 1
        lastDepth = slidingWindow

    print(increase)
