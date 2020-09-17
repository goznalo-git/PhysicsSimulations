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
t = np.linspace(0,200,20)
stateinit = (2,1,0.2,0.1) #(r,theta,rdot,thetadot)

#ecuación: exponencial: d/dx f(x) - f(x) = 0
def equations(state, t, m):
    r = state[0]
    theta = state[1]
    rdot = state[2]
    thetadot = state[3]
    dr = rdot
    dtheta = thetadot
    drdot = (1/2) * (3/(r ** 4) - 1/(r ** 2))
    dthetadot = 0
    dstate_dt = [dr,dtheta,drdot,dthetadot]
    return dstate_dt

#solve the ode
state = odeint(equations, stateinit, t, args = (m,))

# plotting the trajectory
plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()

ax.set_title('Orbital motion')

def draw_orbit(i):
    ax.cla()

    #ax.set_aspect('equal', adjustable='box')

    xf = state[i,0] * np.sin(state[i,0])
    yf = state[i,0] * np.cos(state[i,0])

    #ax4.plot((0, xf), (0, yf), 'k', linewidth = 3)

    ax.plot(xf, yf,'or', label = 'm = 2')

    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.legend(loc = 'best')

ani = FuncAnimation(fig, draw_orbit, interval = 100)

plt.show()


















#
