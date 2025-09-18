"""
Challenge: Implement error handling to ensure that the user enters a positive integer for the age.

==================================
Input: Prompt the user to enter their age.
Processing: Classify the age into different categories:
Under 18: Minor
18-65: Adult
Above 65: Senior citizen
Output: Display the category based on the entered age.
"""

def main():
    age = int(input("Please enter your age: "))

    if age < 0:
        print("Please input a positive age.")
        return

    if age < 18:
        print("You are a minor")
    elif age < 65:
        print("You are an adult")
    else:
        print("You are a senior citizen")

main()