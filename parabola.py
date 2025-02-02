# Import matplotlib and matplotlib.pyplot
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

def update_plot(val):
   r = radius_slider.val
   a = depth_slider.val
   y = a * (x**2 - r**2)
   line.set_ydata(y)
   fig.canvas.draw_idle()

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.2)

r = 1.0 # Radius, at y = 0
a = 0.5 # Depth, greater is deeper (but is not an absolute value)

x = np.arange(-np.pi, np.pi, 0.1)
y = a * (x**2 - r**2)

# Set up plot range and zero lines
plt.ylim(-2, 2)
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)

# Add sliders
ax_radius = plt.axes([0.1, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
radius_slider = Slider(ax_radius, 'radius', 0, 2.0, valinit=1.0)
ax_depth = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
depth_slider = Slider(ax_depth, 'depth', 0, 2.0, valinit=0.5)

# Plot Sine Graph
line, = ax.plot(x, y, color='green')
radius_slider.on_changed(update_plot)
depth_slider.on_changed(update_plot)
plt.show()