
def get_magic(vale):
    primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    # print(min(primes, key=lambda x:abs(x-vale)))
    return (min(primes, key=lambda x:abs(x-vale)))
#
def magical_words():
    n = int(input())
    s = input()
    output = []
    for i in range(n):
    # print(s[i], ord(s[i]))
        c = get_magic(ord(s[i]))
        output.append(chr(c))
    print(''.join(output))


test_cases = int(input())

while test_cases != 0:
    # print(test_cases)
    # test_cases -= 1
    magical_words()
    test_cases -= 1