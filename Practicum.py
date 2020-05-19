#---------------------------------------------------------------
# Ambrose Ryan Xavier
#---------------------------------------------------------------

import statistics

def question_01():
    L01 = [1, 2]
    print("The median of the list is " + str(statistics.median(L01)) + ".")
    print("The low median of the list is " + str(statistics.median_low(L01)) + "." + "\n")

question_01()

CC01 = ["Being", "of", "sound", "mind", "and", "body"]

def count_characters(CC01):
    morse = 0
    for i in range(len(CC01)):
        for char in CC01[i]:
            morse += 1
    return morse

print("The total number of characters contained in all strings is " + str(count_characters(CC01)) + "." + "\n")

def my_reverse(CC01):
    CC02 = []
    for i in range(len(CC01)):
        CC02.append(CC01[len(CC01) - (i+1)])
    return CC02

print("The list known as CC01 is represented in reverse as " + str(my_reverse(CC01)) + "." + "\n")

def create_file(file_name, n):

    output_file = open(file_name, "w")
    
    for i in range(n):
        if i == (n-1):
            output_file.write(str(i+1))
        else:
            output_file.write(str(i+1) + "\n")
    
    output_file.close()

create_file("test.out", 5)

import turtle

def bobcat_line(my_turtle, segment_number, length):
    
    for i in range(segment_number):
        if i % 2 == 0:
            my_turtle.color("blue")
        else:
            my_turtle.color("gold")
        my_turtle.forward(length)

drawing_turtle = turtle.Turtle()
drawing_turtle.width(3)
drawing_turtle.hideturtle()

number_of_segments = 7
segment_length = 45

bobcat_line(drawing_turtle, number_of_segments, segment_length)

scores = [0, 31, 27, 31, 49, 21, 17, 25]
victories = 0
defeats = 0

while scores != []:
    if scores[0] > scores[1]: # Copare MSU score to opponent score.
        victories += 1
    else:
        defeats += 1

    scores = scores[2:]

print("MSU has", victories, "triumph(s) and", defeats, "defeat(s).\n")

scores = [0, 31, 27, 31, 49, 21, 17, 25]
victories = 0
defeats = 0

for i in range(0, len(scores), 2):
    if scores[i] > scores[i+1]:
        victories += 1
    else:
        defeats += 1

print("MSU has", victories, "triumph(s) and", defeats, "defeat(s).\n")

print("Question 01 (25 Points)")
print("----------------------------------------------------------------------------\n")
print("Supply the missing function so that when the code runs, the following output")
print("is produced:\n")
print("The Duffer Brothers directed 6 episodes")
print("Shawn Levy directed 2 episodes")
print("Keri Cobb directed 0 episodes\n")

print("The following output is the actual output:\n")

stranger_things = {}
stranger_things["The Vanishing of Will Byers"] = "The Duffer Brothers"
stranger_things["The Weirdo on Maple Street"] = "The Duffer Brothers"
stranger_things["Holly, Jolly"] = "Shawn Levy"
stranger_things["The Body"] = "Shawn Levy"
stranger_things["The Flea and the Acrobat"] = "The Duffer Brothers"
stranger_things["The Monster"] = "The Duffer Brothers"
stranger_things["The Bathtub"] = "The Duffer Brothers"
stranger_things["The Upside Down"] = "The Duffer Brothers"

def episodes_directed(stranger_things, directors):
    series = stranger_things.values()
    count = 0
    for i in series:
        if directors == i:
            count += 1
    print(directors + " directed " + str(count) + " episodes ")

episodes_directed(stranger_things, "The Duffer Brothers")
episodes_directed(stranger_things, "Shawn Levy")
episodes_directed(stranger_things, "Keri Cobb")

print("\n----------------------------------------------------------------------------\n")

# Question 02 (50 Points)

print("Question 02 (50 Points)")
print("---------------------------------------------------------------------------------\n")
print("Supply the missing class and methods so that when this code runs, the following")
print("output is produced:\n")
print("Stranger Things has aired 8 episodes over 1 seasons.")
print("Stranger Things has aired 17 episodes over 2 seasons.\n")

print("The following output is the actual output:\n")

# "Stranger Things" is the title of the series.
# "The Duffer Brothers" is the creator of the series.
# 1 is the number of seasons that the that the series has run.
# 8 is the number of episodes that the series contains.

class Series():

    def __init__(self, name, directors, number_seasons, number_episodes):

        self.name = name
        self.directors = directors
        self.number_seasons = number_seasons
        self.number_episodes = number_episodes

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_directors(self):
        return self.directors

    def get_number_seasons(self):
        return self.number_seasons

    def set_number_seasons(self, number_seasons):
        self.number_seasons = number_seasons

    def get_number_episodes(self):
        return self.number_episodes

    def set_number_episodes(self, number_episodes):
        self.number_episodes = number_episodes

    def addSeason(self):
        self.number_seasons = self.number_seasons + 1

    def addEpisodes(self, addition):
        self.number_episodes = self.number_episodes + addition

    def __str__(self):
        return self.name + "has aired " + str(self.number_episodes) + " episodes over " + str(self.number_seasons) + " seasons."

