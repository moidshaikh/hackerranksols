l = int(input())
n = int(input())
w, h = [], []

for i in range(n):
    input3 = input().split()
    w.append(input3[0])
    h.append(input3[1])
# print(l, n)

w = list(map(int, w))
h = list(map(int, h))
# print(w, h)

for i in range(len(w)):
    # print(w[i], type(w[i]))
    # print(h[i], type(w[i]))
    if ((w[i] < l) or (h[i] < l)):
        print('UPLOAD ANOTHER')
    elif ((w[i] == h[i])):
            print("ACCEPTED")
    else:
            print('CROP IT')