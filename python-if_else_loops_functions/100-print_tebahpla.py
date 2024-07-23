#!/usr/bin/python3

def print_tebahpla():
    # Initialize an empty string to hold the result
    result = ''
    # Loop to build the string of the alphabet in reverse order
    for i in range(26):
        # Determine if the position is even or odd
        if i % 2 == 0:
            # For even indices, add lowercase letters starting from 'z'
            result += chr(122 - (i // 1))
        else:
            # For odd indices, add uppercase letters starting from 'Y'
            result += chr(90 - (i // 1))
    # Print the final result string using string formatting without a newline
    print("{}".format(result), end='')

print_tebahpla()
