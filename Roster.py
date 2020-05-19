#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------
# [i+1] Represents Numerical Placement
# character[0] Represents Character Name
# character[1] Represents Alter Ego Name
# character[2] Represents Publisher Name
#-----------------------------------------------------------------------
# Data Generation Template
#-----------------------------------------------------------------------
# 01, Black Panther, Bashenga, Marvel Comics
# 02, Dark Knight, Bruce Wayne, DC Comics
#-----------------------------------------------------------------------
# 03, Gladiator Spider, Peter Benjamin Parker, Marvel Comics
# 04, Ghost Spider, Gwendolyne Maxine Stacy, Marvel Comics
#-----------------------------------------------------------------------
# 05, Hammerhead, Joseph Martel, Marvel Comics
# 06, Silver Sable, Sable Manfredi, Marvel Comics
#-----------------------------------------------------------------------
# 07, Tombstone, Wilson Grant Fisk, Marvel Comics
# 08, Lizard, Curtis Connors, Marvel Comics
#-----------------------------------------------------------------------
# 09, Doctor Octopus, Otto Gunther Octavius, Marvel Comics
# 10, Vulture, Adrian Thomas, Marvel Comics
# 11, Electro, Maxwell Dillon, Marvel Comics
# 12, Sandman, Flint Harlow, Marvel Comics
# 13, Rhino, Alexander Hirsch, Marvel Comics
# 14, Apex Hunter, Sergei Nikolaevich Orlov, Marvel Comics
#-----------------------------------------------------------------------
# 15, Shocker, Jackson Whitaker Brice, Marvel Comics
# 16, Ricochet, Daniel Brigham, Marvel Comics
# 17, Matador, Ramon Gutierrez, Marvel Comics
#-----------------------------------------------------------------------
# 18, Chameleon, Dmitri Anatoly Nikolaevich Orlov, Marvel Comics
# 19, Spellbinder, Quentin Beck, Marvel Comics
# 20, Tinkerer, Phineas Mason, Marvel Comics
#-----------------------------------------------------------------------
# 21, Black Cat, Felicia Sara Hardy, Earth-26496
# 22, Cat Burglar, Walter Hardy, Earth-26496
#-----------------------------------------------------------------------
# 23, Magma Armor, Marcos Alvarado, Earth-26496
# 24, Scorpion, Drago Novak, Earth-26496
# 25, Colonel Jupiter, John Jonah Jameson, Earth-26496
#-----------------------------------------------------------------------
# 26, Hobgoblin, Roderick Kingsley, Earth-26496
# 27, Carnage, Cletus Cassidy, Earth-26496
#-----------------------------------------------------------------------
# 28, Venom, Edward Charles Allan Brock, Earth-26496
# 29, Green Goblin, Norman Virgil Osborn, Earth-26496
#-----------------------------------------------------------------------
# [Earth-26496]: Jonathon Jonah Jameson, Joseph Robertson
# [Earth-26496]: Elizabeth Brant, Edward Lau, Benjamin Ulrich
#-----------------------------------------------------------------------
# [Earth-26496]: Harold Osborn, Elizabeth Alvarado
# [Earth-26496]: Eugene Thompson, Jade Nguyen
# [Earth-26496]: Randolph Robertson, Sarah Avril
# [Earth-26496]: Kenneth Kong, Glory Grant
# [Earth-26496]: Hobart Brown, Mary Jane Watson
#-----------------------------------------------------------------------
# [Earth-26496]: Alistair Alphonso Smythe, Miles Warren
# [Earth-26496]: Henry Oliver Thornton, Donald Menken
# [Earth-46496]: Silvio Manfredi, Morgan Michaels
#-----------------------------------------------------------------------
# [Earth-26496]: Jefferson Davis, Aaron Warren
# [Earth-26496]: James Smith, Saint-John Devereaux
# [Earth-26496]: Jean DeWolff, Stanley Carter
# [Earth-26496]: George Stacy, Yuriko Watanabe
# [Earth-26496]: Vincent Gonzalez, Miguel Morales
#-----------------------------------------------------------------------

import string

def entry(characters, i):
    profile = ("Number: " + str(i+1) + ", Name: " + str(characters[0])
               + ", Alter Ego: " + str(characters[1]) + ", Publisher: "
               + str(characters[2]))
    return profile

def printMenu():
    print("1. Print the Luminary Roster\n" +
          "2. Find Graphic Novel Character by Name\n" +
          "3. Find Graphic Novel Character by Number\n" +
          "4. Print Number of Graphic Novel Characters\n" +
          "5. Terminate Program\n")

def CharacterRoster(characterRoster):
    print("\nCharacter Roster")
    print("------------------")
    for i in range(len(characterRoster)):
        characters = characterRoster[i+1]
        print(entry(characters, i))
    print("----------------------")
    print("\nEnd Character Roster\n")

def FindByName(characterRoster, name):
    nameFound = False
    for i in range(len(characterRoster)):
        characters = characterRoster[i+1]
        if name.upper() == characters[0].upper():
            nameFound = True
            print("\n" + entry(characters, i) + "\n")
    if nameFound == False:
        print("The graphic novel character named "
              + str(name) + " is not on this roster.\n")

def FindByNumber(characterRoster, number):
    while isinstance(number, str):
        number = int(input("Enter a Rank Number: "))
        if 0 < number <= len(characterRoster):
            characters = characterRoster[number]
            print("\n" + entry(characters, number-1) + "\n")
        elif isinstance(number, int):
            print("\nError: The graphic novel character ranked at number "
                  + str(number) " is not on this list.\n")

def RosterCount(characterRoster):
    print("\nThere are " + str(len(characterRoster))
          + " graphic novel characters on this list.\n")

def CreateCharacterRoster(filename):
    characterRoster = {}
    file = open(filename, "r")
    for characters in file:
        charactersRank = characters.strip().split(",")
        index = int(charactersRank.pop(0))
        characterRoster[index] = [charactersRank.pop(0).lstrip()] # Name
        characterRoster[index] += [charactersRank.pop(0)] # Alter Ego
        characterRoster[index] += [charactersRank.pop(0)] # Publisher
    file.close()
    return characterRoster

def ObtainChoice(low, high, message):
    legalChoice = False
    while not legalChoice:
        legalChoice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legalChoice = False
                print("That is not a number. Reattempt.")
                break
            if legalChoice:
                answer = int(answer)
                if (answer < low) or (answer > high):
                    legalChoice = False
                    print("That is not a valid choice. Please Reattempt.")
    return answer

def main():
    characterRoster = CreateCharacterRoster("roster.txt")
    choice = 0
    while choice != 5:
        printMenu()
        choice = ObtainChoice(1, 5, "Enter a Menu Option: ")
        if choice == 1:
            CharacterRoster(characterRoster)
        elif choice == 2:
            name = input("Enter a Graphic Novel Character Name: ")
            FindByName(characterRoster, name)
        elif choice == 3:
            number = ObtainChoice(1, 100, "Enter a Character Rank: ")
            FindByNumber(characterRoster, number)
        elif choice == 4:
            RosterCount(characterRoster)
    print("Merci. Au Revoir.\n")

main()
