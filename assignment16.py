"""
Challenge: Optimize the function to handle large input numbers efficiently.

=====================================================
Description: Develop a function called is_prime that takes a positive integer as input and returns True if it is a prime number, and False otherwise.
"""

import math

def is_prime(n):
    # Handle base cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Eliminate multiples of 2 and 3 early
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check for factors up to the square root of n
    # Using 6k ± 1 optimization to skip unnecessary checks
    limit = int(math.sqrt(n)) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


def main():
    number = int(input("Enter a positive integer: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


main()
