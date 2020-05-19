#---------------------------------------------------------------
# Ambrose Ryan Xavier
#---------------------------------------------------------------
# Data Generation Template
#---------------------------------------------------------------
# ace hearts king hearts queen hearts
# three diamonds three spades three clubs
# two hearts two diamonds four hearts
# five hearts six diamonds five clubs
# seven hearts eight diamonds eight hearts
# ten hearts nine diamonds jack hearts
#---------------------------------------------------------------
# Desired Output
#---------------------------------------------------------------
# Poker Hand
# ----------
# Card 1: Ace of Hearts
# Card 2: King of Hearts
# Card 3: Queen of Hearts
#
# Poker Hand Evaluation: FLUSH
#
# Poker Hand
# ----------
# Card 1: Three of Diamonds
# Card 2: Three of Spades
# Card 3: Three of Clubs
#
# Poker Hand Evaluation: THREE OF A KIND
#
# Poker Hand
# ----------
# Card 1: Two of Hearts
# Card 2: Two of Diamonds
# Card 3: Four of Hearts
#
# Poker Hand Evaluation: TWO OF A KIND
#
# Poker Hand
# ----------
# Card 1: Five of Hearts
# Card 2: Six of Diamonds
# Card 3: Five of Clubs
#
# Poker Hand Evaluation: TWO OF A KIND
#
# Poker Hand
# ----------
# Card 1: Seven of Hearts
# Card 2: Eight of Diamonds
# Card 3: Eight of Hearts
#
# Poker Hand Evaluation: TWO OF A KIND
#
# Poker Hand
# ----------
# Card 1: Ten of Hearts
# Card 2: Nine of Diamonds
# Card 3: Jack of Hearts
#
# Poker Hand Evaluation: NOTHING
#
#---------------------------------------------------------------

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
