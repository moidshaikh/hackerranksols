import sys
import argparse
from itertools import permutations
from pprint import pprint
def part1(data):
    cities, distmap = parse_data(data)
    distmap.update({key[::-1]:value for key, value in distmap.items()})
    distances = {}
    for route in permutations(cities):
        # print(f"{route=}")
        steps = list(zip(route, route[1:]))
        # print(route, steps)
        t = 0
        for step in steps:
            t += distmap[step]
        distances[route] = t
        # input((route, t))
    # pprint(distances)
    # return distances[min(distances)]
    return min(distances.values())

def part2(data):
    cities, distmap = parse_data(data)
    distmap.update({key[::-1]:value for key, value in distmap.items()})
    distances = {}
    for route in permutations(cities):
        # print(f"{route=}")
        steps = list(zip(route, route[1:]))
        # print(route, steps)
        t = 0
        for step in steps:
            t += distmap[step]
        distances[route] = t
        # input((route, t))
    # pprint(distances)
    # return distances[min(distances)]
    return max(distances.values())


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return content.splitlines()

def parse_data(rdata):
    loc = {}
    cities = set()
    for r in rdata:
        route, dist = r.split(' = ')
        start, end = route.split(' to ')
        if start not in cities:
            cities.add(start)
        if end not in cities:
            cities.add(end)
        loc[(start, end)] = int(dist)
    # print(cities, '\n', loc)
    return cities, loc

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--part", type=int, required=True, help="Which part?")
    parser.add_argument("-t","--test", type=int, help="Is test input?")
    args = parser.parse_args()

    if args.test == 1:
        inputfile = "testinput"
        # print('testing')
    else:
        # print('testing')
        inputfile = "input"

    data = read_file(inputfile)
    # data = parse_data(rdata)

    if args.part == 1:
        res = part1(data)
        print(res)
    elif args.part == 2:
        res = part2(data)
        print(res)
    else:
        print("Incorrect argument")


if __name__ == "__main__":
    main()