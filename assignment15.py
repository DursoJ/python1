"""
Challenge: Write the function using recursion.

===================================
Description: Create a function named is_palindrome that takes a string as input and returns True if it is a palindrome, and False otherwise.
"""

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def main():
    text = input("Enter a string: ")
    cleaned = ''.join(text.lower().split())
    if is_palindrome(cleaned):
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")



main()
