"""
Problem 1:
Multiples of 3 or 5

Find the sum of all the multiples of 3 or 5 below a given number.
"""


def multiples_of_3_or_5(num):
    sum_of_multiples = 0

    for x in range(3, num):
        if (not x % 3) or (not x % 5):
            sum_of_multiples += x

    return sum_of_multiples
