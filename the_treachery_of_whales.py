
def cost_at_position(crabs, position):
    cost = 0

    for crab in crabs:
        if crab != position:
            steps = abs(crab - position)
            cost += (steps * (1 + steps))/2

    return cost


with open('data/crabs.txt') as file:
    crabs = file.readline().split(',')
    crabs = [int(crab) for crab in crabs]

    fuel_cost = 9999999999

    for i in range(len(crabs)):
        new_cost = cost_at_position(crabs, i)
        if new_cost < fuel_cost: fuel_cost = new_cost

    print(fuel_cost)
