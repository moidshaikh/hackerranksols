'''
Write a program that generates a series of random equations and prompts the user to answer each equation generated. The program should keep track of each equation and whether or not the equation was answered correctly. If an equation is generated that has already been presented to the user, the program should check if the equation was previously answered correctly. If it was answered correctly, the equation should be ignored and a new equation generated. If the equation was not answered correctly, the user should be prompted to answer it.
The program should implement 4 levels of difficulty based on the range of operands that can be generated at each level.
Level 1: 0 - 10
Level 2: 0 - 25
Level 3: 10 - 25
Level 4: -25 - 25
The program should begin at Level 1. After ten (10) equations in a row have been answered correctly, the program should prompt the user with the following list of options:
1. Continue at the current level.
2. Go to the next level.
3. Display summary statistics for the current level.
4. Quit.
If the user chooses to continue at the current level, the program should continue generating equations until the user correctly answers in a row the next ten (10) equations generated and then follow with the menu options. If the user chooses to increase the level, the minimum and maximum range should be updated accordingly and the program should continue to generate equations. If the user chooses to see summary statistics, the program should display the following information:
% of addition equations correctly answered,
% of subtraction equations correctly answered,
% of multiplication equations correctly answered,
% of division equations correctly answered
at the current level. The user should then be presented with the menu options again and proceed accordingly.

Note that when calculating the summary statistics an equation generated a second time should only be included in the summary if the equation was answered incorrectly previously and the user prompted to answer again.
If the user chooses to quit the program, the program should display summary statistics for each of the levels the game was played on and exit politely.
'''

import operator
import random

score = {
    '+': 0,
    '-': 0,
    '*': 0,
    '/': 0,
    'current': 0,
    'total': 0
}

OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.floordiv),
]

# list of questions asked
asked_questions = []

# no of questions asked
n = 0
# range of different levels
levels = [range(0, 10), range(0, 25), range(10, 25), range(-25, 25)]

current_level_index = 0


def random_equation(binary_operations, operand_range):
    """Generate a pair consisting of a random question (as a string)
    and its answer (as a number)"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(min(operand_range), max(operand_range))
    n2 = random.randint(min(operand_range), max(operand_range))
    ques = '{} {} {}'.format(n1, op_sym, n2)
    ans = op_func(n1, n2)
    return ques, ans, op_sym


def askquestion(level):
    # score = 0
    question, answer, sign = random_equation(OPERATIONS, level)
    asked_questions.append(question)
    if question not in asked_questions:
        print('What is {}'.format(question))
        try:
            user_input = float(input("Enter the answer: "))
        except ValueError:
            print("I'm sorry that's invalid")
        else:
            if answer == user_input:
                print("Correct!\n")
                score[sign] += 1
                score['current'] += 1
                score['total'] += 1
                # score += 1
            else:
                print("Incorrect!\n")
    # else:
    #     question()
            # print("correct ans is::" + str(answer))


def print_options():
    print("press correct option::")
    print("1 to continue current level")
    print("2 to go to next level")
    print("3 to display summary statistics of current level")
    print("4 to quit")
    return int(input(n))


def display_scores(cli):
    return None


def display_statistics():
    print("% of addition equations correctly answered is:", "%.2f" % (score['+']/len(score)*100))
    print("% of subtraction equations correctly answered is:", "%.2f" % (score['-']/len(score)*100))
    print("% of multiplication equations correctly answered is:", "%.2f" % (score['*']/len(score)*100))
    print("% of division equations correctly answered is:", "%.2f" % (score['/']/len(score)*100))


def menu():
    global current_level_index
    op = print_options()
    if op == 1:
        pass
    elif op == 2:
        current_level_index += 1
    elif op == 3:
        display_scores(current_level_index)
    elif op == 4:
        exit(1)

while True:
    global n
    n += 1
    # print(levels[current_level_index])
    # if n % 10 == 0:
    #     menu()
    askquestion(levels[current_level_index])
#



#
# def quiz(number_of_questions):
#     """Ask the specified number of questions, and return the number of correct
#     answers."""
#     score = 0
#     for _ in range(number_of_questions):
#         question, answer = random_question(OPERATIONS, range(0, 21))
#         print('What is {}'.format(question))
#         try:
#             user_input = float(input("Enter the answer: "))
#         except ValueError:
#             print("I'm sorry that's invalid")
#         else:
#             if answer == user_input:
#                 print("Correct!\n")
#                 score += 1
#             else:
#                 print("Incorrect!\n")
#     return score
#
#
# # def identify_user():
# #     # TODO, as an exercise for you
# #     pass
#
#
# def display_score(first_name, last_name, class_name):
#     # TODO, as an exercise for you
#     pass
#
#
# def menu():
#     # TODO, as an exercise for you
#     pass
#
#
# def main():
#     # first_name, last_name, class_name = identify_user()
#     while True:
#         menu_choice = menu()
#         if menu_choice == 1:        # Display score
#             display_score(first_name, last_name, class_name)
#
#         elif menu_choice == 2:      # Run quiz
#             QUESTIONS = 10
#             score = quiz(QUESTIONS)
#             print('{first_name} {last_name}, you scored {score} out of {QUESTIONS}'.format(**locals()))
#
#         elif menu_choice == 3:      # Exit
#             break
#
#         else:
#             print("Sorry, I don't understand. Please try again...")
#             print()
#
# if __name__ == '__main__':
#     main()

