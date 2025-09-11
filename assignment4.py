"""
Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.
"""
import math

def main():
    while True:
        try:
            x1, y1, x2, y2 = map(float, input(
                "Please enter the coordinates of two points (x1 y1 x2 y2): "
            ).split())
            break
        except ValueError:
            print("Invalid input. Please enter four numbers separated by spaces.")

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(f"The distance between the two points is: {distance:.2f}")

if __name__ == "__main__":
    main()