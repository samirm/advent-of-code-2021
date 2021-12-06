
with open('data/depths.txt') as file:
    lines = file.readlines()

    first_value = lines[0]
    last_depth = int(lines[0]) + int(lines[1]) + int(lines[2])
    increase = 0

    for index, item in enumerate(lines[1:-2]):
        sliding_window = int(lines[index + 1]) + int(lines[index + 2]) + int(lines[index + 3])
        if sliding_window > last_depth: increase += 1
        last_depth = sliding_window

    print(increase)
