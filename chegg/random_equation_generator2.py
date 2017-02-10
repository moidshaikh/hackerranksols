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

OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.floordiv),
]


def random_question(binary_operations, operand_range):
    """Generate a pair consisting of a random question (as a string)
    and its answer (as a number)"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(min(operand_range), max(operand_range))
    n2 = random.randint(min(operand_range), max(operand_range))
    question = '{} {} {}'.format(n1, op_sym, n2)
    answer = op_func(n1, n2)
    return question, answer


def quiz(number_of_questions):
    """Ask the specified number of questions, and return the number of correct
    answers."""
    score = 0
    for _ in range(number_of_questions):
        question, answer = random_question(OPERATIONS, range(0, 21))
        print('What is {}'.format(question))
        try:
            user_input = float(input("Enter the answer: "))
        except ValueError:
            print("I'm sorry that's invalid")
        else:
            if answer == user_input:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect!\n")
    return score


def identify_user():
    # TODO, as an exercise for you
    pass


def display_score(first_name, last_name, class_name):
    # TODO, as an exercise for you
    pass


def menu():
    # TODO, as an exercise for you
    pass


def main():
    first_name, last_name, class_name = identify_user()
    while True:
        menu_choice = menu()
        if menu_choice == 1:        # Display score
            display_score(first_name, last_name, class_name)

        elif menu_choice == 2:      # Run quiz
            QUESTIONS = 10
            score = quiz(QUESTIONS)
            print('{first_name} {last_name}, you scored {score} out of {QUESTIONS}'.format(**locals()))

        elif menu_choice == 3:      # Exit
            break

        else:
            print("Sorry, I don't understand. Please try again...")
            print()

if __name__ == '__main__':
    main()