t = int(input())

n, m, s = input().split()

n, m, s = int(n), int(m), int(s)

# t = 1
# n, m, s = 5,2,1

# print(n, m, s)
# print(type(n), type(m), type(s))

pos = s

while(m>n):
    m -= n

while(m>0):
    if(pos == n):
        pos = 1
    pos += 1
    m -= 1

if(pos==1):
    pos = n
else:
    print(pos-1)