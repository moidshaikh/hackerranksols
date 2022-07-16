def print_formatted(number):
    # your code goes here
    # decimals = [x for x in range(1,x+1)]
    # octals = [oct(x).split('o')[-1] for x in range(1, number+1)]
    # hexdec = [hex(x).split('x')[-1] for x in range(1, number+1)]
    # binary = [bin(x).split('b')[-1] for x in range(1, number+1)]

    for i in range(1, number+1):
        print(f"{i}\t{oct(i).split('o')[-1]}\
            \t{(hex(i).split('x')[-1]).upper()}\t{bin(i).split('b')[-1]}")

    """
    Another WAY
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width),octa.rjust(width),hexa.rjust(width),bina.rjust(width))
    """

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
