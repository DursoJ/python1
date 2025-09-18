"""
Challenge: Ensure that the user enters only a single character and handle cases where the input is not a letter.

=====================================================
Input: Ask the user to enter a single character.
Processing: Determine whether the entered character is a vowel (a, e, i, o, u) or a consonant.
Output: Display whether the entered character is a vowel or a consonant.
"""


def main():
    vowels = ['a', 'e', 'i', 'o', 'u']

    letter = input("Please enter a single character: ")
    if not letter.isalpha() or len(letter) > 1:
        print("Please enter a single character.")
        return

    if letter in vowels:
        print("You entered a vowel.")
    else:
        print("You entered a consonant.")

main()