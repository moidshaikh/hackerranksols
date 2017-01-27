# Inputs
n, d = input().split()
a = input().split(' ')

n = int(n)
d = int(d)
l = []

for i in range(len(a)):
    # print(a.split()[i])
    l.append(int(a[i]))

cnt = 0
for i in range(len(l)):
    if (l[i]+d) in l:
        if(l[i]+d+d) in l:
            cnt += 1
print(cnt)