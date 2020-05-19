#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import sys # To Determine Python Version Number
import matplotlib # To Determine Matplotlib Version Number

print("Python version " + sys.version)
print("Pandas version " + pd.__version__)
print("Matplotlib version " + matplotlib.__version__)

# Create Data ------------------------------------------------

# http://www.onthesnow.com/montana/bridger-bowl/historical-snowfall.html

years = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]  # Bridger Bowl Year
total_snowfall = [310, 253, 304, 388, 265, 283, 209, 194] # Inches
largest_snowfall = [18, 19, 16, 19, 25, 20, 14, 13]       # Inches

BridgerDataSet = list(zip(years, total_snowfall, largest_snowfall))
print("BridgerDataSet: ", BridgerDataSet, "\n")

data = pd.DataFrame(data = BridgerDataSet, columns=["Year", "Total", "Largest"])
print("Bridger DataFrame")
print("-----------------")
print(data)

data.to_csv("bridger.csv", index=False,header=False)

# Obtain Data -------------------------------------------------

bridger = pd.read_csv("bridger.csv", names=["Year", "Total", "Largest"])
print("\nBridger DataFrame after reading csv file")
print("------------------------------------------")
print(bridger)

# Prepare Data ------------------------------------------------

if (bridger.Total.dtype == "int64"):
    print("\nTotal Snowfall is of Type int64")
else:
    print("\nTotal Snowfall is of Type", bridger.Total.dtype)

# Analyze Data ------------------------------------------------

sorted_data = bridger.sort_values(["Total"], ascending=False)
print("\nSorted Bridger Data Set")
print("-------------------------")
print(sorted_data)

print("\nThe lowest total snowfall was", bridger["Total"].min())

# Display Data ------------------------------------------------

bridger.plot(x = "Year", y = "Total", kind = "bar", color = "red")
plt.xlabel("Year")
plt.ylabel("Largest Snowfall")
plt.show()

bridger.plot(x = "Year", y = "Total", kind = "line", color = "blue")
plt.xlabel("Year")
plt.ylabel("Largest Snowfall")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

how_many = 1000       # Number of Submissions
file_name = "jbd.csv" # File to write to and then read from

# Create Data ----------------------------------------------------

names = ["Victor", "Ryan", "Justin", "Samuel", "Michael", "Grace",
         "Courtney", "Chris", "Kyle", "Tyler", "Oliver"]

# np.random.seed(2017)
random_names = list(map((lambda x: names[x]),
                        np.random.randint(0, len(names), how_many)))

print("First 5 names:", random_names[:5], "\n")

scores = np.random.randint(0, 101, how_many)
print("First 5 scores:", scores[:5], "\n")

CSDataSet = list(zip(random_names, scores))
print("First 5 Zipped Names and Scores")
print("-------------------------------")
print(CSDataSet[:5])

data_frame = pd.DataFrame(data = CSDataSet, columns=["Names", "Scores"])
print("\nFirst 5 Items in Data Frame")
print("-----------------------------")
print(data_frame[:5])

data_frame.to_csv(file_name, index=False, header=True)

# Access Data ----------------------------------------------------

jbd_data_frame = pd.read_csv(file_name)
print("\nFirst 5 Items in Data Frame From File")
print("---------------------------------------")
print(jbd_data_frame[:5])

print("\nData Frame Info")
print("-----------------")
print(jbd_data_frame.info())

print("\nData Frame Head")
print("-----------------")
print(jbd_data_frame.head())

print("\nData Frame Tail")
print("-----------------")
print(jbd_data_frame.tail(3))

# Manipulate Data ----------------------------------------------------

print("\nUnique Names in Data Frame")
print("----------------------------")

for name in jbd_data_frame["Names"].unique():
    print(name)

jbd_object = jbd_data_frame.groupby("Names")
print("\nDescribe Data Frame")
print(jbd_object.describe())

condensed_data_frame = jbd_object.sum()
print("\nFirst 5 Items in Condensed Data Frame After Sum")
print("-------------------------------------------------")
print(condensed_data_frame[:5])

condensed_data_frame = condensed_data_frame.sort_values(["Scores"])
print("\nFirst 5 Items in Condensed Data Frame After Sort")
print("--------------------------------------------------")
print(condensed_data_frame[:5])

# Present Data ----------------------------------------------------

condensed_data_frame["Scores"].plot.bar(color="turquoise")
plt.xlabel("Student")
plt.ylabel("Points Earned")
plt.title("Introductory Data Science Dashboard")
plt.show()

# Remediation ----------------------------------------------------

os.remove(file_name)

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

failed_banks = pd.read_csv("banklist.csv")

failed_banks["Closing Year"] = 0

for i in range(len(failed_banks)):
    year = failed_banks.ix[i, "Closing Date"]
    year = int(year[-2:]) + 2000
    failed_banks.ix[i, "Closing Year"] = year

plt.figure("Bank Information")

plt.subplot(121)
plt.xlabel("Year")
plt.ylabel("Failures")
plt.title("FDIC Failed Banks")

failed_banks["Closing Year"].value_counts().plot(kind="bar", color="red")

plt.subplot(122)
plt.xlabel("Year")
plt.ylabel("Failures")
plt.title("FDIC Failed Banks")

failed_banks["Closing Year"].value_counts(sort=False).plot("bar", color="violet")

plt.show()
