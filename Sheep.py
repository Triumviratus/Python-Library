#-----------------------------------------------------------------------
# Ambrose Ryan Xavier
#-----------------------------------------------------------------------
# Determine whether introducing 50 sheep into the San Rosario Mountains
# is enough for the population to survive as well as the probability
# that the sheep will survive for 100 years at minimum.
#-----------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

San_Rosario = []
San_Rosario.append(50)
historical_data = []

def sheep():
    n = 50
    t = 100
    p = 0
    for i in range(t):
        p = np.random.random()
        if p > 0.5:
            n = n*1.1
        else:
            n = n*0.9
        print(n)
        San_Rosario.append(n)

    print("The population of sheep after {} years is...{}".format(int(t), int(n)))
    historical_data.append(n)

def plot(n):
    plt.figure("Conservation Genetics")
    plt.title("Extinction of Sheep")
    plt.plot(n)
    plt.xlabel("Time (Years)")
    plt.ylabel("Population Size")
    plt.show()

def prob(n):
    extinct = 0
    for i in n:
        if i < 2:
            extinct = extinct + 1
    return extinct/len(n)

def main():
    sheep()
    plot(San_Rosario)
    for i in range(100):
        sheep()
    plot(historical_data)
    print(prob(historical_data))

main()
