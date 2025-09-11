'''Created by John Durso'''

def main():

    '''
    Assignment1
        Challenge: Handle cases where the user enters non-numeric input for the principal amount,
        interest rate, or time period, and provide appropriate error messages.

        Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
        Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
        Output: Display the calculated simple interest.
    '''
    def get_nums():
        try:
            p = float(input("Enter the principal amount: "))
            i = float(input("Enter the interest rate as decimal value: "))
            t = float(input("Enter the time period in years: "))
            si = p*i*t/100
            print("Your simple interest rate: ", si)
        except ValueError:
            print("These values must be numbers. Please try again.")
            return None

    get_nums()

main()