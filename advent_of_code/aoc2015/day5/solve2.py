import sys
import argparse
import re

vowel_re = re.compile(r"[aeiou]")
dup_re = re.compile(r"(.)\1")
exclude_re = re.compile(r"(ab|cd|pq|xy)")
repeat_re = re.compile(r"(.).\1")
dup_pair_re = re.compile(r"(..).*\1")

def is_nice(word):
    if exclude_re.search(word):
        return False
    vowel_count = len(vowel_re.findall(word))
    dup = dup_re.search(word)
    return (vowel_count >= 3 and dup is not None)

def is_nice2(word):
    if repeat_re.search(word) is None:
        return False
    return dup_pair_re.search(word) is not None


def part1(data):
    words = data.split()
    res = 0
    nicewords1 = list(map(is_nice, words))
    print(nicewords1)
    # for word in words:
    #     if is_nice(word):
    #         res += 1
    return len(nicewords1)

def part2(data):
    words = data.split()
    res = 0
    print(len(words), words)
    for word in words:
        print(f"checking {word}")
        if is_nice2(word):
            print("nice word2")
            # print(word, end=" ")
            res += 1
    return res

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