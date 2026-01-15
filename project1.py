letter = input("Enter a single letter: ")

if ('A' <= letter <= 'Z') or ('a' <= letter <= 'z'):
    print("'" + letter + "' is an alphabet.")
else:
    print("'" + letter + "' is NOT an alphabet.")