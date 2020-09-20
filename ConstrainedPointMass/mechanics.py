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
g = 9.8
m = 1

init_theta = [2.5,1]
init_phi = [0, 1] #[phi_0,w], constant angular velocity
w = init_phi[1]

t = np.linspace(0,20,400)

#equations of motion: r=R fixed, phi = phi_0 + w * t and
def equation_theta(state, t, g, R, w):
    theta = np.mod(state[0], 2 * np.pi) - np.pi # theta ranges from -pi to pi
    thetadot = state[1]
    dtheta = thetadot
    dthetadot = -(g/R) * np.sin(theta) + (w ** 2) / 2 * np.sin(2*theta)
    return [dtheta,dthetadot]

state = odeint(equation_theta, init_theta, t, args = (g,R,w))

theta = np.mod(state[:,0], 2 * np.pi) - np.pi
thetadot = state[:,1]

###### phase space #######
fig, (ax1, ax2) = plt.subplots(1,2, figsize=(10, 5), dpi=100)

ax1.set_title(r"$\theta$ phase space")
ax1.set_xlabel(r"$\theta$")
ax1.set_ylabel(r"$P_\theta$")
ax1.set_xlim(-np.pi, np.pi) # theta ranges from -pi to pi
ax2.set_title(r"$\theta$ and $\dot{\theta}$ over time")
ax2.set_xlabel("t")

ax1.plot(theta, m * R**2 * thetadot)

rangeplot = int(len(t)/5)
ax2.plot(t[0:rangeplot],theta[0:rangeplot], label  = r"$\theta$")
ax2.plot(t[0:rangeplot],thetadot[0:rangeplot], label  = r"$\dot{\theta}$")

ax2.legend(title = "Legend", loc='upper left', bbox_to_anchor = [1.05,1])

###### 3d plot ###########
#twice as wide as it is tall
fig3d = plt.figure(figsize=plt.figaspect(0.5))

ax3d = fig3d.add_subplot(projection='3d')

circtheta = np.linspace(0, 2 * np.pi, 201)
def plotanim(timenow):
    ax3d.cla()
    ax3d.set_xlim(-Rplot, Rplot)
    ax3d.set_ylim(-Rplot, Rplot)
    ax3d.set_zlim(-Rplot, Rplot)
    ax3d.set_xlabel("x")
    ax3d.set_ylabel("y")
    ax3d.set_zlabel("z")

    thetanow = theta[timenow]
    xf = - R * np.sin(thetanow) * np.sin(init_phi[0] + w * timenow/10)
    yf = R * np.sin(thetanow) * np.cos(init_phi[0] + w * timenow/10)
    zf = - R * np.cos(thetanow)

    ax3d.plot((0,0),(0,0), (-Rplot,Rplot), '-k', label='z-axis')
    ax3d.plot(- R * np.sin(circtheta) * np.sin(init_phi[0] + w * timenow/10), R * np.sin(circtheta) * np.cos(init_phi[0] + w * timenow/10), - R * np.cos(circtheta), linewidth = 3, label = "Ring")

    ax3d.plot([xf], [yf], [zf], 'or', markersize = 10, label = "Point mass")

frames  = 200
anim = FuncAnimation(fig3d, plotanim, frames  = frames, interval = 10)

figfile = f"./ConstrainedPointMass/PhaseSpace-w={init_phi[1]}.png"
fig.savefig(figfile, facecolor='w', edgecolor='w',format='png', dpi=100)

anifile = f"./ConstrainedPointMass/animation-w={init_phi[1]}.gif"
#anim.save(anifile, writer='imagemagick')

plt.show()




















#
