# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5


# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

strings = 'abcdefghijklmnopqrstuvwxyz'


def print_rangoli(size):
    # your code goes here
    res = []
    for i in range(size):
        st = "-".join(strings[i:size])
        res.append(f"{st[::-1]}{st[1:]}".center(4*size-3, '-'))
    # print(L+L[1::-1])  
    return res[::-1]+res[1:]

if __name__ == '__main__':
    # n = int(input())
    s = print_rangoli(5)
    print('\n'.join(s))

