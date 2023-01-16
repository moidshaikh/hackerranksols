import sys
import argparse

def parse_data(data):
    wires = {}
    for line in data:
        wire = line.rstrip().split(" -> ")
        wires[wire[-1]] = wire[0].split()
    return {key: val for key, val in sorted(wires.items(), key = lambda ele: ele[0])}


def part1(data):
    # data = {'x': ['123'], 'y': ['456'], 'd': ['x', 'AND', 'y'], 'e': ['x', 'OR', 'y'], 'f': ['x', 'LSHIFT', '2'], 'g': ['y', 'RSHIFT', '2'], 'h': ['NOT', 'x'], 'i': ['NOT', 'y']}
    gates = {}
    for k in sorted(data, key=lambda k: len(data[k]), reverse=False):
        v = data[k]
        print(v)
        if len(v) == 1 and v[0].isnumeric():
            gates[k] = int(v[0])
            input(gates)
        elif "AND" in v:
            op1, op2 = v[0], v[-1]
            if op1.isalpha():
                op1 = gates[op1]
            if op2.isalpha():
                op2 = gates[op2]
            gates[k] = op1 & op2
            input(gates)
        elif "OR" in v:
            op1, op2 = v[0], v[-1]
            if op1.isalpha():
                op1 = gates[op1]
            if op2.isalpha():
                op2 = gates[op2]
            gates[k] = op1 | op2
            input(gates)
        elif "NOT" in v:
            op = v[-1]
            if op.isalpha():
                op = gates[v[-1]]
            gates[k] = ~op & 65535
            input(gates)
        elif "LSHIFT" in v:
            op1, op2 = v[0], v[-1]
            if op1.isalpha():
                op1 = gates[op1]
            if op2.isalpha():
                op2 = gates[op2]
            gates[k] = int(op1) << int(op2)
            input(gates)
        elif "RSHIFT" in v:
            op1, op2 = v[0], v[-1]
            if op1.isalpha():
                op1 = gates[op1]
            if op2.isalpha():
                op2 = gates[op2]
            gates[k] = int(op1) >> int(op2)
            input(gates)
        else:
            print("No operator found.")
    return gates['a']

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

    rdata = read_file(inputfile)
    data = parse_data(rdata)

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
