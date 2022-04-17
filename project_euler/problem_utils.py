import math


# Get sum of digits for given number
def get_digit_sum(num):
    digit_sum = 0
    while num != 0:
        digit_sum += num % 10
        num /= 10
    return int(digit_sum)


# Determine if a number is prime
def is_prime(x):
    for number in range(2, int(math.sqrt(x)) + 1):
        if not x % number:
            return False
    return True


def is_factor(num_to_check, num_to_check_against):
    return not num_to_check_against % num_to_check
