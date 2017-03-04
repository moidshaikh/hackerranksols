# test_case = int(input())
# for i in range(test_case):
#     num = int(input())
#     total_sum = 0
#     for j in range(2, num):
#         remainder = j + 1
#         temp = num
#         while remainder >= j:
#             remainder = int(temp / j)
#             total_sum += temp % j
#             temp = remainder
#         total_sum += remainder
#     k = num - 2
#     flag = 1
#     while k > 1:
#         if total_sum % k == 0 and (num - 2) % k == 0:
#             flag = 0
#             break
#         else:
#             k -= 1
#     if flag == 0:
#         print(int((num-2)/k))
#     else:
#         print(int(num-2))

# [[16, 12, 5, 19, 9]]
# [[17, 13, 9, 20, 15]]
# [[18, 14, 15, 22, 21]]
# [[19, 16, 21, 23, 1]]
# [[20, 17, 1, 24, 5]]
# 21, 18,   ,

# s = ['PLESI','QMITO', 'RNOVU', 'SPUWA', 'TQAXE']
s = 'BDGKP'
l = []
ans = []
for i in range(5):
    l.append(ord(s[i])-64)
ans.append(l)

print(24)