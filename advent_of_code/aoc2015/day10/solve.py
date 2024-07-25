import sys
import argparse
from hashlib import md5

def look_and_say(s, n=40):
    for i in range(n):
        s = generate_next(s)
        print(f"Iteration: {i}\tNumber: {s}")
    return len(s)

def generate_next(s):
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result += str(count) + s[i-1]
            count = 1
    result += str(count) + s[-1]
    return result

def part1(data):
    res = look_and_say(data)
    print(f'Length of result for {data} after 40 iterations: {res}')
    return res

def part2(data):
    return


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