

with open('data/directions.txt') as file:
    lines = file.readlines()
    horizontal = 0
    depth = 0
    aim = 0

    for direction in lines:
        vector = direction.split(' ')
        magnitude = int(vector[1])
        match vector[0]:
            case 'forward':
                horizontal += magnitude
                depth += (aim * magnitude)
            case 'up':
                aim -= magnitude
            case 'down':
                aim += magnitude

print(horizontal * depth)