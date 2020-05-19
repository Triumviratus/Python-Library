#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------
# Data Generation Template
#----------------------------------------------------------------------------
##4
##56
##Beaverhead County,9401
##Big Horn County,13343
##Blaine County,6601
##Broadwater County,5747
##Carbon County,10460
##Carter County,1203
##Cascade County,81755
##Chouteau County,5759
##Custer County,11924
##Daniels County,1755
##Dawson County,9327
##Deer Lodge County,9085
##Fallon County,3120
##Fergus County,11413
##Flathead County,98082
##Gallatin County,104502
##Garfield County,1310
##Glacier County,13694
##Golden Valley County,831
##Granite County,3368
##Hill County,16542
##Jefferson County,11853
##Judith Basin County,1940
##Lake County,29758
##Lewis and Clark County,67282
##Liberty County,2409
##Lincoln County,19259
##Madison County,7924
##McCone County,1700
##Meagher County,1827
##Mineral County,4184
##Missoula County,116130
##Musselshell County,4589
##Park County,16114
##Petroleum County,489 
##Phillips County,4133
##Pondera County,6084
##Powder River County,1746
##Powell County,6858
##Prairie County,1182
##Ravalli County,42088
##Richland County,11482
##Roosevelt County,11305
##Rosebud County,9287
##Sanders County,11534
##Sheridan County,3648
##Silver Bow County,34553
##Stillwater County,9406
##Sweet Grass County,3623
##Teton County,6056
##Toole County,4977
##Treasure County,692
##Valley County,7539
##Wheatland County,2117
##Wibaux County,1093
##Yellowstone County,158437
#----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

def read_file(name):
    input_file = open(name, "r")
    number_buckets = int(input_file.readline())
    total_counties = int(input_file.readline())

    county_populations = np.zeros([total_counties], dtype="int")
    for county_number in range(total_counties):
        line = input_file.readline().split(",")
        county_populations[county_number] = int(line[1])
    county_populations.sort()
    input_file.close()

    return number_buckets, county_populations

#-------------------------------------

def print_summary(averages):
    print("Population Grouping Summary")
    print("---------------------------")
    for grouping in range(len(averages)):
        print("Grouping", grouping + 1, "has a population average of",
              averages[grouping])
        
#-------------------------------------

def calculate_averages(number_buckets, county_populations):
    n = len(county_populations) // number_buckets
    average = [0] * number_buckets
    for i in range(number_buckets):
        total_bucket = 0
        for j in range(n):
            lowest_k = 0
            lowest_value = county_populations[0]
            for k in range(len(county_populations)):
                if county_populations[k] < lowest_value:
                    lowest_value = county_populations[k]
                    lowest_k = k
            if lowest_k == 0:
                cou_pop = county_populations[1:]
            elif lowest_k == len(county_populations) - 1:
                cou_pop = county_populations[:lowest_k]
            else:
                cou_pop = county_populations[:lowest_k] + county_populations[lowest_k + 1:]
            county_populations = cou_pop
            total_bucket = total_bucket + lowest_value
        average[i] = total_bucket // n
    return average
#-------------------------------------

def graph_summary(averages):

    fig = plt.figure("CSCI 127, Lab 12")
    x = np.arange(1, (number_buckets + 1), 1)
    plt.xticks(x, [1, 2, 3, 4, 5])
    plt.plot(x, averages, "c--")
    plt.plot(x, averages, "bh")
    plt.xlabel("County Groupings")
    plt.ylabel("County Population Average")
    plt.title("Montana County Population Analysis")
    fig = plt.figure("CSCI 127, Lab 12")
    plt.show()
#-------------------------------------

number_buckets, county_populations = read_file("montana-counties.txt")
averages = calculate_averages(number_buckets, county_populations)
print_summary(averages)
graph_summary(averages)

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------

def generate_hands(how_many):

    result = np.ndarray(how_many, dtype=int)

    for hand in range(how_many):
        
        card1 = np.random.randint(1, 14)
        card2 = np.random.randint(1, 14)

        if card1 == 1:
            card1 = 11
        elif card1 > 10:
            card1 = 10

        if card2 == 1 and card1 == 11:
            card2 = 1
        elif card2 == 1:
            card2 = 11
        elif card2 > 10:
            card2 = 10
        
        result[hand] = card1 + card2

    return result

#-------------------------------------

def main():

    hands = generate_hands(10000)
    plt.figure("CSCI 127, Lab 13")
    plt.hist(hands, bins=np.arange(2, 54), normed=True, facecolor = "g", align = "left") # Generate Histogram
    plt.xticks(np.arange(4, 22))
    plt.xlim(3, 22)
    
    plt.xlabel("Hand Value")
    plt.ylabel("Probability")
    plt.title("Histogram of BlackJack Hands")
    plt.grid(True)
    plt.show()

#-------------------------------------

if __name__ == "__main__":
    main()
