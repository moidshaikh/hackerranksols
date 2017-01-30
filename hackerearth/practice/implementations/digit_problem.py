# Taking input from user

inpt = input().split()
num = int(inpt[0])
d = int(inpt[1])

l = [int(d) for d in str(num)]
i = 0

while d > 0:
    d -= 1

    if l[i] == 9:
        d += 1
    else:
        l[i] = 9

    i += 1
    l = map(str, l)
print(''.join(str(l)))