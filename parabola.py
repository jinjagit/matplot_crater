# Import matplotlib and matplotlib.pyplot
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Create x axis with range and y axis with Sine
# Function for Plotting Sine Graph

r = 1.0 # Radius
a = 0.5 # depth of parabola (below zero)


x = np.arange(-np.pi, np.pi, 0.1)
y = a * (x**2 - r**2)

# Set up plot range and zero lines
plt.ylim(-2, 2)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Plot Sine Graph
plt.plot(x, y, color='green')
plt.show()