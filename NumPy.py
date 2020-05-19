#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------
# Data Generation Template
#----------------------------------------------------------------------------
# 1870 20595
# 1880 39159
# 1890 142294
# 1900 243329
# 1910 376053
# 1920 548889
# 1930 537606
# 1940 559456
# 1950 591024
# 1960 674767
# 1970 694409
# 1980 786690
# 1990 799065
# 2000 902195
# 2010 989415
# 2016 1042520
#----------------------------------------------------------------------------

import numpy as np
import random

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

#-------------------------------------

class Yahtzee:

    def __init__(self):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(6).roll()

    def count_outcomes(self):
        """A helper method that determines, how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(7, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_yahtzee(self):
        counts = self.count_outcomes()
        for i in range(1, 7):
            if counts[i] == 5:
                return True
        return False
    
    def is_it_full_house(self):
        counts = self.count_outcomes()
        three = False
        two = False
        for i in range(1, 7):
            if counts[i] == 3:
                three = True
            if counts[i] == 2:
                two = True
            if three == True and two == True:
                return True
        return False
    
    def is_it_large_straight(self):
        counts = self.count_outcomes()
        for i in range(2, 6):
            if counts[i] != 1:
                return False
        return True
    
#-------------------------------------

def main(how_many):
    
    yahtzees = 0
    full_houses = 0
    large_straights = 0
    game = Yahtzee()

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_yahtzee():
            yahtzees += 1
        elif game.is_it_full_house():
            full_houses += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    print("Number of Yahtzees:", yahtzees)
    print("Yahtzee Percent:", "{:.2f}%\n".format(yahtzees * 100 / how_many))
    print("Number of Full Houses:", full_houses)
    print("Full House Percent:", "{:.2f}%\n".format(full_houses * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Large Straight Percent:", "{:.2f}%\n".format(large_straights * 100 / how_many))

#-------------------------------------

main(5000)

import numpy as np
import math

def mean(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def standard_deviation(numbers):
    average = mean(numbers)
    variance = 0
    for number in numbers:
        variance += (average - number) ** 2
    variance = variance / len(numbers)
    return math.sqrt(variance)

def sort(numbers):
    for i in range(len(numbers)):
        smallest_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[smallest_index]:
                smallest_index = j
        numbers[i], numbers[smallest_index] = numbers[smallest_index], numbers[i]

shoulder_heights = np.array([600, 470, 170, 430, 300])
print("Original Array:", shoulder_heights)
print("Mean:", mean(shoulder_heights))
print("Standard Deviation:", standard_deviation(shoulder_heights))
sort(shoulder_heights)
print("Sorted Array:", shoulder_heights)

import numpy as np

a = np.array([1, 2, 3]) # Create a rank 01 array
print(type(a))          # Prints "<type 'numpy.ndarray'>"
print(a.shape)          # Prints "(3,)"
print(a[0], a[1], a[2]) # Prints "1 2 3"
a[0] = 5                # Change an element of the array
print(a)                # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 02 array
print(b.shape)                        # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])      # Prints "1 2 4"

# Creating Arrays:

a = np.zeros((2, 2))   # Create an array of all zeros
print(a)               # Prints "[[ 0.  0.]
                       #          [ 0.  0.]]"

b = np.ones((1, 2))    # Create an array of all ones
print(b)               # Prints "[[ 1.  1.]]"

c = np.full((2, 2), 7) # Create a constant array
print(c)               # Prints "[[ 7.  7.]
                       #          [ 7.  7.]]"

d = np.eye(2)          # Create a 2x2 identity matrix
print(d)               # Prints "[[ 1.  0.]
                       #          [ 0.  1.]"

e = np.random.random((2, 2)) # Create an array filled with random values
print(e)                     # Might print "[[ 0.91940167  0.08143941]
                             #               [ 0.68744134  0.87236687]]"

# Slicing:

# Create the following rank 02 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Utilize slicing to pull out the subarray consisting of the first 02 rows
# and columns 01 and 02; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
print(a[0, 1])  # Prints "2"
b[0, 0] = 77    # b[0, 0] is the same piece of data as a[0, 1]
print(a[0, 1])  # Prints "77"

# Mixing indexing and slicing:

# Create the following rank 02 array with shape (3, 4)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Two ways of accessing the data in the middle row of the array.
# Mixing integer indexing with slices yields an array of lower rank,
# while utilizing only slices yields an array of the same rank as the
# original array:

row_r1 = a[1, :]             # Rank 01 view of the second row of a
row_r2 = a[1:2, :]           # Rank 02 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape) # Prints "[5 6 7 8]] (1, 4)"

# We can formulate the same distinction when accessing columns of an array:

col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape) # Prints "[ 2 6 10] (3,)"
print(col_r2, col_r2.shape) # Prints "[[ 2]
                            #          [ 6]
                            #          [10]] (3, 1)"

# Integer Array Indexing:

a = np.array([[1, 2], [3, 4], [5, 6]])

# An example of integer array indexing.
# The returned array will have shape (3,) and
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"

# The above example of integer array indexing is equivalent to this:
print(np.array([a[0, 0], a[1, 1], a[2, 0]])) # Prints "[1 4 5]"

# When utilizing integer array indexing, you can reutilize the same
# element from the source array:
print(a[[0, 0], [1, 1]]) # Prints "[2 2]"

# Equivalent to the previous integer array indexing example
print(np.array([a[0, 1], a[0, 1]])) # Prints "[2 2]"

# Time Comparison

import time
size_of_vec = 10000000

def pure_python_version():
    start = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = []
    for i in range(len(X)):
       Z.append(X[i] + Y[i])
    return time.time() - start

def numpy_version():
    start = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.time() - start

t1 = pure_python_version()
t2 = numpy_version()
print(t1, t2)
print("Numpy is, in this example, " + str(t1/t2) + " times faster!")

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = a[1:4]
b[0] = 200
print(a[1])

m = np.array(np.random.randint(1, 100, (5, 5)))
print(m)

import turtle

import numpy as np

def draw_house(stylus, coordinates, pen_color):
    stylus.color(pen_color)
    stylus.up()
    stylus.goto(coordinates[0][0], coordinates[0][1])
    stylus.down()
    for coordinate in coordinates:
        stylus.goto(coordinate[0], coordinate[1])

def draw_neighborhood(drawing_turtle):
    drawing_turtle.hideturtle()
    coordinates = np.array([[-30, 50], [-30, -50], [70, -50], [70, 50],
                            [-30, 50], [20, 100], [70, 50]])

    draw_house(drawing_turtle, coordinates, "black")
    draw_house(drawing_turtle, coordinates + 10, "black")
    draw_house(drawing_turtle, coordinates + [-100, -200], "red")
    draw_house(drawing_turtle, coordinates * 2, "turquoise")
    draw_house(drawing_turtle, coordinates * [0.5, 0.2] + [100, 200], "blue")

window = turtle.Screen()
house_turtle = turtle.Turtle()
draw_neighborhood(house_turtle)
window.exitonclick()

# Numpy Introduction (Walkthrough) utilizing arange to attain
# evenly spaced values in an array:

import numpy as np

a = np.arange(1, 10)
print(a)

# Compare to Range:
x = range(1, 10)
print(x) # x is an iterator
print(list(x))

# Some more arange examples:
x = np.arange(10.4)
print(x)
x = np.arange(0.5, 10.4, 0.8)
print(x)
x = np.arange(0.5, 10.4, 0.8, int)
print(x)

# Another related function: linspace

# 50 values between 1 and 10:
print(np.linspace(1, 10))
# 7 values between 1 and 10:
print(np.linspace(1, 10, 7))
# Excluding the endpoint:
print(np.linspace(1, 10, 7, endpoint=False))

# Dimension of Arrays:

x = np.array(42)
print("x: ", x)
print("The type of x: ", type(x))
print("The dimension of x:", np.ndim(x))

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
V = np.array([3.4, 6.9, 99.8, 12.8])
print("F: ", F)
print("V: ", V)
print("Type of F: ", F.dtype)
print("Type of V: ", V.dtype)
print("Dimension of F: ", np.ndim(F))
print("Dimension of V: ", np.ndim(V))

A = np.array([ [3.4, 8.7, 9.9],
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])

print(A)
print(A.ndim)

# Shape of Arrays:
print(x.shape)
print(F.shape)
print(V.shape)
print(A.shape)

# Reshaping:

x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78]])

print(np.shape(x))
print(x.shape) # An equivalent array property

x.shape = (3, 6) # Reshaped
print(x)

# More on array indexing:

F = np.array([1, 1, 2, 3, 5, 8, 13, 21])
# Print the first element of F, i.e. the element with the index 0
print(F[0])
# Print the last element of F
print(F[-1])
B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])

print(B[0][1][0])

A = np.array([ [3.4, 8.7, 9.9],
               [1.1, -7.8, -0.7],
               [4.1, 12.3, 4.8]])

print(A[1][0])
print(A[1, 0]) # Equivalent Syntax

# More Slicing Examples

S = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(S[2:5])
print(S[:4])
print(S[6:])
print(S[:])

# Multidimensional Slicing

A = np.array([
    [11, 12, 13, 14, 15],
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
    [51, 52, 53, 54, 55]])

print(A[:3,2:])
print(A[3:,:])
print(A[:,4:])

X = np.arange(28).reshape(4, 7)
print(X)
print(X[::2, ::3]) # Utilizes the 'step' parameter
print(X[::, ::3])

Z = np.zeros((8, 8), dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

# Shortcuts for Array Creation:

E = np.ones((2, 3))
print(E)
F = np.ones((3, 4), dtype=int)
print(F)

Z = np.zeros((2, 4))
print(Z)

X = np.array([2, 5, 18, 14, 4])
E = np.ones_like(x)
print(E)

I = np.identity(4)
print(I)

# Broadcasting:

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x) # Create an empty matrix with the same shape as x

# Add the vector v to each row of the matrix x with an explicit loop (slow)
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)

# We will add the vector v to each row of the matrix x,
# storing the result in the matrix y
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
y = np.array([1, 0, 1])
y = x + v # Add v to each row of x by utilizing broadcasting
print(y) # Prints "[[ 2  2  4]
         #          [ 5  5  7]
         #          [ 8  8 10]
         #          [11 11 13]]"

import matplotlib.pyplot as plt
import numpy as np

#-------------------------------------

def read_file(file_name):
    """Read census data from a file"""

    years = []
    populations = []

    census_file = open(file_name, "r")
    for one_line in census_file:
        values = one_line.split()
        years.append(int(values[0]))
        populations.append(int(values[1]))
    census_file.close()

    return ([np.array(years), np.array(populations)])

#-------------------------------------

def main():
    """Main function to produce graphs"""

    years, populations = read_file("montana.txt")

    plt.figure("Historical Montana Populations") # Graph 01
    plt.plot(years, populations, "ro", years, populations, "black")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.show()

    plt.figure("Historical Montana Populations") # Graph 02
    plt.plot(years, populations, "ro", years, populations, "black")
    plt.xlabel("Year")
    plt.ylabel("Population Differential")
    plt.show()

#-------------------------------------

if __name__ == "__main__":
    main()

