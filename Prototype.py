#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------

adjective_01 = input("Enter an adjective: ")
name_01 = input("Enter a name: ")
name_02 = input("Enter a different name: ")
city_01 = input("Enter a city: ")
city_02 = input("Enter a different city: ")
adjective_02 = input("Enter a different adjective: ")

print()
print("A new and " + adjective_01 + " film will be released soon.")
print("It is about " + name_01 + ", who is on a journey of self-discovery.")
print(name_01 + " is a force of nature whose hyper-competence threatens " + name_02 + ".")
print("In response, " + name_02 + " captured the individuals that " + name_01 + " called allies.")
print(name_01 + " is forced to leave " + city_01 + " and establsih a new HQ in " + city_02 + ".")
print("However, " + name_01 + " is intercepted so that " + name_02 + " can finally achieve " + adjective_02 + " revenge.")

import turtle
import math

def drawSquare(t, sz):
    """ Force turtle t to draw a square with side sz."""
    for i in range(4):
        t.forward(sz)
        t.left(90)


def drawBar(t, height):
    """Force turtle to draw one bar, of height."""
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.write(str(height))
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

xs = [48, 117, 200, 240, 160, 260, 220]
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen() # Set up the window and its attributes
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("silver")

alexander = turtle.Turtle() # Create alexander
drawSquare(alexander, 50) # Call the function to draw the square passing
                          # the actual turtle and the actual side size.

alexander.penup()
alexander.goto(100, 100)
alexander.pendown()

drawSquare(alexander, 75) # Draw Another Square

def drawMulticolorSquare(t, sz):
    """Force turtle t to draw a multicolor square of sz."""
    for i in ["red", "purple", "gold", "blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)

alexander.color("blue")
alexander.fillcolor("red")
alexander.pensize(3)

for a in xs:
    drawBar(alexander, a)

size = 20 # Size of the smallest square

for i in range(15):
    drawMulticolorSquare(alexander, size)
    size = size + 10 # Increase the size for next time
    alexander.forward(10) # Move alexander along slightly
    alexander.right(18) # and give him some additional turn

def drawRectangle(t, w, h):
    """Manipulate turtle t to draw a rectangle of width w and height h"""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def drawSquare(tx, sz): # A new version of drawSquare
    drawRectangle(tx, sz, sz)

drawSquare(alexander, 50)

wn.exitonclick()

print(abs(5))
print(abs(-5), "\n")

print(math.pow(2, 3))
print(math.pow(7, 4), "\n")

print(max(7, 11))
print(max(4, 1, 17, 2, 12))
print(max(3*11, 5**3, 512-9, 1024**0), "\n")

def square(x):
    y = x * x
    return y

toSquare = 10
result = square(toSquare)
print("The result of", toSquare, "squared is", result, "\n")

def square(x):
    runningtotal = 0
    for counter in range(x):
        runningtotal = runningtotal + x
    return runningtotal

toSquare = 10
squareResult = square(toSquare)
print("The result of", toSquare, "squared is", squareResult, "\n")

def pow(b, p):
    y = b ** p
    return y

def square(x):
    a = pow(x, 2)
    return a

n = 5
result = square(n)
print(result, "\n")

def squareit(n):
    return n * n

def cubeit(n):
    return n*n*n

def main():
    anum = int(input("Please enter a number: "))
    print(squareit(anum), "\n")
    print(cubeit(anum), "\n")

if __name__ == "__main__":
    main()

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

def area(radius):
    b = math.pi * radius**2
    return b

def area2(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print(distance(1, 2, 4, 6), "\n")
print(area2(0, 0, 1, 1), "\n")

def myPi(iters):
    """Calculate an approximation of Pi by utilizing the Leibniz approximation with iters number of iterations."""
    pi = 0
    sign = 1
    denominator = 1
    for i in range(iters):
        pi = pi + (sign/denominator)
        sign = sign * -1 # Alternate positive and negative
        denominator = denominator + 2

    pi = pi * 4.0
    return pi

pi_approx = myPi(10000)
print(pi_approx, "\n")

import random

def average(some_list):
    sum = 0
    for number in some_list:
        sum += number
    return sum / len(some_list)

numbers = []

for i in range(100):
    number = random.randint(0, 1000)
    numbers.append(number)

print(average(numbers))

eng2sp = {"three": "tres", "two": "dos", "one": "uno"}
value_eng2sp = eng2sp["two"]
print(value_eng2sp + "\n")

mydict = {"feline": 12, "canine": 6, "elephant": 23}
value_mydict = mydict["canine"]
print(str(value_mydict) + "\n")
mydict["mouse"] = mydict["feline"] + mydict["canine"]
print(str(mydict["mouse"]) + "\n")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
del inventory["pears"]
print(str(inventory) + "\n")
inventory["bananas"] = inventory["bananas"] + 200
print(str(inventory["bananas"]) + "\n")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
for akey in inventory.keys(): # The order in which we obtain the keys.
    print("Obtained key", akey + ",", "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(str(ks) + "\n")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
for k in inventory:
    print("Obtained key", k, "\n")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k, v) in inventory.items():
    print("Obtained", k + ",", "which maps to", v, "\n")

for k in inventory:
    print("Obtained", k + ",", "which maps to", inventory[k], "\n")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print("apples" in inventory)
print("cherries" in inventory)

if "bananas" in inventory:
    print(str(inventory["bananas"]) + "\n")
else:
    print("We have no bananas.")

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))
print(str(inventory.get("cherries", 0)) + "\n")

