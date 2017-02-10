def digits(n):
    sd = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
    s, d = 0, 0
    if n==0:
        return 6
    while n:
        d = n % 10
        s += sd.get(d)
        n //= 10
    return s

t = int(input())
# sd = { '0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6 }
# sd = [ 6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# t = -2

while t > 0:
    t -= 1
    n = int(input())
    x = [int(i) for i in input().split(' ')]
    s = []
    for i in range(n):
        s.append(digits(x[i]))
    print(x)
    print(s)
    print(x[s.index(min(s))])

