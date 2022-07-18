

# input
a = [1, 3, 4, 5, 6, 7, 9] * 10000000

# output
# a = [1, 4, 8, 13, 19, 26, 35]


# normal function
def cumsum(li):
    final = []
    csum = 0
    for item in li:
        csum += item
        final.append(csum)
    return final


# using generator function
def accumsum(lis):
    total = 0
    for x in lis:
        total += x
        yield total




print(f"output: {list(accumsum(a))}")