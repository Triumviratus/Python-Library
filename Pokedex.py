#---------------------------------------------------------------
# Ambrose Ryan Xavier
#---------------------------------------------------------------
# Data Generation Template
#---------------------------------------------------------------
# 1, Charizard, 534, Fire, Flying
# 2, Alakazam, 500, Psychic
# 3, Gengar, 500, Ghost, Poison
# 4, Gyarados, 540, Water, Flying
# 5, Lapras, 535, Water, Ice
# 6, Articuno, 580, Ice, Flying
# 7, Zapdos, 580, Electric, Flying
# 8, Moltres, 580, Fire, Flying
# 9, Dragonite, 600, Dragon, Flying
#---------------------------------------------------------------
# 10, Mewtwo, 680, Psychic
# 11, Mew, 600, Psychic
#---------------------------------------------------------------
# 12, Feraligatr, 530, Water
# 13, Lanturn, 460, Water, Electric
# 14, Steelix, 510, Steel, Ground
# 15, Heracross, 500, Bug, Fighting
# 16, Scizor, 500, Bug, Steel
# 17, Magcargo, 430, Fire, Rock
# 18, Octillery, 480, Water
# 19, Skarmory, 465, Steel, Flying
# 20, Houndoom, 500, Dark, Fire
# 21, Kingdra, 540, Water, Dragon
# 22, Donphan, 500, Ground
# 23, Raikou, 580, Electric
# 24, Entei, 580, Fire
# 25, Suicune, 580, Water
# 26, Tyranitar, 600, Rock, Dark
# 27, Lugia, 680, Psychic, Flying
#---------------------------------------------------------------
# 28, Sceptile, 530, Grass
# 29, Blaziken, 530, Fire, Fighting
# 30, Swampert, 535, Water, Ground
# 31, Gardevoir, 518, Psychic, Fairy
# 32, Breloom, 460, Grass, Fighting
# 33, Aggron, 530, Steel, Rock
# 34, Milotic, 540, Water
# 35, Glalie, 480, Ice
# 36, Walrein, 530, Ice, Water
# 37, Salamence, 600, Dragon, Flying
# 38, Flygon, 520, Ground, Dragon
# 39, Metagross, 600, Steel, Psychic
# 40, Regirock, 580, Rock
# 41, Regice, 580, Ice
# 42, Registeel, 580, Steel
# 43, Latias, 600, Dragon, Psychic
# 44, Latios, 600, Dragon, Psychic
# 45, Kyogre, 670, Water
# 46, Groudon, 670, Ground
# 47, Rayquaza, 600, Dragon, Flying
# 48, Jirachi, 600, Steel, Psychic
# 49, Deoxys, 600, Psychic
#---------------------------------------------------------------
# 50, Torterra, 525, Grass, Ground
# 51, Infernape, 534, Fire, Fighting
# 52, Empoleon, 530, Water, Steel
# 53, Staraptor, 485, Normal, Flying
# 54, Luxray, 523, Electric
# 55, Rampardos, 495, Rock
# 56, Bastiodon, 495, Rock, Steel
# 57, Honchkrow, 505, Dark, Flying
# 58, Bronzong, 500, Steel, Psychic
# 59, Garchomp, 600, Dragon, Ground
# 60, Lucario, 525, Fighting, Steel
# 61, Hippowdon, 525, Ground
# 62, Drapion, 500, Poison, Dark
# 63, Rhyperior, 535, Ground, Rock
# 64, Electivire, 540, Electric
# 65, Magmortar, 540, Fire
# 66, Gliscor, 510, Ground, Flying
# 67, Gallade, 518, Psychic, Fighting
# 68, Frosslass, 480, Ice, Ghost
# 69, Rotom, 440, Electric, Ghost
# 70, Palkia, 680, Water, Dragon
# 71, Dialga, 680, Steel, Dragon
# 72, Heatran, 600, Fire, Steel
# 73, Regigigas, 670, Normal
# 74, Giratina, 580, Ghost, Dragon
# 75, Darkrai, 600, Dark
# 76, Arceus, 720, Normal
#---------------------------------------------------------------
# 77, Serperior, 528, Grass
# 78, Emboar, 528, Fire, Fighting
# 79, Samurott, 528, Water
# 80, Zebstrika, 497, Electric
# 81, Galvantula, 427, Bug, Electric
# 82, Eelektross, 415, Electric
# 83, Chandelure, 520, Ghost, Fire
# 84, Cryogonal, 515, Ice
# 85, Bisharp, 490, Dark, Steel
# 86, Haxorus, 540, Dragon
# 87, Hydreigon, 600, Dark, Dragon
# 88, Volcarona, 550, Bug, Fire
# 89, Cobalion, 580, Steel, Fighting
# 90, Terrakion, 580, Rock, Fighting
# 91, Virizion, 580, Grass, Fighting
# 92, Tornadus, 580, Flying
# 93, Thundurus, 580, Electric, Flying
# 94, Landorus, 600, Ground, Flying
# 95, Reshiram, 680, Dragon, Fire
# 96, Zekrom, 680, Dragon, Electric
# 97, Kyurem, 660, Dragon, Ice
# 98, Genesect, 600, Bug, Steel
# 99, Seismitoad, 509, Water, Ground
#---------------------------------------------------------------
# 100, Aegislash, 520, Steel, Ghost
# 101, Malamar, 482, Dark, Psychic
# 102, Hawlucha, 500, Fighting, Flying
# 103, Noivern, 535, Flying, Dragon
# 104, Yveltal, 680, Dark, Flying
# 105, Zygarde, 600, Dragon, Ground
# 106, Volcanion, 600, Fire, Water
#---------------------------------------------------------------
# 107, Lycanroc, 487, Rock
# 108, Xurkitree, 570, Electric
# 109, Celesteela, 570, Steel, Flying
# 110, Kartana, 570, Grass, Steel
# 111, Guzzlord, 570, Dark, Dragon
# 112, Marshadow, 600, Fighting, Ghost
# 113, Naganadel, 540, Poison, Dragon
# 114, Zeraora, 600, Electric
#---------------------------------------------------------------
# 115, Rillaboom, 530, Grass
# 116, Cinderace, 530, Fire
# 117, Inteleon, 530, Water
# 118, Corviknight, 495, Flying, Steel
# 119, Sandaconda, 510, Ground
# 120, Centiskorch, 525, Fire, Bug
# 121, Duraludon, 535, Steel, Dragon
# 122, Dragapult, 600, Dragon, Ghost
# 123, Zamazenta, 720, Fighting, Steel
# 124, Eternatus, 690, Poison, Dragon
#---------------------------------------------------------------

