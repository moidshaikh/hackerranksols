# from itertools import cycle
# # t = int(input())
# # n, m, s = input().split()
# # n, m, s = int(n), int(m), int(s)
#
# t = 1
# n, m, s = 5, 5, 1
#
# l = [i for i in range(1,n+1)]
#
# # print(t, n, m, s)
# # print(l)
#
#
# m = m % n
#
# print(m)


def save_prisoner(number_of_prisoners, candy, current_prisoner):

    for _ in range(candy-1):
        if current_prisoner == number_of_prisoners:
            current_prisoner = 1
        else:
            current_prisoner += 1
    return current_prisoner


test_cases = int(input())
input2 = []
for _ in range(test_cases):
    input2.append(input())


# print(input2, type(input2))
for _ in range(test_cases):
    n, m, s = map(int, input().split())
    # # n, m, s = 5, 19, 2
    # print(save_prisoner(n, m, s))