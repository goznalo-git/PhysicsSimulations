import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import random

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.set_title("Computing Pi using Monte Carlo methods")

ax.set_xlim([-1.1,1.1])
ax.set_ylim([-1.1,1.1])
ax.set_aspect('equal', adjustable='box')

ax.plot(0,0,"x", color = "lightgrey")

#Draw square
square, = plt.plot((-1,1,1,-1,-1),(1,1,-1,-1,1), "k", linewidth = 2, label = "Square")
ax.add_artist(square)

#Draw Circle
circle = plt.Circle((0, 0), 1, color='c', fill = False, linewidth = 2, label = "Circle")
ax.add_artist(circle)


def newpoint(i):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    ax.plot(x,y, 'ro')

ani = FuncAnimation(fig,newpoint,frames = 100, interval = 100, repeat = False)

ax.legend(handles = [square, circle], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left') #bbox_to_anchor = (x-distance from center, y-distance from center)

#fig.text(x,y (from bottom), text, horizontalalignment optional argument)
fig.text(.5, .005, "Random points over a square with a circle of radius 1 inscribed in it.", ha='center')

plt.show()





















#
