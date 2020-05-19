#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import random

def legal_play(value_01, color_01, value_02, color_02):
    return ((value_01 == value_02) or (color_01 == color_02))

print(legal_play(3, "blue", 3, "green"))
print(legal_play(5, "yellow", 7, "yellow"))
print(legal_play(9, "red", 6, "green"), "\n")

print("Loop With Continuation\n")
for i in range(2000, 2017):
    if i % 7 == 0:
        continue
    print(i)

print("\nLoop With Break\n")
for i in range(2000, 2017):
    if i % 7 == 0:
        break
    print(i)

answer = random.randint(1, 10)

number_of_guesses = 0
current_guess = -1

while (current_guess != answer):
    current_guess = int(input("Enter a Guess: "))
    current_guess = int(current_guess)
    number_of_guesses = number_of_guesses + 1

print("Congratulations! That took", number_of_guesses, "guess(es).\n")

columns = int(input("Enter Number of Columns: "))
rows = int(input("Enter Number of Rows: "))
print()

for i in range(rows):
    line = ""
    for column in range(columns):
        if (random.randint(1, 2) == 1):
            char = "*"
        else:
            char = "-"
        line = line + char
    print(line)

print()
