
# n, m, k = map(int, input().split(' '))
n,m,k = 5,2,2
# print(n,m,k)
# print(type(n), type(m), type(k))
pref = [1,1,2,1,1]
# pref = [int(x) for x in input().split()]
seats = []
happy = 0
for i in range(m):
    seats.append([0]*k)
    # print(seats[i])

# print(seats)
final_count = 0

def occupy(rn):
    row = seats[rn]
    if 0 in row:
        zero = row.count(0)-1
        ones = row.count(1)+1
        seats[rn] = [1]*ones + [0]*zero


for i in range(len(pref)):
    p = pref[i]
    occupy(p-1)

print(seats)

cnt = 0

for i in range(len(seats)):
    # print(seats[i])
    cnt += seats[i].count(0)
x = n - (m*k)
print(cnt + x)