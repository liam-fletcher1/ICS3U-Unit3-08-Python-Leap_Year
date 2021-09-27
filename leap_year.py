#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Sep 2021
# This program asks the user to enter a year and
# tells them if the year is a leap year


def main():
    # this tells the user if the year is a leap year

    # input
    leap_year = input("Please enter the year: ")

    # process & output
    try:
        integer_as_number = int(leap_year)

        if integer_as_number % 4 == 0:

            if integer_as_number % 100 == 0:

                if integer_as_number % 400 == 0:
                    print("This is a leap year!")

                else:
                    print("This is a common year!")

            else:
                print("This is a leap year!")

        else:
            print("This is a common year!")

    except Exception:
        print("This is not a year!")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
