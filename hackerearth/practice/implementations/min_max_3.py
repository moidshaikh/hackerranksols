# Given an array of integers . Check if all the numbers between minimum and maximum number in array exist's within the array .
#
# Print 'YES' if numbers exist otherwise print 'NO'(without quotes).
#
# Input:
#
# Integer N denoting size of array
#
# Next line contains N space separated integers denoting elements in array
#
# Output:
#
# Output your answer

# l = int(input())
# n = [int(i) for i in input().split()]
# mn = min(n)
# mx = max(n)
# ary = [i for i in range(mn, mx+1)]
# # for i in range(len(ary)):
# #     if n[i] in ary:
# #         ary.remove(n[i])
# # if len(ary) == 0:
# #     print('YES')
# # else:
# #     print('NO')
# print(mn, mx)
# print('ary', ary)
# print('n', n)
# for i in range(len(ary)):
#     if ary[i] not in n:
#         print('NO')
#         sys.exit(1)
# print("YES")

import sys
n = int(input())
a=list(map(int,input().split()))

for i in range(min(a),max(a)+1):
    if i not in a:
        print('NO')
        sys.exit()
print('YES')