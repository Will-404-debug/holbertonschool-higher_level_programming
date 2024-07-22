def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            # Convert lowercase to uppercase
            c = chr(ord(c) - 32)
        print("{}".format(c), end='')
    print()
