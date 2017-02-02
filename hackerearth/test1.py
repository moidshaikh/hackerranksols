# def power(num, x):
#     if x == 1:
#         return num
#     else:
#         return num ** power(num, x-1)


def power(base,exponent):
    exponent = bin(exponent)[2:][::-1]

    result = 1
    for i in range(len(exponent)):
        if exponent[i] is '1':
            result *= base
        base *= base
    return result


def solution():
    x, k, m = list(map(int, input().split()))
    # print(type(x), type(k), type(m))
    # print(power(x, k) % m)
    res = 1
    # xx = x
    for __ in range(k):
            res *= pow(x,res)

    print(res % m)


test_cases = int(input())

while test_cases > 0:
    solution()
    test_cases -= 1