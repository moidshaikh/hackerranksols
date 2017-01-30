l = int(input())
n = [int(i) for i in input().split()]
n.append(0)
n.append(0)
s1, s2, s3 = 0,0,0

for i in range(0,l,3):
    s1 += n[i]
    s2 += n[i+1]
    s3 += n[i+2]

print(s1, s2, s3)