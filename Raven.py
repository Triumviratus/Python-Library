#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------
# Modify the program to count and print the occurrences of each letter in
# the alphabet from a to z, regardless of whether it is lowercase or
# uppercase. Utilize a dictionary in your solution.
#----------------------------------------------------------------------------

import string

def keep_letters(filename):
    file = open(filename, "r")
    modified_text = ""

    for line in file:
        line = line.lower()
        for letter in line:
            if letter in string.ascii_lowercase:
                modified_text += letter

    file.close()
    return modified_text

def calculate_occurrences(original_text):
    occurrences = {}
    for letter in original_text:
        occurrences[letter] = occurrences.get(letter, 0) + 1
    return occurrences

text = keep_letters("raven.txt")
counts = calculate_occurrences(text)
print("\n", counts, "\n")
