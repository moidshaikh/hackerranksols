'''
Solution to hackerrank challenge
https://www.hackerrank.com/challenges/beautiful-binary-string
'''



# n = int(input())
# binary = input()
# cnt = 0
# #
# # def substring(strr):
# #     global cnt
# #     for i in range(0, len(strr), 3):
# #         if strr[i:i+3] == '010':
# #             new_string = strr[:i+1] + '1' + strr[i+3:]
# #             cnt += 1
# #             substring(new_string)
# #     return cnt
#
# # print("sdfsdf b s d :::::::  ", substring(binary))
# strr = binary
#
# for i in range(0, len(strr), 3):
#     print(strr[i:i+3])
#     # if strr[i:i + 3] == '010':
#     #     new_string = strr[:i + 1] + '1' + strr[i + 3:]
#     #     cnt += 1
#
# print("sdfsdf:::", cnt)

n = int(input())
b = list(input())
cnt = 0
for i in range(n):
    if b[i:i+3] == ['0','1','0']:
        b[i+2] = '1'
        cnt += 1
print(cnt)