#!/usr/bin/python3

def remove_char_at(s, n):
    if n < 0 or n >= len(s):
        return s
    return s[:n] + s[n+1:]

# You can test the function with the provided examples
if __name__ == "__main__":
    print(remove_char_at("Best School", 3))  # "Bes School"
    print(remove_char_at("Chicago", 2))      # "Chcago"
    print(remove_char_at("C is fun!", 0))    # " is fun!"
    print(remove_char_at("School", 10))      # "School"
    print(remove_char_at("Python", -2))      # "Python"
