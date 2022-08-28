# def minion_game(string):
#     # your code goes here
#     # get all substrings of the problem:
#     subs = [string[i:j] for j in range(len(string)+1) for i in range(len(string)+1)]
#     subs = [x for x in subs if len(x)>0]
#     # subs = list(set(subs))

#     d = {
#         'Stuart':0,
#         'Kevin':0
#         }

#     # iterate over substrings.
#     # if substring starts with vowel, increase score of Kevin; else Stuart
#     for w in subs:
#         # print(w)
#         if w[0] in ['A', 'E', 'I', 'O', 'U']:
#             d['Kevin'] += 1
#         else:
#             d['Stuart'] += 1
#     # compare results and return max of both.
#     if d['Stuart'] == d['Kevin']:
#         print('Draw')
#     else:   
#         player, score = max(d.items())
#         # return (player, score)
#         print(f"{player} {score}")
#     return

def minion_game(string):
    # your code goes here
    n = len(string)
    stu, kev = 0, 0
    for i in range(n):
        if string[i] in 'AEIOU':
            stu += (n-i)
        else:
            kev += (n-i)
    if stu > kev:
        print(f"Kevin {stu}")
    elif stu < kev:
        print(f"Stuart {kev}")
    else:
        print("Draw")
    
    return

if __name__ == '__main__':
    minion_game('BANANA')


