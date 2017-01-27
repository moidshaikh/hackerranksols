c = 10**9 + 7

n = int(input())
a = input().split()

ans = 1

for i in range(len(a)):
    if (ans < c):
        ans = (ans * int(a[i])) % c
    else:
        ans = ans * int(a[i])

print(ans)