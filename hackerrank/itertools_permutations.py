# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

# s, n = input().split(' ')

s, n = 'abcdef', 3
# res = [''.join(x) for x in (list(permutations(s, int(n))))]


res = [''.join(x) for x in permutations(s,n)]

print('\n'.join(res))
