if __name__ == '__main__':
    s = input()
    # any alphanumeric
    print(any(x.isalnum() for x in s))
    # any alphabetic
    print(any(x.isalpha() for x in s))
    # any digits or false
    print(any(x.isdigit() for x in s))
    # any lowercase or false
    print(any(x.islower() for x in s))
    # any uppercase or false
    print(any(x.isupper() for x in s))