import string

def entry(pokemon, i):

    details = "Number: " + str(i+1) + ", Name: " + str(pokemon[0]) + ", CS: " + str(pokemon[1])
    classification = ", Type: " + str(pokemon[2])
    if len(pokemon) > 3:
        classification += " and " + pokemon[3]
    profile = details + classification
    return profile

# The purpose of the entry function is to outline the other essential functions
# with a more succicnt snippet of code to carry out those essential functions.

def printMenu():
    print("1. Print Pokedex\n" +
          "2. Lookup Pokemon by Name\n" +
          "3. Lookup Pokemon by Number\n" +
          "4. Print Number of Pokemon\n" +
          "5. Print Total Cumulative Statistics of All Pokemon\n" +
          "6. Terminate Program\n")

def printPokedex(pokedex):
    print("\nThe Pokedex")
    print("-----------")
    for i in range(len(pokedex)):
        pokemon = pokedex[i+1]
        print(entry(pokemon, i))
    print("\nEnd Pokedex\n")

def lookupByName(pokedex, name):
    nameFound = False
    for i in range(len(pokedex)):
        pokemon = pokedex[i+1]
        if name == pokemon[0]:
            nameFound = True
            print(entry(pokemon, i) + "\n")
    if nameFound == False:
        print("The pokemon named " + str(name) + " does not exist\n")

def lookupByNumber(pokedex, number):
    while isinstance(number, str):
        number = int(input("Enter a Pokemon Number: "))
    if 0 < number <= len(pokedex):
        pokemon = pokedex[number]
        print(entry(pokemon, number-1) + "\n")
    elif isinstance(number, int):
        print("Error: Pokemon " + str(number) + " does not exist.\n")

def howManyPokemon(pokedex):
    print("There are " + str(len(pokedex)) + " different Pokemon.\n")

def howManyCS(pokedex):
    CStotal = 0
    for i in range(len(pokedex)):
        pokemon = pokedex[i+1]
        CStotal = CStotal + pokemon[1]
    print("The total number of cumulative statistics for all Pokemon is " + str(CStotal) + "\n")

#-------------------------------------------------------------------------------------------------------

def createPokedex(filename):
    pokedex = {}
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        pokedex[index] = [pokelist.pop(0)] # Name
        pokedex[index] += [int(pokelist.pop(0))] # Cumulative Statistics (CS)
        pokedex[index] += [pokelist.pop(0)] # Type
        if len(pokelist) == 1:
            pokedex[index] += [pokelist.pop(0)] # Optional Second Type

    file.close()
    return pokedex

#--------------------------------------------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number. Reattempt.")
                break
            if legal_choice:
                answer = int(answer)
                if (answer < low) or (answer > high):
                    legal_choice = False
                    print("That is not a valid choice. Reattempt.")
    return answer

#--------------------------------------------------------------------------

def main():
    pokedex = createPokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        printMenu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:
            printPokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon Name: ")
            name = name.capitalize()
            lookupByName(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon Number: ")
            lookupByNumber(pokedex, number)
        elif choice == 4:
            howManyPokemon(pokedex)
        elif choice == 5:
            howManyCS(pokedex)
    print("\nMerci. Au Revoir.\n")

#--------------------------------------------------------------------------

main()
