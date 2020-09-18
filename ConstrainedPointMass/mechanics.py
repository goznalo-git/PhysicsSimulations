import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
import numpy as np

plt.style.use('seaborn')

'''
Here we're going to simulate the situation present in the finalproject.pdf file.
For that we will solve the equations of motion and then plot and animate the results.
'''

#Parameters & definitions
R = 1
Rplot = R + 0.1 * R

###### phase space #######
fig, (ax1, ax2) = plt.subplots(2,1)

ax1.set_title("Theta phase space")
ax2.set_title("Theta over time")

###### 3d plot ###########
#twice as wide as it is tall
fig3d = plt.figure(figsize=plt.figaspect(0.5))

ax3d = fig3d.add_subplot(projection='3d')
ax3d.set_xlim(-Rplot, Rplot)
ax3d.set_ylim(-Rplot, Rplot)
ax3d.set_zlim(-Rplot, Rplot)


plt.show()




















#
