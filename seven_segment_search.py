
with open('data/signal_patterns.txt') as file:
    lines = file.readlines()
    count = 0
    total = 0
    number_to_signal_map = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}

    for line in lines:
        signals = line.split('|')
        input_digits = signals[0].strip().split(' ')
        output_digits = signals[1].strip().split(' ')
        # all_digits = input_digits + output_digits

        # print(output_digits)
        # for digit in output_digits:
        #     if len(digit) == 2 or len(digit) == 4 or len(digit) == 3 or len(digit) == 7:
        #         count += 1

        for digit in input_digits.copy():
            if len(digit) == 2: # 1
                number_to_signal_map[1] = set(digit)
                input_digits.remove(digit)
            elif len(digit) == 3: # 7
                number_to_signal_map[7] = set(digit)
                input_digits.remove(digit)
            elif len(digit) == 4: # 4
                number_to_signal_map[4] = set(digit)
                input_digits.remove(digit)
            elif len(digit) == 7:
                number_to_signal_map[8] = set(digit)
                input_digits.remove(digit)

        segment_map = {}
        segment_map[1] = (number_to_signal_map[7] - number_to_signal_map[1]).pop()

        guess_list = []
        for digit in input_digits.copy():
            if len(set(digit) & number_to_signal_map[1]) != 1: continue
            else: # 2, 5 or 6
                if len(digit) == 6:
                    number_to_signal_map[6] = set(digit)
                    input_digits.remove(digit)
                else: guess_list.append(digit) # 2 and 5

        segment_map[6] = (number_to_signal_map[6] & number_to_signal_map[1]).pop()
        segment_map[3] = (number_to_signal_map[1] - set(segment_map[6])).pop()

        for digit in guess_list:
            if digit.__contains__(segment_map[3]):
                number_to_signal_map[2] = set(digit)
                input_digits.remove(digit)
            else:
                number_to_signal_map[5] = set(digit)
                input_digits.remove(digit)

        for digit in input_digits.copy():
            if len(digit) == 5:
                number_to_signal_map[3] = set(digit)
                input_digits.remove(digit)

        leftovers = number_to_signal_map[4] - number_to_signal_map[1]
        number_to_signal_map[9] = number_to_signal_map[3] | set(leftovers)

        for digit in input_digits.copy():
            if set(digit) == number_to_signal_map[9]:
                input_digits.remove(digit)
            else:
                number_to_signal_map[0] = set(digit)
                input_digits.remove(digit)

        string_rep = ''
        for digit in output_digits:
            for key, value in number_to_signal_map.items():
                if set(digit) == value:
                    string_rep += str(key)
                    break

        total += int(string_rep)
        # print(total)
    print(total)
