import sys
import argparse
from hashlib import md5

def part1(data):
    i = 0
    while True:
        s = f"{data}{i}"
        if md5(s.encode('utf-8')).hexdigest()[:5] == "00000":
            print(s)
            return i
        i += 1
    return

def part2(data):
    i = 0
    while True:
        s = f"{data}{i}"
        if md5(s.encode('utf-8')).hexdigest()[:6] == "000000":
            print(s)
            return i
        i += 1
    return

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