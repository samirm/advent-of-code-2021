import copy


class Fish:
    freq = 0

    def __init__(self, timer):
        self.timer = timer

    def __str__(self):
        return 'Fish: ' + str(self.timer)


class Fish2:
    def __init__(self, map):
        self.map = map


def get_frequency(all_fish):
    freq = {}

    for fish in all_fish:
        if fish.timer in freq:
            freq[fish.timer] += 1
        else:
            freq[fish.timer] = 1

    return freq


def simulate(map):
    fish_map = copy.deepcopy(map)

    for age, count in map.items():
        for i in range(count):
            if age == 0:
                fish_map[age] -= 1
                fish_map[6] += 1
                fish_map[8] += 1
            else:
                fish_map[age] -= 1
                fish_map[age - 1] += 1

    return fish_map

with open('data/fish.txt') as file:
    initial_population = file.readline().split(',')
    all_fish = []
    fish_map = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for fish in initial_population:
        fish_age = int(fish)
        if fish_age in fish_map:
            fish_map[fish_age] += 1

    # third approach
    for day in range(256):
        fish_map = simulate(fish_map)

    for key, value in fish_map.items():
        print("% d : % d" % (key, value))

    total = 0
    for pop in fish_map.values():
        total += pop

    print(total)

    # first approach
    # for day in range(18):
    #     # print(*all_fish)
    #     for fish in fish_to_test:
    #         if fish.timer == 0:
    #             fish.timer = 6
    #             all_fish.append(Fish(9))
    #         else:
    #             fish.timer -= 1
    # print(len(all_fish))

    # second approach
    # fish_to_test = []
    # histogram = get_frequency(all_fish)
    # for key, value in histogram.items():
    #     print("% d : % d" % (key, value))
    #     f = Fish(key)
    #     f.freq = value
    #     fish_to_test.append(f)
    #
    # local_pool = []
    # total = 0
    # for fish in fish_to_test:
    #     local_pool.append(fish)
    #     for day in range(256):
    #         # print(*local_pool)
    #         for local_fish in local_pool:
    #             if local_fish.timer == 0:
    #                 local_fish.timer = 6
    #                 local_pool.append(Fish(9))
    #             else:
    #                 local_fish.timer -= 1
    #     total += len(local_pool) * fish.freq
    #     local_pool = []
    #
    # print(total)
