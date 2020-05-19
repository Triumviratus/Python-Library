#---------------------------------------------------------------------
# Ambrose Ryan Xavier
#---------------------------------------------------------------------
# Data Generation Template
#---------------------------------------------------------------------
# 1, Houndoom, Flamethrower, Crunch, Sunny Day, Solar Beam
#---------------------------------------------------------------------
# 2, Salamence, Dragon Claw, Zen Headbutt, Steel Wing, Flamethrower
#---------------------------------------------------------------------
# 3, Metagross, Psychic, Meteor Mash, Hammer Arm, Magnet Rise
#---------------------------------------------------------------------
# 4, Infernape, Close Combat, Flare Blitz, Fire Punch, Thunder Punch
#---------------------------------------------------------------------
# 5, Garchomp, Earth Power, Dragon Pulse, Iron Head, Flamethrower
#---------------------------------------------------------------------
# 6, Drapion, Cross Poison, Night Slash, Dark Pulse, Ice Fang
#---------------------------------------------------------------------

import string

def entry(pokemon, i):
    profile = ("Number: " + str(i+1) + ", Name: " + str(pokemon[0])
               + ", First Move:" + str(pokemon[1]) + ", Second Move:"
               + str(pokemon[2]) + ", Third Move:" + str(pokemon[3])
               + ", Fourth Move:" + str(pokemon[4]))
    return profile

def printMenu():
    print("1. Print Dream Team\n" +
          "2. Find Pokemon by Name\n" +
          "3. Find Pokemon by Number\n" +
          "4. Print Number of Pokemon\n" +
          "5. Terminate Program\n")

def printDreamTeam(dream_team):
    print("\nDream Team")
    print("----------")
    for i in range(len(dream_team)):
        pokemon = dream_team[i+1]
        print(entry(pokemon, i))
    print("--------------")
    print("End Dream Team\n")

def Find_By_Name(dream_team, name):
    nameFound = False
    for i in range(len(dream_team)):
        pokemon = dream_team[i+1]
        if name.upper() == pokemon[0].upper():
            nameFound = True
            print("\n" + entry(pokemon, i) + "\n")
    if nameFound == False:
        print("The Pokemon named " + str(name) + " is not on this team.\n")

def Find_By_Number(dream_team, number):
    while isinstance(number, str):
        number = int(input("Enter a Team Number: "))
    if 0 < number <= len(dream_team):
        pokemon = dream_team[number]
        print("\n" + entry(pokemon, number-1) + "\n")
    elif isinstance(number, int):
        print("Error: Pokemon " + str(number) + " is not on this team.\n")

def Roster_Count(dream_team):
    print("There are " + str(len(dream_team)) + " members on the Dream Team.\n")

def createDreamTeam(filename):
    dream_team = {}
    file = open(filename, "r")

    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        index = int(pokelist.pop(0))
        dream_team[index] = [pokelist.pop(0).lstrip()] # Name
        dream_team[index] += [pokelist.pop(0)] # Move 01
        dream_team[index] += [pokelist.pop(0)] # Move 02
        dream_team[index] += [pokelist.pop(0)] # Move 03
        dream_team[index] += [pokelist.pop(0)] # Move 04

    file.close()
    return dream_team

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

def main():
    dream_team = createDreamTeam("team.txt")
    choice = 0
    while choice != 5:
        printMenu()
        choice = get_choice(1, 5, "Enter a menu option: ")
        if choice == 1:
            printDreamTeam(dream_team)
        elif choice == 2:
            name = input("Enter a Pokemon Name: ")
            Find_By_Name(dream_team, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Team Number: ")
            Find_By_Number(dream_team, number)
        elif choice == 4:
            Roster_Count(dream_team)
    print("\nMerci. Au Revoir.\n")

main()
