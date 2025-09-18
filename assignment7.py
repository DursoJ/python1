"""
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.

===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.
"""

def main():
    input_year = input("Enter a year: ")

    if input_year.isdigit():
        year = int(input_year)

        if year % 400 == 0:
            print("Leap year")
        elif year % 100 == 0:
            print("Not a leap year")
        elif year % 4 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Please enter a valid number.")

main()