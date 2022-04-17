import math
from project_euler.problem_utils import is_prime, is_factor


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


"""
Problem 2:
Even Fibonacci Numbers

By considering the terms in the Fibonacci sequence whose values do not exceed x, find the sum of the even-valued terms.
"""


def even_fibonacci_numbers(x):
    # I do not want to do this again
    # Will update when possible
    pass


"""
Problem 3:
Largest Prime Factor

What is the largest prime factor of a given number?
"""


def largest_prime_factor(number):
    the_answer = 0

    for num in range(int(math.sqrt(number)) + 1, 1, -1):
        if not is_factor(num, number):
            continue

        if is_prime(num) and num > the_answer:
            the_answer = num
        elif is_prime(num) and num < the_answer:
            return the_answer

    return number
