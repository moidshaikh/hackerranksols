# #!/bin/python3
#
# import sys
#
#
# n,c = input().strip().split(' ')
# n,c = [int(n),int(c)]
# crate = []
# for crate_i in range(c):
#    crate_t = [int(crate_temp) for crate_temp in input().strip().split(' ')]
#    crate.append(crate_t)
# # # your code goes here
# #
#
# # n, c = 3,3
# # crate = [[1, 3], [2, 2], [3, 1]]
# options = []
# for i in range(len(crate)):
#     # print(crate[i], crate[i][0], crate[i][1])
#     for j in range(crate[i][0]):
#         options.append(crate[i][1])
#
# # print(options)
# options.sort()
# # print("options:", options)
# maxim = 0
# ops = options
# for i in range(n):
#     maxim += max(ops)
#     # print(maxim)
#     ops.pop()
#
# print(maxim)


n,c = input().strip().split(' ')
n,c = [int(n),int(c)]
crate = []
for crate_i in range(c):
   crate_t = [int(crate_temp) for crate_temp in input().strip().split(' ')]
   crate.append(crate_t)


def largestBox(crates):

    largest = 0
    for i in crates:
        if i[1] > largest:
            largest = i[1]
    return largest

largest = largestBox(crate)


def total(largest, n):

    total = 0
    index = 0
    while n > 0:
        for box in crate:
            if box[1] == largest:
                for i in range(box[0]):
                    n -= 1
                    total += box[1]
                    if n == 0:
                        return total
                del crate[index]
                largest = largestBox(crate)

            index += 1
print(total(largest, n))