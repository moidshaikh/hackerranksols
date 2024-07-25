def which_floor(s: str) -> int:    
    f = 0    
    for c in s:
        if c == "(":
            f += 1
        elif c == ")":
            f -= 1
        else:
            print("ERROR")
    return f

import time

def which_floor2(s: str) -> int:    
    floor = 0
    instructions_executed = 1
    for instruction in s:
        print(f"{instructions_executed=}  {floor=}")
        if instruction == ")":
            floor += 1
        elif instruction == "(":
            floor -= 1
        if floor == -1:
            return instructions_executed
        instructions_executed += 1


with open("input2", 'r') as f:
    s = f.read()

# print(len(s))
print(which_floor2(s.strip()))