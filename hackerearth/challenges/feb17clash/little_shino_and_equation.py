i = [int(x) for x in input().split()]
i1, i2, dist = i[0], i[1], i[2]
steps = 0
distance = dist
current_pos = 0
# a = min(i1, i2)
b = max(i1, i2)
while distance > 0:
    distance -= b
    steps += 1
    current_pos += b

print(steps)
print("final", current_pos)