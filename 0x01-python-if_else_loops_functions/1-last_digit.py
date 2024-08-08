#!/usr/bin/python3
import random

# Generate a random number within the range of -10000 to 10000
number = random.randint(-10000, 10000)

# Calculate the last digit of the absolute value of the number
last_digit = abs(number) % 10

# Determine the description based on the value of the last digit
if last_digit > 5:
    description = "and is greater than 5"
elif last_digit == 0:
    description = "and is 0"
else:
    description = "and is less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_digit} {description}")

