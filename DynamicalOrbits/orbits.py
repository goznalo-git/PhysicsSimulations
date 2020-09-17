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
t = np.linspace(0,20,200)
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

# plotting the trajectory
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
fig2, ((ax1,ax2),(ax3,ax4)) = plt.subplots(ncols = 2, nrows = 2)

ax.set_title('Orbital motion')
ax1.set_title('Radial phase space')
ax2.set_title('Potential')
ax3.set_title('Angular phase space')

ax1.plot(stater[:,0],stater[:,1], linewidth = 3, label = "m = 2")

rvals = np.linspace(0.01,25,1000)
ax2.plot(rvals, 1/np.power(rvals,3) - 1/rvals, label =  "V(r)")
ax2.legend(loc = "best")

ax3.plot(statetheta[:,0],statetheta[:,1], linewidth = 3, label = "m = 2")

ax2.set_xlim([-1, 20])
ax2.set_ylim([-1, 5])

def draw_orbit(i):
    ax.cla()
    #ax.set_aspect('equal', adjustable='box')

    xf = stater[i,0] * np.sin(statetheta[i,0])
    yf = stater[i,0] * np.cos(statetheta[i,0])

    ax.plot(xf, yf,'or', label = 'm = 2')

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.legend(loc = 'best')

ani = FuncAnimation(fig, draw_orbit, frames  = 100, interval = 10, repeat = True)

plt.show()















#
