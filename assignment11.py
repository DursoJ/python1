"""Challenge: Use a loop structure to generate the Collatz sequence until it reaches 1. Handle cases where the user enters a non-numeric input.

=================================
Description: Write a program that generates the Collatz sequence for a given positive integer entered by the user. The Collatz sequence is generated iteratively by repeatedly applying the following rules:
If the current number is even, divide it by 2.
If the current number is odd, multiply it by 3 and add 1."""

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example runs:
print(collatz(1))
print(collatz(2))

num = int(input("Enter a positive integer to generate Collatz sequence: "))
print(collatz(num))