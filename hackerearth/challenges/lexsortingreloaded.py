def lexsort():
    n = int(input())
    words = []
    # max word length
    # maximum, minimum = 0
    while n > 0:
        word = input()
        words.append(word)
    #     if len(word) > maximum:
    #         m = len(word)
    #     if len(word) < minimum:
    #         m = len(word)
        n -= 1
    # print(maximum, minimum)
    word_list = sorted(words,key=len)
    dd = {}
    for i in range(len(word_list)):
        k = len(word_list[i])
        v = word_list[i]
        dd[k] = v

    print( dd.keys(), dd.values())


test_cases = int(input())

while test_cases > 0:
    lexsort()
    test_cases -= 1
#
#
# # l = [[5, 5, 3], [3, 4, 4, 4, 4], [11,11], [5, 5, 5, 5, 5]]
# # w = [['fuNny', 'funny', 'fun'], ['All', 'hall', 'Fall', 'ball', 'Call'], ['hello world', 'World Hello'], ['HellO', 'hello', 'HEllo', 'hellO', 'Hello']]
# #
# # a = l[0]
# b = ['fuNny', 'funny', 'fun']
# #
# # print(b)
# ss = (sorted(b,key=len))
# print(ss)
# # print(b.sort(key=lambda item: (-len(item), item)))