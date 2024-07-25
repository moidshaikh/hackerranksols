import sys
import argparse

def get_pos(direction, pos):
    if direction == ">":
        return (pos[0]+1, pos[1])
    elif direction == "<":
        return (pos[0]-1, pos[1])
    elif direction == "^":
        return (pos[0], pos[1]+1)
    else:
        return (pos[0], pos[1]-1)

def part1(data):
    pos = (0,0)
    visited = set()
    visited.add(pos)

    for direction in data:
        if direction == ">":
            pos = (pos[0]+1, pos[1])
            visited.add(pos)
        elif direction == "<":
            pos = (pos[0]-1, pos[1])
            visited.add(pos)
        elif direction == "^":
            pos = (pos[0], pos[1]+1)
            visited.add(pos)
        elif direction == "v":
            pos = (pos[0], pos[1]-1)
            visited.add(pos)
        else:
            print("Incorrect Direction in input")
    return len(visited)

def part2(data):
    pos = (0,0)
    visited = set()
    visited.add(pos)
    santa, robo = pos, pos
    for i, direction in enumerate(data):
        if i%2 == 0:
            santa = get_pos(direction, santa)
            visited.add(santa)
        else:
            robo = get_pos(direction, robo)
            visited.add(robo)
    return len(visited)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("part", type=int, help="Which part?")
    parser.add_argument("testing", type=int, help="Is test input?")
    args = parser.parse_args()

    if args.testing:
        inputfile = "testinput"
    else:
        inputfile = "input"

    with open(inputfile, 'r') as f:
        data = f.read().strip()

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