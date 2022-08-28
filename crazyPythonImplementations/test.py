

def isedit(s1, s2):

    diff = 0

    # if  <= 2:
    #     return False
    # s1 = sorted(s1)
    # s2 = sorted(s2)


    n = min(len(s1), len(s2))
    # len_diff = abs(len(s1)-len(s2))

    for i in range(n):
        if s1[i] != s2[i]:
            diff += 1

    # print(diff)
    # check for diff
    if diff == 1:
        return True
    else:
        return False

    



print(isedit('str1', 'str1'))
print(isedit('str1', 'str2'))
print(isedit('str1', 'st1'))
print(isedit('str1', 'tr1'))
print(isedit('tr1', 'str1'))
print(isedit('st1r', 'str1'))


