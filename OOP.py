#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------

print()

class Date:
    """Date Class for Representing and Manipulating Calendar Dates"""

    def __init__(self, day, month, year):
        """A constructor method that sets the month, day, and year"""
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        """A reader method that returns the day"""
        return self.day

    def get_month(self):
        """A reader method that returns the month"""
        return self.month

    def get_year(self):
        """A reader method that returns the year"""
        return self.year

    def set_day(self, day):
        """A writer method that sets the day"""
        self.day = day

# Create an instance of the [Date] class with the value 16 September 1995
today = Date(16, "September", 1995)
print("Calendar Date: ", today.get_day(), today.get_month(), today.get_year())

# Update the instance to be one day later
day = today.get_day()
today.set_day(day+1)
print("Calendar Date: ", today.get_day(), today.get_month(), today.get_year())

print()

import card

def evaluate(hand):
    result = 0
    for oneCard in hand:
        result += oneCard.get_value()
    return result

def process_hand(hand):
    result = ""
    for oneCard in hand:
        result += oneCard.get_rank() + " of " + oneCard.get_suit() + ", "
    print(result[:-2], "evaluates to", evaluate(hand))

ace = card.Card("ace", "spades")
king = card.Card("king", "diamonds")
queen = card.Card("queen", "hearts")
jack = card.Card("jack", "clubs")
ten = card.Card("ten", "spades")
nine = card.Card("nine", "hearts")
eight = card.Card("eight", "diamonds")
seven = card.Card("seven", "clubs")
six = card.Card("six", "spades")
five = card.Card("five", "hearts")
four = card.Card("four", "diamonds")
three = card.Card("three", "clubs")
two = card.Card("two", "spades")

process_hand([ace, king])
process_hand([queen, ace])
process_hand([ace, jack])
process_hand([ten, ace])
process_hand([ten, ace])
process_hand([two, three, four, five, six, seven])
process_hand([eight, nine, two])

print()

import random

class Person:

    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last
    def __str__(self):
        return self.first_name + " " + self.last_name

def shuffle(persons):
    for i in range(len(persons)):
        j = random.randint(0, len(persons)-1)
        print(i, j)
        persons[i], persons[j] = persons[j], persons[i]

# Main Application
def main():
    person1 = Person("Enzo", "Ferrari")
    person2 = Person("Ferruccio", "Lamborghini")
    people = [person1, person2, Person("Ferdinand", "Porsche"),
              Person("Alfieri", "Maserati"), Person("Ettore", "Bugatti")]
    for person in people:
        print(person)

main()

print()

import random

class Card:
    """Card Class for Representing and Manipulating One Playing Card"""

    def __init__(self, rank, suit):
        """A constructor method that sets the suit and rank"""
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        """A reader method that returns the suit of the card"""
        return self.suit

    def get_rank(self):
        """A reader method that returns the rank of the card"""
        return self.rank

    def __str__(self):
        """Overrides the information utilized by the print function"""
        return "The " + self.rank + " of " + self.suit

class Deck:
    """Deck Class for Representing and Manipulating [52] Instances of the [Card] class"""

    def __init__(self):
        """A constructor method that creates a [52]-card deck"""
        self.cards = []
        for rank in ["two", "three", "four", "five", "six", "seven", "eight",
                     "nine", "ten", "jack", "queen", "king", "ace"]:
            for suit in ["clubs", "diamonds", "hearts", "spades"]:
                self.cards += [Card(rank, suit)]
    def shuffle(self):
        for i in range(len(self.cards)):
            j = random.randint(0, len(self.cards)-1)
    def print_deck(self):
        """A method that prints the [52]-card deck"""
        print("Deck of Cards")
        print("-------------")
        number = 1
        for card in self.cards:
            print(number, card)
            number += 1
        print()

cards = Deck()
cards.print_deck()
cards.shuffle()
print("After Shuffling...\n")
cards.print_deck()

print()

import random

class Character:
    """Common Base Class for Any Type of Character"""

    def __init__(self, name, age, height, weight):
        """Constructor for a New Character"""
        self.archetype = "Generic Character"
        self.intelligence = random.randrange(8, 18)
        self.strength = random.randrange(8, 18)
        self.dexterity = random.randrange(8, 18)
        self.wisdom = random.randrange(8, 18)
        self.charisma = random.randrange(8, 18)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_intelligence(self):
        """Reader method to return the intelligence of the character"""
        return (self.intelligence)

    def get_strength(self):
        """Reader method to return the strength of the character"""
        return(self.strength)
    
    def get_dexterity(self):
        """Reader method to return the dexterity of the character"""
        return(self.dexterity)

    def get_wisdom(self):
        """Reader method to return the wisdom of the character"""
        return (self.wisdom)

    def get_charisma(self):
        """Reader method to return the charisma of a character"""
        return (self.charisma)

    def set_intelligence(self, intelligence):
        """Writer method to set the intelligence of a character"""
        self.intelligence = intelligence

    def set_strength(self, strength):
        """Writer method to set the strength of a character"""
        self.strength = strength

    def set_dexterity(self, dexterity):
        """Writer method to set the dexterity of a character"""
        self.dexterity = dexterity

    def set_wisdom(self, wisdom):
        """Writer method to set the wisdom of a character"""
        self.wisdom = wisdom

    def set_charisma(self, charisma):
        """Writer method to set the charisma of a character"""
        self.charisma = charisma

    def __str__(self):
        """Override the print method for a character"""
        answer = "Name: " + self.name + "\n"
        answer += "Archetype: " + self.archetype + "\n"
        answer += "Age: " + str(self.age) + "\n"
        answer += "Height: " + str(self.height) + " Centimeters\n"
        answer += "Weight: " + str(self.weight) + " Kilograms\n"
        answer += "Intelligence: " + str(self.intelligence) + "\n"
        answer += "Strength: " + str(self.strength) + "\n"
        answer += "Dexterity: " + str(self.dexterity) + "\n"
        answer += "Wisdom: " + str(self.wisdom) + "\n"
        answer += "Charisma: " + str(self.charisma) + "\n"
        return answer