stranger_things = Series("Stranger Things", "The Duffer Brothers", 1, 8)

print(stranger_things)
stranger_things.addSeason() # Here comes the next season.
stranger_things.addEpisodes(9) # There are now 9 more episodes.
print(stranger_things)

print("-----------------------------------------------------------------------------------------\n")

# Question 03 (25 Points)

print("Question 03 (25 Points)")
print("-----------------------------------------------------------------------------------------\n")
print("(Question 03, Part A) What is the name of the constructor method in a class?\n")
print("Answer: The name of the constructor method utilized in a class is the initializer method.")
print("The initializer method is a special method in Python (called __init__) that is invoked")
print("automatically to set the attributes of a newly-created object to their initial state.\n")

print("-----------------------------------------------------------------------------------------\n")
print("(Question 03, Part B) Suppose that class Athlete is already defined and we seek to define a")
print("new class called Runner that is a subclass of Athlete. Define the Runner subclass.\n")

# To answer this question, this part of the program adapts the "Dungeons" program for athletics (track and field).

import random

class Athlete:

    def __init__(self, name, age, height, weight):

        self.event = "Generic Athlete"
        self.strength = random.randrange(1, 10)
        self.speed = random.randrange(1, 10)
        self.agility = random.randrange(1, 10)
        self.coordination = random.randrange(1, 10)
        self.endurance = random.randrange(1, 10)
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_strength(self):
        return self.strength

    def get_speed(self):
        return self.speed

    def get_agility(self):
        return self.agility

    def get_coordination(self):
        return self.coordination

    def get_endurance(self):
        return self.endurance

    def set_strength(self, strength):
        self.strength = strength

    def set_speed(self, speed):
        self.speed = speed

    def set_agility(self, agility):
        self.agility = agility

    def set_coordination(self, coordination):
        self.coordination = coordination

    def set_endurance(self, endurance):
        self.endurance = endurance

    def __str__(self):

        answer = "Name: " + self.name + "\n"
        answer += "Event: " + self.event + "\n"
        answer += "Age: " + str(self.age) + "\n"
        answer += "Height: " + str(self.height) + " inches\n"
        answer += "Weight: " + str(self.weight) + " lbs\n"
        answer += "Strength: " + str(self.strength) + "\n"
        answer += "Speed: " + str(self.speed) + "\n"
        answer += "Agility: " + str(self.agility) + "\n"
        answer += "Coordination: " + str(self.coordination) + "\n"
        answer += "Endurance: " + str(self.endurance) + "\n"
        return answer

class Runner(Athlete):

    def __init__(self, name, age, height, weight):

        Athlete.__init__(self, name, age, height, weight)
        self.event = "Runner"
        self.set_strength(self.get_strength() - 2)
        self.set_speed(self.get_speed() + 2)
        self.set_endurance(self.get_endurance() + 2)

class Thrower(Athlete):

    def __init__(self, name, age, height, weight):

        Athlete.__init__(self, name, age, height, weight)
        self.event = "Thrower"
        self.set_strength(self.get_strength() + 2)
        self.set_agility(self.get_agility() + 2)
        self.set_coordination(self.get_coordination() + 2)

def main():
    name = input("Enter name: ")
    name = name.capitalize()
    age = input("Enter age: ")
    height = input("Enter height in inches: ")
    weight = input("Enter weight in pounds: ")
    event = input("Enter event (runner or thrower): ")
    event = event.lower()
    print()

    if (event == "runner"):
        competitor = Runner(name, age, height, weight)
        print(competitor)

    elif (event == "thrower"):
        competitor = Thrower(name, age, height, weight)
        print(competitor)

    else:
        print("Illegal Event Type.")

main()

print("-----------------------------------------------------------------------------------------\n")

print("(Question 03, Part C)")
print("-----------------------------------------------------------------------------------------\n")
print("In the context of the Athlete class, give a concrete example of the difference between")
print("an instance and an instance variable.\n")

print("Answer: An instance is an object whose type is of some class. If the main class is Athlete,")
print("then the Athlete class is the instance itself and 'name = Ryan' is the instance variable.\n")

print("-----------------------------------------------------------------------------------------\n")

print("(Question 03, Part D)")
print("-----------------------------------------------------------------------------------------------\n")
print("Describe briefly the difference between a reader method and a writer method.\n")
print("Answer: A reader method reads the entire content of a file as a string. This is often")
print("utilized in an assignment statement so that a variable can reference the contents of the file.")
print("A writer methods adds characters to the end of a file that has been opened for writing.\n")
print("-----------------------------------------------------------------------------------------------\n")

print("(Question 03, Part E)")
print("-----------------------------------------------------------------------------------------------\n")
print("To override the + operator, an __add__ method can be defined in a class. What method must be")
print("defined to override the ** operator?\n")

