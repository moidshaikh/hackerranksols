l, r, k = input().split()
l, r, k = int(l), int(r), int(k)
cnt = 0
for i in range(l, r+1):
    if (i % k == 0):
        cnt += 1
print(cnt)