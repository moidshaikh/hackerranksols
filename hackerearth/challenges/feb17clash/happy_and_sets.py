from itertools import combinations

l = []

# no = int(input())
# s = [int(x) for x in input().split()]
inputs = [1, 2, 3]

output = sum([map(list, combinations(inputs, i)) for i in range(len(inputs) + 1)], [])

# print(output)

# print("sdlfkjsdlfjsdlfj")

for o in output:
    print (o)