"""
Challenge: Handle negative exponents efficiently.



====================================

Description: Develop a function named power that takes two integers, base and exponent, as input and returns base raised to the power of exponent.
"""

def power(base, exponent):
    if exponent < 0:
        return 1 / power(base, -exponent)
    elif exponent == 0:
        return 1
    else:
        result = 1
        for _ in range(exponent):
            result *= base
        return result


def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter the exponent: "))
    print(f"{base} raised to the power of {exponent} is {power(base, exponent)}")



main()
