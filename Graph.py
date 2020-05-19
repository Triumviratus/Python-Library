#----------------------------------------------------------------------------
# Ambrose Ryan Xavier
#----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import math

#-------------------------------------

def plot_line(x1, y1, x2, y2):
    """Plot a line by utilizing the specific points."""
    x = [x1, x2]
    y = [y1, y2]
    plt.plot(x, y, "m-")

#-------------------------------------

def plot_sine_wave(start_x, stop_x, amplitude):
    """Plot a sine wave."""
    x_array = np.linspace(start_x, stop_x, 1000)
    y_array = []
    for x in x_array:
        y_array.append(amplitude * math.sin(x))
    plt.plot(x_array, y_array, linewidth=5.0)

#-------------------------------------

def main(graph_min, graph_max):

    plt.axis([graph_min, graph_max, graph_min, graph_max])

    plot_line(graph_min, graph_min, graph_max, graph_max)
    plot_line(graph_min, graph_max, graph_max, graph_min)
    plot_sine_wave(graph_min // 2, graph_max // 2, graph_max // 4)

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")

    plt.show()

#-------------------------------------

main(-100, 100)

#-------------------------------------

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1, 2, 3, 4])
plt.xlabel("Some Numbers")
plt.ylabel("Some Numbers")
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], "ro")
plt.axis([0, 6, 0, 20])
plt.xlabel("Some Numbers")
plt.ylabel("Some Numbers")
plt.show()

# Evenly sampled time at 200 millisecond intervals
t = np.arange(0.0, 5.0, 0.2)

# Red dashes, blue squares, and green triangles
plt.plot(t, t, "r--", t, t**2, "bs", t, t**3, "g^")
plt.show()

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), "bo", t2, f(t2), "k")
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), "r--")
plt.show()

np.random.seed(19680801)

mu, sigma = 100, 15

x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor = "g", alpha=0.75)

plt.xlabel("IQ")
plt.ylabel("Probability")
plt.title("Histogram of IQ")
plt.text(69, 0.025, r"$\mu=100,\ \sigma=15$")
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate("local max", xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor="black", shrink=0.05),)

plt.ylim(-2, 2)
plt.show()


from matplotlib.ticker import NullFormatter # Valuable for "Logit" Scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# Create some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()

# Plot with various axes scales
x = np.arange(len(y))

plt.figure(1)

# Linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale("linear")
plt.title("linear")
plt.grid(True)

# Log
plt.subplot(222)
plt.plot(x, y)
plt.yscale("log")
plt.title("Log")
plt.grid(True)

# Symmetric Log

plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale("symlog", linthreshy=0.01)
plt.title("Symlog")
plt.grid(True)

# Logit

plt.subplot(224)
plt.plot(x, y)
plt.yscale("logit")
plt.title("Logit")
plt.grid(True)
# Format the minor tick lables of the y-axis into empty strings with
# "NullFormatter", to avoid cumbering the axis with too many labels.

plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

import numpy as np
import matplotlib.pyplot as plt

#-------------------------------------------------

def generate_rolls(how_many):
    result = np.ndarray(how_many, dtype=int)

    for roll in range(how_many):
        result[roll] = np.random.randint(1, 7) + np.random.randint(1, 7)

    return result

#-------------------------------------------------

def main():

    rolls = generate_rolls(10000)

    plt.hist(rolls, bins=np.arange(2, 14), facecolor = "g", align = "left") # Generate Histogram
    plt.xticks(np.arange(2, 13))
    plt.xlim(1, 13)

    plt.xlabel("Value")
    plt.ylabel("Occurrences")
    plt.title("Histogram of Dice Rolls")
    plt.grid(True)
    plt.show()

#-------------------------------------------------

if __name__ == "__main__":
    main()
