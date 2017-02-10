'''

Write a program  that reads lines of input from the user and converts each line into "Pig Latin."'
Pig Latin is English with the initial consonant sound moved to the end of each word,
followed by "ay". Words that begin with vowels simply have an "ay" appended.

Your program  should continuously prompt the user for sentences
until  they enter a blank line, at which point the program  should terminate.

'''


def pig_latin(sentence):
    # splitting sentence into list of words
    sentence = sentence.split()

    for k in range(len(sentence)):
        word = sentence[k]
        # condition 1: if word begins with a Vowel, we have to add 'ay' with the word
        if word[0] in ['a', 'e', 'i', 'o', 'u']:
            sentence[k] = word + 'ay'
        # condition 2: if word contains numbeers, we display it as is
        elif not word.isalpha():
            sentence[k] = word
        # condition 3: if word begins with a Consonant, we move initial consonant and add 'ay' to it.
        else:
            sentence[k] = word[1:] + word[0] + 'ay'
    # Joining the newly created pig-latin words
    return ' '.join(sentence)


# user_input = input()
print("Enter blank line at anytime to terminate the program.")
while True:
    input_sentence = input()
    # below code is to get input lines until user puts blank line to terminate program
    if input_sentence == "":
        break
    else:
        print(pig_latin(input_sentence))