mydict = {"feline":12, "canine":6, "elephant":23, "bear":20}
keylist = list(mydict.keys())
keylist.sort()
print(str(keylist[3]) + "\n")

answer = mydict.get("feline") // mydict.get("canine")
print(str(answer) + "\n")

print(str("dog" in mydict) + "\n")

print(str(23 in mydict) + "\n")

total = 0
mydict = {"feline":12, "canine":6, "elephant":23, "bear":20}
for akey in mydict:
    if len(akey) > 3:
        total = total + mydict[akey]
print(str(total) + "\n")

opposites = {"up": "down", "right": "wrong", "true": "false"}
alias = opposites

print(alias is opposites)

alias["right"] = "left"
print(str(opposites["right"]) + "\n")

mydict = {"feline":12, "canine":6, "elephant":23, "bear":20}
yourdict = mydict
yourdict["elephant"] = 999
print(str(mydict["elephant"]) + "\n")

matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix.get((0, 3)))
print(str(matrix.get((1, 3), 0)) + "\n")

homeruns = {}
homeruns["George Herman Ruth"] = 714
homeruns["Michael Charles Mantle"] = 536
homeruns["Barry Lamar Bonds"] = 762

total = 0
for player in homeruns:
    total += homeruns[player]

print("Total homeruns =", total)

x = input("Enter a sentence: ")

x = x.lower() # convert to all lowercase

alphabet = "abcdefghijklmnopqrstuvwxyz"

letter_count = {} # Empty Dictionary

for char in x:
    if char in alphabet: # Ignore any punctuation, numbers, etc.
        if char in alphabet:
            if char in letter_count:
                letter_count[char] = letter_count[char] + 1
            else:
                letter_count[char] = 1

keys = letter_count.keys()
for char in sorted(keys):
    print(char, letter_count[char])

pirate = {}
pirate["sir"] = "matey"
pirate["hotel"] = "fleabag inn"
pirate["student"] = "swabbie"
pirate["boy"] = "matey"
pirate["madam"] = "proud beauty"
pirate["professor"] = "foul blaggart"
pirate["restaurant"] = "galley"
pirate["your"] = "yer"
pirate["excuse"] = "arr"
pirate["students"] = "swabbies"
pirate["are"] = "be"
pirate["lawyer"] = "foul blaggart"
pirate["the"] = "th'"
pirate["restroom"] = "head"
pirate["my"] = "me"
pirate["hello"] = "avast"
pirate["is"] = "be"
pirate["man"] = "matey"

sentence = input("Please enter a sentence: ")

psentence = []

