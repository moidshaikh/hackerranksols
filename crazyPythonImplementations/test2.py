
s1 = 'ab'
s2 = 'cdef'

def contains(s1, s2):
    s1 = set(s1)
    # s2 = set(s2)
    s2 = {k:0 for k in s2 }

    res2 = [1 for x in s1 if x not in s2]

    return False if any(res2) else True


    # # print(res2)
    # if any(res2):
    #     return False
    # return True
    # print(res2)
    # for c in s1:
    #     if c in s2:
    #         res.append(1)
    #     else:
    #         res.append(0)
    # print(res)
    # return all(res)

print(contains(s1,s2))