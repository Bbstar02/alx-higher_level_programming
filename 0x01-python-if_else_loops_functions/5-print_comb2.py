#!/usr/bin/python3

# Loop through numbers from 0 to 98
for num in range(0, 99):
    # Print each number in two-digit format, followed by a comma and space
    print("{:02d}".format(num), end=', ')
# Print the last number (99) without the comma at the end
print("{:02d}".format(num + 1))

