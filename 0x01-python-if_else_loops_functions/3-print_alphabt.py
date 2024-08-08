#!/usr/bin/python3

# Print all lowercase letters except 'q' and 'e'
for code in range(97, 123):
    char = chr(code)
    if char != 'q' and char != 'e':
        print(char, end='')

