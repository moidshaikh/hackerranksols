import sys
import argparse
import pandas as pd
import numpy as np


def part1(data):
    df = pd.DataFrame(-1, index=np.arange(1000), columns=np.arange(1000))
    for instr in data:
        x1,y1 = instr['from']
        x2,y2 = instr['to']
        if instr['instruction'] == "on":
            df.loc[x1:x2,y1:y2] = 1
        elif instr['instruction'] == "off":
            df.loc[x1:x2,y1:y2] = -1
        else:
            df.loc[x1:x2,y1:y2] *= -1 
    df.replace(-1, 0, inplace=True)
    return df.sum().sum()

def part2(data):
    df = pd.DataFrame(0, index=np.arange(1000), columns=np.arange(1000))
    for instr in data:
        x1,y1 = instr['from']
        x2,y2 = instr['to']
        if instr['instruction'] == "on":
            df.loc[x1:x2,y1:y2] += 1
        elif instr['instruction'] == "off":
            df.loc[x1:x2,y1:y2] -= 1
            df.clip(lower=0, inplace=True)
        else:
            df.loc[x1:x2,y1:y2] += 2
    return df.sum().sum()

def read_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return content.splitlines()

def parse_content(filecontent):
    instructions = []
    for line in filecontent:
        i = {}
        linecontent = line.split() # ['turn', 'on', '579,693', 'through', '650,978']
        if len(linecontent) == 4:
            i['instruction'] = "flip"
            f, t = linecontent[1], linecontent[-1]
        else:
            f, t = linecontent[2], linecontent[-1]
            if linecontent[1] == "on":
                i['instruction'] = "on"
            else:
                i['instruction'] = "off"
        i['from'] = tuple(map(int, f.split(',')))
        i['to'] = tuple(map(int, t.split(',')))
        instructions.append(i)
    return instructions

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

    filecontent = read_file(inputfile)
    data = parse_content(filecontent) 
    # data = [{'from': (579, 693), 'instruction': 'on', 'to': (650, 978)}, ...]

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