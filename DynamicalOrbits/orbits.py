import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

'''
https://brilliant.org/problems/starfish-orbit/?ref_id=1587067
Orbits of a point mass under the influence of a V(r) = 1/r^3 - 1/r potential.
Position in polar coordinates: x = r * cos(theta), y = r * sin(theta)
Equation of motion (in polar coordinates): F = m * d^2/dt^2 r = -d/dr V(r)
'''

# Parameters:
m = 2
t = np.linspace(0,200,1600)
statei_r = (2,0.2) #(r,rdot)
statei_theta = (1,0.1) #(theta,thetador)

#ecuación: exponencial: d/dx f(x) - f(x) = 0
def equation_r(state, t, m):
    r = state[0]
    rdot = state[1]
    dr = rdot
    drdot = (1/m) * (3/(r ** 4) - 1/(r ** 2))
    dstater_dt = [dr,drdot]
    return dstater_dt

def equation_theta(state, t):
    theta = state[0]
    thetadot = state[1]
    dtheta = thetadot
    dthetadot = 0
    dstatetheta_dt = [dtheta,dthetadot]
    return dstatetheta_dt

#solve the ode
stater = odeint(equation_r, statei_r, t, args = (m,))
statetheta = odeint(equation_theta, statei_theta, t)

#x-y trajectory
xtot = np.multiply(stater[:,0], np.cos(statetheta[:,0]))
ytot = np.multiply(stater[:,0], np.sin(statetheta[:,0]))


#figure parameters (height, width...)
def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)

# plotting the trajectory
plt.style.use('seaborn')

fig, ax = plt.subplots()
fig2, (ax1,ax2) = plt.subplots(ncols = 2, nrows = 1)

fig.suptitle('Orbital motion(m = 2)')

ax1.set_title('Radial phase space')
ax2.set_title('Central potential')
#ax3.set_title('Angular phase space')

#Radial phase space
ax1.plot(stater[:,0], m * stater[:,1], linewidth = 2, label = "m = 2")
ax1.legend(loc = "best")
ax1.set_xlabel('r')
ax1.set_ylabel('m dr/dt')

#Potential vs radius
rvals = np.linspace(0.01,25,1000)
ax2.plot(rvals, 1/np.power(rvals,3) - 1/rvals, label =  "V(r)")
ax2.legend(loc = "best")
ax2.set_xlabel('r')
ax2.set_ylabel('V')

#ax3.plot(statetheta[:,0],statetheta[:,1], linewidth = 3, label = "m = 2") #not really interesting.
ax2.set_xlim([-1, 20])
ax2.set_ylim([-1, 5])

set_size(7,3)

def draw_orbit(i):
    ax.cla()
    #ax.set_aspect('equal', adjustable='box')

    rnow = stater[i,0]
    rdotnow = stater[i,1]
    thetanow = statetheta[i,0]

    ########particle moving on top of trajectory
    xf = rnow * np.cos(thetanow)
    yf = rnow * np.sin(thetanow)

    ax.plot(xtot, ytot, color  = 'black', linewidth = 3 , label = 'Trajectory')
    ax.plot(xf, yf,'or', label = 'Point mass')

    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])
    ax.legend(loc = 'best')

    ########### Radial phase space
    #ax1.plot(stater[:,0],stater[:,1], linewidth = 3, label = "m = 2")
    #ax1.plot(rnow,rdotnow, 'or')
    #ax1.legend(loc = "best")

frames = 600
ani = FuncAnimation(fig, draw_orbit, frames  = frames, interval = 10, repeat = True)

figfile = "./DynamicalOrbits/PhaseSpace-Potential.png"
fig2.savefig(figfile, facecolor='w', edgecolor='w',format='png')

anifile = f"./DynamicalOrbits/CentralForceOrbits-{frames}.gif"
ani.save(anifile, writer='imagemagick')

plt.show()















#
