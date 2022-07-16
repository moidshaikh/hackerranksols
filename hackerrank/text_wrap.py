import textwrap

def wrap(s, max_width):
    wrapped = []
    for i in range(0,len(s), max_width):
        wrapped.append(s[i:i+max_width])
    return "\n".join(wrapped)

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

if __name__ == '__main__':
    # string, max_width = input(), int(input())
    string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
    max_width = 4
    result = wrap(string, max_width)
    print(result)