print("Answer: To override the ** method, a __pow__ method must be defined in the class. For example, in")
print("the Athlete class, it would be defined as Athlete.__pow__(a, b), which is expected to return")
print("a ** b for a and b numbers.")
print("-----------------------------------------------------------------------------------------------\n")

score_differences = {}
score_differences["October 7, 2017"] = 8
score_differences["October 14, 2017"] = -12
score_differences["October 21, 2017"] = 3

victories = 0
defeats = 0

for differential in score_differences.values():
    if (differential > 0):
        victories += 1
    else:
        defeats += 1

print(victories, "victories -", defeats, "defeat(s)\n")

class Appliance:

    def __init__(self, manufacturer, refrigerant):
        self.manufacturer = manufacturer
        self.refrigerator = refrigerant

    def get_manufacturer(self):
        return self.manufacturer

    def get_refrigerant(self):
        return self.refrigerant

class Refrigerator(Appliance):
    
    def __init__(self, manufacturer, refrigerant):

        Appliance.__init__(self, manufacturer, refrigerant)
        self.manufacturer = "Samsung"
        self.refrigerant = "R134a" #R134a is the refrigerant utilized.

    def __str__(self):
        return "The " + str(self.manufacturer) + " refrigerator contains refrigerant " + str(self.refrigerant)

my_refrigerator = Refrigerator("Samsung", "R134a")
print(str(my_refrigerator) + ".\n")

class Appliance:
    
    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

class Refrigerator(Appliance):

    def __init__(self, manufacturer, coolant):
        Appliance.__init__(self, manufacturer)
        self.coolant = coolant

    def __str__(self):
        result = "The " + self.manufacturer + \
                 " refrigerator contains refrigerant " + self.coolant
        return result

my_refrigerator = Refrigerator("Samsung", "R134a")
print(str(my_refrigerator) + ".\n")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numbers = np.empty([4, 4], dtype="int64")
for row in range(4):
    for col in range(4):
        numbers[row][col] = row + col

print(str(numbers) + "\n")

some_variable = numbers
print(str(type(some_variable)) + "\n")

some_variable = numbers[2][3]
print(str(some_variable.dtype) + "\n")

number = int(input("Enter an integer: "))
numbers = np.arange(number*number).reshape(number, number)
print(str(numbers) + "\n")

tictactoe = np.array([["x", "x", "o"],["o", "o", "x"],["x","x","o"]])
print(str(tictactoe) + "\n")
print(str(tictactoe[:,1]) + "\n")

victories = pd.read_csv("warriors.csv")
print(str(victories) + "\n")

victories["Percentage"] = (victories["Victories"] / 82) * 100

plt.figure("NBA Analysis")
plt.title("Golden State Warriors")

plt.xlim([1999, 2017])
plt.ylim([0, 100])
plt.xticks(np.arange(2000, 2017, 5))
plt.xlabel("Year")
plt.ylabel("Victory Percentage")
plt.plot(victories["Year"], victories["Percentage"], "b--")
plt.plot(victories["Year"], victories["Percentage"], "rd")
plt.show()

import pandas as pd

units = ["Chemical and Biological Engineering", "Civil Engineering", "Computer Engineering",
         "General Engineering", "Mechanical and Industrial Engineering", "School of Computing"]

enrollments = [563, 731, 410, 210, 1463, 552] # 536 Students in Chemial and Biological Engineering, etc.

dataset = list(zip(units, enrollments))
dataframe = pd.DataFrame(data=dataset, columns=["Unit", "Enrollment"])

sorted_dataframe = dataframe.sort_values(["Enrollment"], ascending=True)
print(sorted_dataframe[2::1], "\n")

import numpy as np
import matplotlib.pyplot as plt

units = ["CS", "ChBE", "Civil", "M&IE", "General", "CpE"]
enrollments = [552, 563, 731, 1463, 210, 410]

plt.figure("COE Enrollment Visualizations")
plt.title("Pie Chart of COE Enrollments")
plt.pie(enrollments, labels=units, autopct = "%1.1f%%", shadow=False)
plt.show()

import numpy as np

class Course:
    def __init__(self, rubric, number):
        self.rubric = rubric
        self.number = number

    def __str__(self):
        return self.rubric + "" + str(self.number)

class Course_Schedule:

    def __init__(self, my_courses):
        self.my_courses = my_courses

    def get_my_courses(self):
        return self.my_courses
    
    def set_my_courses(self, my_courses):
        self.my_courses = my_courses

    def print_function():
        print("My Schedule")
        print("-----------")

    def add(self, my_courses):
        result = Course_Schedule(my_courses)
        return result

def main():
    my_courses = Course_Schedule(3)
    course_1 = Course("CSCI", 127)
    my_courses.add(course_1)
    course_2 = Course("M", 171)
    my_courses.add(course_2)
    course_3 = Course("WRIT", 101)
    my_courses.add(course_3)
    print(my_courses)

main()