class Polymath(Character):
    """Define Polymath to be a subclass of Character"""
    def __init__(self, name, age, height, weight):
        """Constructor for a new Polymath"""
        Character.__init__(self, name, age, height, weight)
        self.race = "Polymath"
        self.set_charisma(self.get_charisma()+2)
        self.set_intelligence(self.get_intelligence()+2)

class Metahuman(Character):
    """Define Metahuman to be a subclass of Character"""
    def __init__(self, name, age, height, weight):
        """Constructor for a new Metahuman"""
        Character.__init__(self, name, age, height, weight)
        self.race = "Metahuman"
        self.set_charisma(self.get_charisma()-2)
        self.set_intelligence(self.get_intelligence()-2)
        self.set_strength(self.get_strength()+2)

class Fighter(Character):
    """Define Fighter to be a subclass of Character"""
    def __init__(self, name, age, height, weight):
        """Constructor for a new Fighter"""
        Character.__init__(self, name, age, height, weight)
        self.race = "Fighter"
        self.set_dexterity(self.get_dexterity()+2)
        self.set_wisdom(self.get_wisdom()+2)

# Main Application
def main():
    name = input("Enter Name: ")
    name = name.capitalize()
    age = input("Enter Age: ")
    height = input("Enter Height: ")
    weight = input("Enter Weight: ")
    archetype = input("Enter Archetype (Polymath, Metahuman, Fighter): ")
    archetype = archetype.lower()
    print()
    if (archetype == "metahuman"):
        player = Metahuman(name, age, height, weight)
        print(player)
    elif (archetype == "fighter"):
        player = Fighter(name, age, height, weight)
        print(player)
    elif (archetype == "polymath"):
        player = Polymath(name, age, height, weight)
        print(player)
    else:
        print ("Illegal Character Archetype")

main()

print()

class Fraction:

    def __init__(self):
        """Constructor With Default Values"""
        self.numerator = 1
        self.denominator = 1

    def __str__(self):
        """Convert Object to a String"""
        return str(self.numerator) + "/" + str(self.denominator)

    def simplify(self):
        """Utilize the [Euclidean] algorithm to simplify fractions
            via the greatest common divisor (GCD)"""
        m = self.numerator
        n = self.denominator

        while m % n != 0:
            old_m = m
            old_n = n
            m = old_n
            n = old_m % old_n

        self.numerator = self.numerator // n
        self.denominator = self.denominator // n

    def __add__(self, other_fraction):
        """Add Two Fractions"""
        result = Fraction()
        result.numerator = ((self.numerator * other_fraction.denominator)
                            + (other_fraction.numerator * self.denominator))
        denominator = (self.denominator * other_fraction.denominator)
        result.simplify()
        return result

    def utilizer_fraction(self):
        """Modify fraction with utilizer supplied values"""
        self.numerator = int(input("Enter the Numerator: "))
        self.denominator = int(input("Enter the Denominator: "))
        self.simplify()

# Print a Menu of Choices

def print_menu():
    print()
    print("1. Enter Fraction 1")
    print("2. Enter Fraction 2")
    print("3. Add Fraction 2 to Fraction 1")
    print("4. Add Fraction 1 to Fraction 2")
    print("5. Print Fraction 1")
    print("6. Print Fraction 2")
    print("7. Terminate")
    print()

# Enable the Utilize to Create a Fraction

def create_fraction(message):
    result = Fraction()
    print(message)
    result.utilizer_fraction()
    return result

# Main Application

def main():

    fraction_1 = create_fraction("Enter Fraction 1")
    fraction_2 = create_fraction("Enter Fraction 2")

    choice = 0

    while choice != 7:
        print_menu()
        choice = int(input("Enter Choice: "))
        if choice == 1:
            fraction_1.utilizer_fraction()
        elif choice == 2:
            fraction_2.utilizer_fraction()
        elif choice == 3:
            fraction_1 = fraction_1 + fraction_2
        elif choice == 4:
            fraction_2 = fraction_1 + fraction_2
        elif choice == 5:
            print(fraction_1)
        elif choice == 6:
            print(fraction_2)
        elif choice == 7:
            print("Adios")
        else:
            print("Invalid Choice. Please Attempt Again")

main()

print()
