import time


class Point:
    count = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


def increment_if_existing(x, y, all_points):
    for this_point in all_points:
        if this_point.x == x and this_point.y == y:
            this_point.count += 1
            return True
    return False


with open('data/vents.txt') as file:
    lines = file.readlines()
    all_points = []

    start = time.time()
    for line in lines:
        coords = line.split(' -> ')

        first_pair = coords[0].split(',')
        second_pair = coords[1].split(',')

        if int(first_pair[0]) == int(second_pair[0]):
            ys = [int(first_pair[1]), int(second_pair[1])]
            ys.sort()

            for i in range(ys[1] - ys[0] + 1):
                x = int(first_pair[0])
                y = ys[0] + i

                if not increment_if_existing(x, y, all_points):
                    all_points.append(Point(x, y))
        elif int(first_pair[1]) == int(second_pair[1]):
            xs = [int(first_pair[0]), int(second_pair[0])]
            xs.sort()

            for i in range(xs[1] - xs[0] + 1):
                y = int(first_pair[1])
                x = xs[0] + i

                if not increment_if_existing(x, y, all_points):
                    all_points.append(Point(x, y))
        else:
            x1 = int(first_pair[0])
            x2 = int(second_pair[0])
            y1 = int(first_pair[1])
            y2 = int(second_pair[1])
            if x2 > x1: xys = [(x1, y1), (x2, y2)]
            else: xys = [(x2, y2), (x1, y1)]

            if xys[1][0] > xys[0][0] and xys[1][1] < xys[0][1]:
                for i in range(xys[1][0] - xys[0][0] + 1):
                    x = xys[0][0] + i
                    y = xys[0][1] - i

                    if not increment_if_existing(x, y, all_points):
                        all_points.append(Point(x, y))

            elif xys[1][0] > xys[0][0] and xys[1][1] > xys[0][1]:
                for i in range(xys[1][0] - xys[0][0] + 1):
                    x = xys[0][0] + i
                    y = xys[0][1] + i

                    if not increment_if_existing(x, y, all_points):
                        all_points.append(Point(x, y))

    stop = time.time()
    print('total seconds: ' + str(stop - start))

    count = 0
    for point in all_points:
        if point.count >= 2:
            count += 1

    print(count)
