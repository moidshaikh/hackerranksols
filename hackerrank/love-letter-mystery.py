'''
Solution to hackerrank challenge
https://www.hackerrank.com/challenges/the-love-letter-mystery
'''

from itertools import islice


def count_operations(word):
    diff = lambda x, y: abs(ord(x) - ord(y))
    median = len(word) // 2
    pairs = zip(word, reversed(word))
    operations = sum(diff(x, y) for x, y in islice(pairs, median))
    return operations

word_count = int(input())

for _ in range(word_count):
    word = input()
    print(count_operations(word))