#!/usr/bin/env python3
# Created by Marc Coffi
# Created in May 2022
# This program generate 10 random numbers
# and returns the max value

import random

# Defining the function that returns the max value
def max_value(list):
    total_sum = -1
    for counter in range(1, 10):
        if list[counter] > total_sum:
            total_sum = list[counter]
    return total_sum


def main():
    # Creating empty list and "max_num" variable
    nums = []
    max_num = 0
    # Generating the 10 random numbers
    for counter in range(10):
        random_num = random.randint(0, 100)
        nums.append(random_num)
        print("{} added to list at index {}".format(random_num, counter))

    # Calling the function
    max_num = max_value(nums)

    # Displaying the max number
    print()
    print("The max number is {}".format(max_num))


if __name__ == "__main__":
    main()
