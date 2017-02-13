l = []


def printlist():
    global l
    print("OUTPUT")
    for i in range(len(l)):
        print(l[i])


def checkstring(word):
    global l
    new_list = l
    for i in range(len(l)):
        if l[i] in word:
            new_list.remove(l[i])
    l = new_list


while True:
    w = input()
    if w == 'quit':
        printlist()
        exit(1)
    if len(w) < 4:
        l.append(w)
    else:
        checkstring(w)
