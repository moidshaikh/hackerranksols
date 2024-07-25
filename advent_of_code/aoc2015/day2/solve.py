import sys
import argparse

def part1(data):
    return "part1"

def part2(data):
    return "part2"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("part", type=int, help="Which part?")
    parser.add_argument("testing", type=int, help="Is test input?")
    args = parser.parse_args()

    if args.testing:
        inputfile = "input"
    else:
        inputfile = "testinput"

    with open(inputfile, 'r') as f:
        data = f.read().strip()
    print(data)
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