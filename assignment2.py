'''Created by John Durso'''

def main():
    '''
    Assignment2
        Challenge: Implement error handling to ensure that the
        length and width entered by the user are positive numbers.

        Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
        Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
        Output: Display the calculated simple interest.
    '''

    def area_rectangle():
        l = float(input("Enter the length of rectangle: "))
        w = float(input("Enter the width of rectangle: "))
        if l < 0 or w < 0:
            print("Please make sure to enter positive numbers.")
        else:
            print("Area of the rectangle: ", l * w)

    area_rectangle()


main()