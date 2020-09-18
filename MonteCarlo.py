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
#ax.add_artist(square)

#Draw Circle
circle = plt.Circle((0, 0), 1, color='c', fill = False, linewidth = 2, label = "Circle")
ax.add_artist(circle)

props1 = dict(boxstyle='round', facecolor='wheat')
props2 = dict(boxstyle='round', facecolor='wheat')

pointsCir = 0
pointsSqu = 0

def newpoint(i):
    global pointsCir, pointsSqu
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    ax.plot(x,y, 'ro')

    dist = x ** 2 + y ** 2
    pointsSqu += 1
    if dist <= 1:
        pointsCir += 1

    aproxPi = round(4 * pointsCir/pointsSqu,3)

    #Boxes with extra information
    infobox = ax.text(1.05, 0.5, "Points: " + str(i), transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props1)
    pibox = ax.text(1.05, 0.25, r"$\pi = $" + str(aproxPi), transform=ax.transAxes, fontsize=14,
            verticalalignment='top', bbox=props2)

    #ax.add_artist(infobox)

frames = 200

ani = FuncAnimation(fig, newpoint, frames = frames, interval = 100, repeat = False)

ax.legend(handles = [square, circle], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left') #bbox_to_anchor = (x-distance from center, y-distance from center)

#fig.text(x,y (from bottom), text, horizontalalignment optional argument)
fig.text(.5, .005, "Random points over a square with a circle of radius 1 inscribed in it.\n" + r"Pi can be computed as 4 $\times$ Area circle/Area square = 4 $\times$ Points out/Points in", ha='center')
#fig.text(.5, .005, "\n" + r"Pi can be computed as $\dfrac{Points out}{Points in}$, ", ha='center')

anifile = f"./MonteCarloPi-{frames}.gif"
ani.save(anifile, writer='imagemagick')

plt.show()





















#
