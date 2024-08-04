#!/usr/bin/python3
# Define the string variable with a long sentence
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# Concatenate specific slices of the string and assign to str
str = str[39:66] + str[106:112] + str[:6]
# Print the concatenated result
print(str)
