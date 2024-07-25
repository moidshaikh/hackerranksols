import sys
import argparse
from hashlib import md5
import ast 

def part1(data):
    # s = [len(x) for x in data]
    # c = [len(eval(x)) for x in data]
    # print(s,c)
    # return sum(s) - sum(c)
    total_length = 0
    for line in data:
        total_length += len(line)
        total_length -= len(ast.literal_eval(line))
    print(total_length)
    return total_length

def part2(data):
    extras = 0
    for line in data:
        #Adding quotes back onto the line
        extras +=2
        extras += sum(map(line.count, ['"', '\\']))
    print(extras)
    return extras


def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return content.splitlines()

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