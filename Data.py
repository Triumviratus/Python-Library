#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import sys # To determine Python Version Number
import matplotlib # To Determine Matplotlib Version Number

print("Python Version " + sys.version)
print("Pandas Version " + pd.__version__)
print("Matplotlib Version " + matplotlib.__version__ + "\n")

buildings = pd.read_csv("buildings.csv")
print(buildings)

# The purpose of these two lines of code is to display all the data from the csv file
# so that it is accessible for the purpose of program modification.

def main():
    
    """First Visualization"""

    buildings_data_frame = pd.read_csv("buildings.csv")
    
    buildings_data_frame.plot(x="Square Feet", y="Building Value", kind="scatter",color="blue")
    
    plt.xlabel("Square Feet")
    
    plt.ylabel("Building Value")

    plt.title("Correlation of Area Versus Value")
    
    plt.show()

    """Second Visualization"""

    buildings_data_frame = pd.read_csv("buildings.csv")

    sort_data = buildings_data_frame.sort_values(["Contents Value"], ascending=False)

    top10 = sort_data[:10] # This arranges the top 10 values of the sort_data variable.

    top10.plot(x="Year Built", y="Contents Value", kind="bar", color="red")
    
    plt.xlabel("Year Built")
    
    plt.ylabel("Contents Value")

    plt.title("Year Built Versus Most Expensive Contents Value")

    plt.show()
    
#-------------------------------------

if __name__ == "__main__":
    main()

# To visualize this data, we must consider quantitative pieces of data.
# The first visualization will be a scatterplot that examines whether
# there is a correlation between the area of the building and its value.
# The second visualization will be a bar graph that measures that compares
# the year built and the contents value of the building in the year that it
# was built. Only the 10 most expensive contents values and the years those
# buildings were constructed in will be sorted from the data.
