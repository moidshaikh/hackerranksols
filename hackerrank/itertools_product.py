# from math import prod


# def product(A, B):
#     for a in A:
#         for b in B:
#             print(a,b)

# product([11,22],[33,44])

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product 
a = map(int, input().split())
b = map(int, input().split())

print(*product(a, b))