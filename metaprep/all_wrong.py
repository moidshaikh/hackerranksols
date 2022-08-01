"""There's a multiple-choice test with NN questions, numbered from 11 to NN. Each question has 22 answer options, labelled A and B. You know that the correct answer for the iith question is the iith character in the string CC, which is either "A" or "B", but you want to get a score of 00 on this test by answering every question incorrectly.
Your task is to implement the function getWrongAnswers(N, C) which returns a string with NN characters, the iith of which is the answer you should give for question ii in order to get it wrong (either "A" or "B").
Constraints
1 \le N \le 1001≤N≤100
C_i \in \{``A", ``B"\}C 
i
​
 ∈{‘‘A",‘‘B"}"""

# Write any import statements here
# Write any import statements here


def getIncorrect(a: str) -> str:
    return "A" if a == "B" else "B"


def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    # method 1
    # return ''.join([getIncorrect(x) for x in C])

    # method 2
    # return ''.join(map(getIncorrect, list(C)))

    # method 3: without using function
    # ''.join(map(lambda x: 'A' if x=='B' else 'B', list(C))

    # method 4: without using function
    # Check for valid string: string should contain just 'A' or 'B'
    if not C.count("A") + C.count("B") == len(C):
        return "INVALID STRING"
    res = ""
    for ch in C:
        if ch == "A":
            res += "B"
        else:
            res += "A"
    return res


print(getWrongAnswers(3, "ABA"))
print(getWrongAnswers(5, "BBBBB"))