words = sentence.split()
for aword in words:
    if aword in pirate:
        psentence.append(pirate[aword])
    else:
        psentence.append(aword)

print(" ".join(psentence))

def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(str(listsum([1,3,5,7,9])) + "\n")

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

print(str(listsum([1,3,5,7,9])) + "\n")

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n // base, base) + convertString[n % base]

print(str(toStr(1453, 16)) + "\n")

def tree(branchLen, t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15, t)
        t.left(40)
        tree(branchLen-15, t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myVictory = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75, t)
    myVictory.exitonclick()

main()

class Point:
    
    # Point class for representing and manipulating x,y coordinates.
    def __init__(self):
        # Create a new point at the origin
        self.x = 0
        self.y = 0

p = Point() # Instantiate an object of type Point
q = Point() # and create a second point.

print("Nothing seems to have happened with the points.\n")

print(str(p) + "\n")
print(str(q) + "\n")
print(p is q)

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def obtainX(self):
        return self.x

    def obtainY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

p = Point(7, 6)
print(str(p.obtainX()) + "\n")
print(str(p.obtainY()) + "\n")
print(str(p.distanceFromOrigin()) + "\n")

import math

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def obtainX(self):
        return self.x

    def obtainY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

def distance(point1, point2):
    xdiff = point2.obtainX() - point1.obtainX()
    ydiff = point2.obtainY() - point1.obtainY()

    dist = math.sqrt(xdiff**2 + ydiff**2)
    return dist

p = Point(4, 3)
q = Point(0, 0)
print(distance(p, q))

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def obtainX(self):
        return self.x

    def obtainY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5

p = Point(7, 6)
print(str(p) + "\n")

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def obtainX(self):
        return self.x

    def obtainY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5
    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)

p = Point(7, 6)
print(p)

class Point:

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def obtainX(self):
        return self.x

    def obtainY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x**2) + (self.y**2)) ** 0.5
    def __str__(self):
        return "x = " + str(self.x) + ", y = " + str(self.y)

    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

p = Point(3, 4)
q = Point(5, 12)
mid = p.halfway(q)

print(str(mid) + "\n")
print(str(mid.obtainX()) + "\n")
print(str(mid.obtainY()) + "\n")

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, otherP):
        dx = (otherP.getX() - self.x)
        dy = (otherP.getY() - self.y)
        return math.sqrt(dy**2 + dx**2)

p = Point(3, 3)
q = Point(6, 7)
print(p.distanceFromPoint(q))

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def slope_from_origin(self):
        if self.x == 0:
            return None
        else:
            return self.y / self.x

p = Point(4, 10)
print(p.slope_from_origin())

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):
        """ Create a new point at the given coordinates. """
        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def __str__(self):
        return str(self.x) + "," + str(self.y)

p = Point(7, 6)
print(str(p) + "\n")
p.move(5, 10)
print(str(p) + "\n")

class Fraction:
    
    def __init__(self, top, bottom):

        self.num = top # The numerator is on top
        self.den = bottom # The denominator is on the bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

myfraction = Fraction(3, 4)
print(myfraction)

print(myfraction.getNum())
print(myfraction.getDen())

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

print(str(gcd(12, 16)) + "\n")

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

myfraction = Fraction(12, 16)

print(str(myfraction) + "\n")
myfraction.simplify()
print(str(myfraction) + "\n")

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)
print()

ourfraction = myfraction
print(myfraction is ourfraction)
print()

def sameFraction(f1, f2):
    return(f1.getNum() == f2.getNum()) and (f1.getDen() == f2.getDen())

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

myfraction = Fraction(3, 4)
yourfraction = Fraction(3, 4)
print(myfraction is yourfraction)
print()
print(sameFraction(myfraction, yourfraction))

def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def simplify(self):
        common = gcd(self.num, self.den)

        self.num = self.num // common
        self.den = self.den // common

    def add(self, otherfraction):
        newnum = (self.num * otherfraction.den) + (self.den * otherfraction.num)
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum // common, newden // common)

f1 = Fraction(1, 2)
f2 = Fraction(1, 4)

f3 = f1.add(f2)
print(f3)

