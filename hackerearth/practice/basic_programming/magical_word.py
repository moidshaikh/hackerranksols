# test_cases = int(input())
# t, s = [], []
#
# for _ in range(test_cases):
#     t.append(int(input()))
#     s.append(input())
#
# print(t)
# print(s)
#
#
# Prime ASCII values of alphabets
# [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

# print(ord('a'), ord('z')) # 97 to 122
# print(ord('A'), ord('Z')) # 65 to 90


# finding primes

# primes = []
#
# for num in range(65,91):
#    # prime numbers are greater than 1
#    if num > 1:
#        for i in range(2,num):
#            if (num % i) == 0:
#                break
#        else:
#            primes.append(num)
#
# print(primes)
#
# primes = []
# for num in range(55, 139):
#     # prime numbers are greater than 1
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             primes.append(num)
#
# print(primes)

pr = [61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127]

def nearestPrime(n):

    for i in range(len(pr)-1):
        if (n == pr[i]):
            return i+1
        else:
            if (n in range(pr[i],pr[i+1])):
                if(abs(n-pr[i]) <= abs(n-pr[i+1])):
                    if (pr[i] == 61):
                        return pr[i+1]
                    return(pr[i])
                else:
                    if(pr[i+1]==127):
                        return pr[i]
                    return(pr[i+1])

test_cases = int(input())
t, s, sol = [], [], []

for _ in range(test_cases):
    t.append(int(input()))
    s.append(input())

for i in range(test_cases):
    for j in range(len(s[i])):
        ch = nearestPrime(ord(s[i][j]))
        sol.append(chr(ch))

print(''.join(sol))