"""
Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.
"""

def main():

    def hrs_to_minutes(hours):

        total_sec = hours*3600
        mins = int(total_sec// 60)
        sec = (total_sec%60)
        print(mins, "minutes and ",sec, "seconds")
    try:
        hrs = float(input("Please enter a time duration in hours: "))
        if hrs < 0:
            print("Please enter a non-negative number for the time duration.")
        else:
            hrs_to_minutes(hrs)
    except ValueError:
        print("Please enter a valid number.")



if __name__ == '__main__':
    main()