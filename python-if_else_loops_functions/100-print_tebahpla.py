#!/usr/bin/python3

def print_tebahpla():
    # Loop to print the alphabet in reverse order
    for i in range(26):
        # Determine if the position is even or odd
        if i % 2 == 0:
            # For even indices, print lowercase letters starting from 'z'
            print(chr(122 - (i // 1)), end='')
        else:
            # For odd indices, print uppercase letters starting from 'Y'
            print(chr(90 - (i // 1)), end='')

print_tebahpla()
