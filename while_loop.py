#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program is for while loop


def main():
    # this function is for while loop
    basic_number = 0
    loop_number = 0

    # input
    positive_number = input("Enter a positive number: ")
    print("")

    # process & output
    try:
        positive_number_int = int(positive_number)
        print("It is a integer")
        if positive_number_int > 0:
            while basic_number <= positive_number_int:
                loop_number = loop_number + basic_number
                basic_number = basic_number + 1
            print("∑i = {0}".format(loop_number))
        else:
            print("It is not a positive number")
    except Exception:
        print("It is not a integer")
    finally:
        print("Done!")


if __name__ == "__main__":
    main()
