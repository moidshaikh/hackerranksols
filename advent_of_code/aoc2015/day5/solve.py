import sys
import argparse
from collections import Counter
import pandas as pd

def is_nice(s):
    # 3 vovels.
    vc = 0
    double_letter = False
    for i, c in enumerate(s):
        if vc < 4 and c in 'aeuio':
            vc += 1
        if i>1 and s[i] == s[i-1]:
            double_letter = True
    # print(s, double_letter, vc)
    return (double_letter) and (vc>=3) and (not any([x in s for x in ['ab','cd', 'pq', 'xy']]))

# def part1(data):
#     nice_letters = 0
#     for w in data.split():
#         if is_nice(w):
#             # print(f"NICE: {w}")
#             nice_letters += 1
#         else:
#             pass
#             # print(f"not NICE: {w}")
#     return nice_letters

def part1(data):
    words = data.split()
    df = pd.DataFrame({'words':words})
    df['vovel'] = df['words'].str.count(r'[aeiou]')
    df['double'] = df['words'].str.count(r'(\w)\1+')
    df['banned'] = df['words'].apply(lambda y: any([x in y for x in ['ab','cd', 'pq', 'xy']]))
    # df2 = df[(df['vovel']>=3) and (df['double']==True) and (df['banned']!=True)]
    mask = (df['vovel']>=3) & (df['double']>=1) & (df['banned']!=True)
    df2 = df[mask]
    # print(df2.shape)
    return df2.shape[0]

def part2(data):
    words = data.split()
    
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