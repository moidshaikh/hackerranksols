# Here, we have tho find out, count of number's occurrences in a string

s = input()
o = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = list(map(int, n))

for i in range(len(s)):
    if s[i].isdigit():
        n[int(s[i])] += 1

for i in range(len(n)):
    n[i] -= o[i]
#
# print(o)
# print(n)

for index, element in enumerate(n):
    print(index, element)