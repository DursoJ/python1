'''Created by John Durso'''

def main():
    '''
    Assignment2
        Implement error handling to ensure that the
        length and width entered by the user are positive numbers.
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