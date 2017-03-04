# As a beginner to the programming, Mishki came to Hackerearth platform, to become a better programmer. She solved some problems and felt very confident. Later being a fan of Hackerearth, she gave a problem to her friends to solve. They will be given a string containing only lower case characters (a-z), and they need to find that by using the characters of the given string, how many times they can print "hackerearth"(without quotes). As they are new to programming world, please help them.
#
# Input:
# The first line will consists of one integer
# N
# N denoting the length of string.
# Next line will contain the string
# S
# t
# r
# Str containing only lower case characters.
#
# Output:
# Print one integer, denoting the number of times her friends can print "hackerearth" (without quotes).
#
# Constraints:
# 1 ≤ N ≤ 10^6
# 1≤N≤10^6
# Each character of string Str will be in range [a,z]
# def solve_hackerearth(s):
#     h = 'hackerearth'
#     c = 0
#     st = s
#     for i in range(len(st)):
#
#                 c += 1
#                 s.remove(h[i])
#     return c%10


# def occurrences(s):
#     hs = 'acehkrt'
#     hh = [2,1,2,2,1,2,1]
#     # h= 1212
#     cnt = 0
#     res = []
#     for i in range(len(hh)):
#         res.append(s.count(hs[i]))
#     print(res)
#     # while 0 not in res:
#     while all (i > 0 for i in res):
#         cnt += 1
#         res = [m - n for m, n in zip(res, hh)]
#         print(cnt, res)
#     return cnt
#
# # n = int(input())
# st = input()
# print(occurrences(st))


# for i in range(n):
#     flag = 0
    # if 'h' in s:
    #     s = s.replace('h','')
    # if 'a' in s:
    #     s = s.replace('a','')
    # if 'c' in s:
    #     s = s.replace('c','')
    # if 'k' in s:
    #     s = s.replace('k','')
    # if 'e' in s:
    #     s = s.replace('e','')
    # if 'r' in s:
    #     s = s.replace('r','')
    #     print(s)
    # if 'e' in s:
    #     s = s.replace('e','')
    # if 'a' in s:
    #     s = s.replace('a','')
    # if 'r' in s:
    #     s = s.replace('r','')
    # if 't' in s:
    #     s = s.replace('t','')
    # if 'h' in s:
    #     s = s.replace('h','')
    #     cnt += 1

# def occurence(s):
#     a = s.count('a')
#     h = s.count('h')
#     c = s.count('c')
#     k = s.count('k')
#     e = s.count('e')
#     r = s.count('r')
#     t = s.count('t')
#     cnt = 0
#     while a > 4 and h>2 and c>1 and k>1 and e>2 and r>2 and t>1 :
#         cnt += 1
#         a -= 4
#         h -= 2
#         c -= 1
#         k -= 1
#         e -= 2
#         r -= 2
#         t -= 1
#     return cnt
#
# n = int(input())
# st = input()
# print(occurence(st))


from collections import Counter
n = int(input())
s = input()
word = 'hackerearth'

wd = Counter(word)
sd = Counter(s)

print(min((sd.get(c, 0) // wd[c] for c in wd), default=0))