#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import string

# Robust Input

print("Robust Input\n")

def valid(item):
    for char in item:
        if char in string.digits:
            return True
        return False

def double_integer():
    
    done = False
    
    while not done:
        candidate = input("Enter a non-negative integer: ")
        if valid(candidate):
            done = True
            candidate = int(candidate)
        else:
            print("That is not a non-negative integer.\n")
    return (2*candidate)

print("\nThe integer mutiplied by 2 is: " + str(double_integer()) + "\n")

print("-------------------------------------------------------------\n")

def alternate_case(sentence, start = 0):
    result = ""
    upper = True
    for i in range(len(sentence)):
        if i < start:
            result = result + sentence[i]
        elif upper:
            result = result + sentence[i].upper()
        else:
            result = result + sentence[i].lower()

        upper = not upper
    return result

print(alternate_case("abcdefghij"))
print(alternate_case("abcdefghij", 2))
print(alternate_case("abcdefghij", 3), "\n")

print(alternate_case("ABCDEFGHIJ"))
print(alternate_case("ABCDEFGHIJ", 3))
print(alternate_case("ABCDEFGHIJ", 4), "\n")
