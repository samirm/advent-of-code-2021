
o2, co2 = [], []


def test(o2, c_o2, digit):
    nu_o2, nu_c_o2 = [], []
    if len(o2) == 1 and len(c_o2) == 1:
        return o2, c_o2
    for this_line in (o2 + c_o2):
        (nu_o2 if digit == '1' else nu_c_o2).append(this_line)
    o2 = nu_o2


def get_msd(new_numbers, index):
    count = 0
    for new_number in new_numbers:
        if new_number[index + 1] == '1': count += 1
    if count >= (len(new_numbers) / 2): return '1'
    else: return '0'


with open('data/diagnostic.txt') as file:
    lines = file.readlines()
    binary_counter = [0 for x in range(len(lines[0]) - 1)]

    for line in lines:
        for index, item in enumerate(line):
            if item == '1': binary_counter[index] += 1

    g_binary = ''
    e_binary = ''
    for count in binary_counter:
        if count >= (len(lines) / 2):
            g_binary += '1'
            e_binary += '0'
        else:
            g_binary += '0'
            e_binary += '1'

    gamma = int(g_binary, 2)
    epsilon = int(e_binary, 2)

    print(gamma * epsilon)

    oxygen_numbers = lines
    most_common_digit = g_binary[0]

    for index in range(len(binary_counter)):
        new_numbers = []

        for number in oxygen_numbers:
            if number[index] == most_common_digit:
                new_numbers.append(number)

        most_common_digit = get_msd(new_numbers, index)
        oxygen_numbers = new_numbers

    o2_rating = int(oxygen_numbers[0], 2)
    print(o2_rating)

    co2_numbers = lines
    most_common_digit = g_binary[0]

    for index in range(len(binary_counter)):
        if (len(co2_numbers) == 1): break
        new_numbers = []

        for number in co2_numbers:
            if number[index] != most_common_digit:
                new_numbers.append(number)

        most_common_digit = get_msd(new_numbers, index)
        co2_numbers = new_numbers

    c02_rating = int(co2_numbers[0], 2)
    print(c02_rating)
    print(o2_rating * c02_rating)
