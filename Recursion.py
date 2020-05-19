#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

def count_vowels(sentence):
    x = sentence.count("a")
    x = x + sentence.count("e")
    x = x + sentence.count("i")
    x = x + sentence.count("o")
    x = x + sentence.count("u")
    return x

def count_vowels_iterative(sentence):
    counter = 0
    for c in sentence:
        if c == "a":
            counter += 1
        elif c == "e":
            counter += 1
        elif c == "i":
            counter += 1
        elif c == "o":
            counter += 1
        elif c == "u":
            counter += 1
    return counter

def count_vowels_recursive(sentence):
    if sentence == "":
        return 0
    return ((1 if sentence[0] in "aeiou" else 0) + count_vowels_recursive(sentence[1:]))

# If the snetence is one character long, check if it is a vowel.
# The return function following the base case contains two general cases.
# If the sentence is longer than one character, the first character is examined
# and the remaining characters in the sentence are sent back into the function.

def main():
    answer = "yes"
    while ((answer == "yes") or (answer == "y")):
        sentence = input("Please enter a sentence to evaluate: ")
        sentence = sentence.lower()
        print("\nNumber of vowels utilizing count   =", count_vowels(sentence))
        print("Number of vowels utilizing iteration =", count_vowels_iterative(sentence))
        print("Number of vowels utilizing recursion =", count_vowels_recursive(sentence), "\n")
        answer = input("Would you prefer to continue: ").lower()
        print()

main()
