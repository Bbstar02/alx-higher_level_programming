#!/usr/bin/python3

def print_last_digit(num):
    '''Function to print the last digit of a number'''
    # Calculate the last digit by taking the absolute value and using modulo
    final_digit = abs(num) % 10
    # Print the last digit without a newline
    print(f"{final_digit}", end='')
    # Return the last digit
    return final_digit

