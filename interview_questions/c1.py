# binary divide. if number is even half it. if no. is odd add 1 to it. count steps it takes to go to zero.
# input: 3: output: 4
def bin_divide(s):
    # n = bin(s,2)
    # steps = 0
    # while n != 0:
    #     steps += 1
    #     input(n)
    #     if n == 1:
    #         break
    #     if n%2 == 0:
    #         n = n//2
    #     else:
    #         n += 1

    steps = 0
    for c in s:
        if c == '0':
            steps += 1
        else:
            steps += 2

    return steps 

# print(bin_divide(bin(7)[2:]))

def num_divide(n):
    # n = bin(s,2)
    steps = 0
    while n != 0:
        steps += 1
        if n == 1:
            break
        if n%2 == 0:
            n = n//2
        else:
            n += 1
    return steps

def test(n):
    print(num_divide(n))
    print(bin_divide(bin(n)[2:]))



test(11)
