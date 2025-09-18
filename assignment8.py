"""
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.

=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
"""


def main():
    marks = input("Enter marks for three subjects separated by spaces: ")

    # split input into list of strings and convert to integers
    marks_list = list(map(float, marks.split()))

    if len(marks_list) != 3:
        print("Please enter exactly three marks.")
        return

    for i in marks_list:
        if i < 0 or i > 100:
            print("Please enter grades between 0 and 100.")


    # calculate average
    average = sum(marks_list) / 3

    # determine grade
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"Average: {average:.2f}, Grade: {grade}")


main()