#---------------------------------------------------------------
# Ambrose Ryan Xavier
#---------------------------------------------------------------
# Data Generation Template
#---------------------------------------------------------------
# 5
# Cody,Bellinger,1B
# Yasiel,Puig,RF
# Corey,Seager,SS
# Chris,Taylor,CF
# Justin,Turner,3B
# Chris,Taylor,10-28-2017,4,1
# Corey,Seager,10-28-2017,4,1
# Justin,Turner,10-28-2017,3,0
# Cody,Bellinger,10-28-2017,4,2
# Chris,Taylor,10-27-2017,3,0
# Corey,Seager,10-27-2017,3,1
# Justin,Turner,10-27-2017,4,1
# Cody,Bellinger,10-27-2017,4,0
# Chris,Taylor,10-25-2017,3,1
# Corey,Seager,10-25-2017,5,1
# Justin,Turner,10-25-2017,5,0
# Cody,Bellinger, 10-25-2017,4,0
# Chris,Taylor,10-24-2017,3,1
# Corey,Seager,10-24-2017,3,2
# Justin,Turner,10-24-2017,4,1
# Cody,Bellinger,10-24-2017,3,0
# Austin,Barnes,10-27-2017,2,0
# Yasiel,Puig,10-24-2017,3,0
# Yasiel,Puig,10-25-2017,5,1
# Yasiel,Puig,10-26-2017,4,1
# Yasiel,Puig,10-27-2017,4,0
#---------------------------------------------------------------

import numpy as np

#-------------------------------------
class Person:
    """Person class for representing first and last names of the players"""
    def __init__(self, first_name, last_name):
        """A constructor method that retrieves the first and last name of the players"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def get_first_name(self):
        """A reader method that returns the first name"""
        return self.first_name

    def get_last_name(self):
        """A reader method that returns the last name"""
        return self.last_name
    
#-------------------------------------

class Batter(Person):
    """Batter subclass for representing the Person as a Battter"""
    def __init__(self, first_name, last_name, position):
        """A constructor method that retrieves the variables for a batter at home base"""
        Person.__init__(self, first_name, last_name)
        self.position = position
        self.at_bats = 0
        self.hits = 0

    def get_position(self):
        """A reader method that returns the position"""
        return self.position

    def get_at_bats(self):
        """A reader method that returns the at-bats"""
        return self.at_bats

    def get_hits(self):
        """A reader method that returns the hits"""
        return self.hits

    def batting_average(self):
        """A method that calculates the batting average"""
        if self.at_bats == 0:
            return "0.000"
        else:
            return round((self.hits / self.at_bats), 3)

    def add_hits(self, hits):
        """A method to add hits to the data analysis"""
        self.hits += int(hits)

    def add_at_bats(self, at_bats):
        """A method to add at_bats to the data analysis"""
        self.at_bats += int(at_bats)

    def update(self, at_bats, hits):
        """A method that updates the specific objects"""
        self.add_hits(hits)
        self.add_at_bats(at_bats)
    
    def __str__(self):
        """Convert object to a string"""
        name = self.first_name + " " + self.last_name + "(" + self.position + ")"
        average = str(self.batting_average()) + " (" + str(self.hits) + " for " + str(self.at_bats) + ")"
        return name + average.rjust(40 - len(name))

#-------------------------------------

class All_Batters:
    """A class to take into account all the batters in the data set"""
    def __init__(self, batters):
        """A reader method that retrieves the variables for all the batters"""
        self.batters = batters

    def get_batters(self):
        """A reader method that returns the players"""
        return self.batters

    def __str__(self):
        """Convert object to a string"""
        header01 = "Player                   Batting Average\n"
        header02 = "----------------------------------------"
        return header01 + header02

#-------------------------------------

def main(file_name):
    
    file = open(file_name, "r")

    length_file = 0
    for line in file:
        length_file += 1
    
    file.close()
    
    # The length_file function is utilized to extrapolate the right
    # information from the length of the input file.
    
    file = open(file_name, "r")
    players = int(file.readline())

    pennant = np.ndarray(shape=players, dtype=Batter)
    batters = All_Batters(pennant) # This implements the batters instance variable
                                   # as a NumPy array.
    index = 0
    print(batters) # This prints the header the first time.
    
    for line in range(players):
        
        player = file.readline().split(",")
        
        first_name = player[0]
        last_name = player[1]
        position = player[2]
        
        batter = Batter(player[0], player[1], player[2].rstrip())
        pennant[index] = batter
        index += 1
        print(batter)

    print("\n" + str(batters)) # This prints the header the second time.

    for line in range(length_file - players):

        player = file.readline().split(",")
        
        for batter in pennant: # This for loop within the for loop
                               # updates the required information.
            if player[0] == batter.get_first_name():
                if player[1] == batter.get_last_name():
                    batter.update(player[3], player[4])

    for batter in pennant: # This for loop prints the remaining pieces of information.
        print(batter)

main("batting.txt")
