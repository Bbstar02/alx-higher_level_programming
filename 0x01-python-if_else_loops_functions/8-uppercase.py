#!/usr/bin/python3

def uppercase(string):
    # Iterate through each character in the string
    for character in string:
        # Check if the character is lowercase
        if ord(character) >= 97 and ord(character) <= 122:
            # Convert lowercase character to uppercase
            character = chr(ord(character) - 32)
        # Print the character without a newline
        print("{:s}".format(character), end='')

    # Print a newline at the end
    print('')

