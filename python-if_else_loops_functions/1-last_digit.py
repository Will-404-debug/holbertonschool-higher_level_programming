#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Extract the last digit
last_digit = number % 10
if number < 0:
    last_digit = -(-number % 10)

# Determine the appropriate message
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Print the result
print(f"Last digit of {number} is {last_digit} {message}")
