def remove_dupes(s):
    res = ''
    for c in s:
        if c not in res:
            res += c
    return res

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        subs = string[i:i+k]
        # print(subs)
        print(remove_dupes(subs))

if __name__ == '__main__':
    merge_the_tools('123111232',3)