def factors(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result




a, b = list(map(int, input().split()))

fa = list(factors(a))
fb = list(factors(b))
# print(fa)
# print(fb)
cnt = 0

if len(fa) < len(fb):
    for i in range(len(fa)):
        if fa[i] in fb:
            cnt += 1
else:
    for i in range(len(fb)):
        if fb[i] in fa:
            cnt += 1
print(cnt)