class Point:
    """ Point class for representing and manipulating x,y coordinates."""

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "),"

class Rectangle:
    """Rectange class utilizing Point, width, and height"""

    def __init__(self, initP, initW, initH):

        self.location = initP
        self.width = initW
        self.height = initH

    def getLocation(self):
        return self.location
    
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __str__(self):
        return "location is " + str(self.location) + " width = " + str(self.width) + ", height = " + str(self.height)

loc = Point(4, 5)
r = Rectangle(loc, 6, 5)
print(r, "\n")

import turtle
import math

class SolarSystem:

    def __init__(self, width, height):

        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2, -height/2,
                                             width/2, height/2)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def displayPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = 0.1
        dt = 0.001
        for p in self.planets:
            p.moveTo(p.getXPos() + dt*p.getXVel(), p.getYPos() + dt*p.getYVel())
            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx**2 + ry**2)

            accx = G * self.thesun.getMass()*rx/r**3
            accy = G * self.thesun.getMass()*ry/r**3

            p.setXVel(p.getXVel() + dt*accx)
            p.setYVel(p.getYVel() + dt*accy)

class Sun:

    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getTemperature(self):
        return self.temp

    def getVolume(self):
        v = 4/3 * math.pi * self.radius**3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.radius**2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, new_name):
            self.name = new_name

    def __str__(self):
        return self.name

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

class Planet:

    def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic

        self.pturtle = turtle.Turtle()
        self.pturtle.speed("fast")
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getVolume(self):
        v = 4/3 * math.pi * self.radius**3
        return v

    def getSurfaceArea(self):
        sa = 4 * math.pi * self.radius**2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, new_name):
        self.name = new_name

    def display(self):
        print(self.name)

    def __str__(self):
        return self.name

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy

def createSSandAnimate():

    ss = SolarSystem(2, 2)

    sun = Sun("SUN", 5000, 10, 5800)
    ss.addSun(sun)

    m = Planet("MERCURY", 19.5, 1000, 0.25, 0, 2, "blue")
    ss.addPlanet(m)

    m = Planet("EARTH", 47.5, 5000, 0.3, 0, 2, "green")
    ss.addPlanet(m)

    m = Planet("MARS", 50, 9000, 0.5, 0, 1.63, "red")
    ss.addPlanet(m)

    m = Planet("JUPITER", 100, 49000, 0.7, 0, 1, "black")
    ss.addPlanet(m)

    m = Planet("PLUTO", 1, 500, 0.9, 0, 0.5, "orange")
    ss.addPlanet(m)

    m = Planet("ASTEROID", 1, 500, 1, 0, 0.75, "cyan")
    ss.addPlanet(m)

    numTimePeriods = 10000
    for amove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()

createSSandAnimate()

import turtle
import random

wn = turtle.Screen()
wn.bgcolor("indigo")

tortoise = turtle.Turtle()
hare = turtle.Turtle()
tortoise.color("red")
hare.color("blue")
tortoise.shape("turtle")
hare.shape("turtle")

tortoise.up()
hare.up()
tortoise.goto(-200, 50)
hare.goto(-200, -50)

for i in range(10):
    
    tortoise.forward(random.randint(1, 80))
    tortoise.dot()

    hare.forward(random.randint(1, 80))
    hare.dot()

if (tortoise.xcor() > hare.xcor()):
    print("\nTortoise Emerges Victorious\n")

elif (hare.xcor() > tortoise.xcor()):
    print("\nHare Emerges Victorious\n")

wn.exitonclick()

import turtle
import math

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * math.pi * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)
wn.exitonclick()

import turtle
import math

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * math.pi * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)
wn.exitonclick()

import turtle
import math

def drawPolygon(t, sideLength, numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        t.forward(sideLength)
        t.right(turnAngle)

def drawCircle(anyTurtle, radius):
    circumference = 2 * math.pi * radius
    sideLength = circumference / 360
    drawPolygon(anyTurtle, sideLength, 360)

wn = turtle.Screen()
wheel = turtle.Turtle()

drawCircle(wheel, 20)
wn.exitonclick()
