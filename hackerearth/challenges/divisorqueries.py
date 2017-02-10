def primefactors(x):
    factorlist=[]
    loop=2
    while loop<=x:
        if x%loop==0:
            x/=loop
            factorlist.append(loop)
        else:
            loop+=1
    return factorlist

def factorcount(s):
    xx=primefactors(s)
    facindex=[]
    for x in xx:
        z=xx.count(x)
        if [x,z] not in facindex:
            facindex.append([x,z])
    numfac=1
    for [p,q] in facindex:
        numfac*=(q+1)
    return numfac


# # def divisors_count(x):
# #     cnt = 0
# #     for i in range(1, x + 1):
# #         if x % i == 0:
# #             cnt += 1
# #     return cnt
#
# # nums = [1,2,3,4,5,6]
#
#

def printsolutions():
    l, r = map(int, input().split())
    print(l,r)
    prod = 1
    for i in range(l-1, r):
        prod *= nums[i]
    print(factorcount(prod))


n, q = map(int, input().split())
nums = list(map(int, input().split(' ')))
while q > 0:
    printsolutions()
    q -= 1

# print("no of elements", n)
# print("no of queries", q)
# print("array:::", (nums))
# print("queries", (queries))
#
# # print(divisors_count(8988888))