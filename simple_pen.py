import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from matplotlib.animation import FuncAnimation

#simple pendulum example (in kg, meters)

#Definitions, initial state = [theta, thetadot], and timespan
g = 9.8
params = {"mass": 5, "length": 2, "friction": 0.5}
m = params["mass"]
l = params["length"]
b = params["friction"]
stateinit = [np.pi/2 + 0.5, 0]
t = np.linspace(0,20,200)

#ecuación: exponencial: d/dx f(x) - f(x) = 0
def difeqs(state, t, m, l, b, g):
    theta = state[0]
    thetadot = state[1]
    dtheta = thetadot
    dthetadot = -(b / m) * thetadot - (g / l) * np.sin(theta)
    dstate_dt = [dtheta, dthetadot]
    return dstate_dt


#solve the ode
state = odeint(difeqs, stateinit, t, args = (m,l,b,g))

#plots:
plt.style.use('fivethirtyeight')
fig1, (ax1,ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

fig2, ax3 = plt.subplots()

fig3, ax4 = plt.subplots()

fig1.suptitle('Position and speed')
fig2.suptitle('Phase space (m,g,b)')
fig3.suptitle('Pendulum motion')

def point_ani_1(i):
    ax1.cla()
    ax2.cla()

    ax1.plot(t,state[:,0], 'c',label = r'$\theta $')
    ax2.plot(t,state[:,1], 'c',label = r'$\dot{\theta} $')

    ax1.plot(t[i], state[i,0],'or')
    ax2.plot(t[i], state[i,1],'or')

    ax1.legend(loc = 'best')
    ax2.legend(loc = 'best')

    ax1.set_xlabel('Time')
    ax1.set_ylabel('Displacement')
    ax2.set_ylabel('Velocity')


def point_ani_2(i):
    ax3.cla()

    ax3.plot(state[:,0], m * state[:,1], label = '(5,2,0)')

    ax3.plot(state[i,0], m * state[i,1],'or')

    ax3.legend(loc = 'best')

def pendulum(i):
    ax4.cla()

    ax4.set_aspect('equal', adjustable='box')

    xf = l * np.sin(state[i,0])
    yf = -l * np.cos(state[i,0])

    ax4.plot((0, xf), (0, yf), 'k', linewidth = 3)

    ax4.plot(xf, yf,'or', label = '(5,2,0)')

    ax4.set_xlim([-2.5, 2.5])
    ax4.set_ylim([-2.5, 2.5])
    ax4.legend(loc = 'best')


ani1 = FuncAnimation(fig1, point_ani_1, interval = 10)
ani2 = FuncAnimation(fig2, point_ani_2, interval = 10)
ani3 = FuncAnimation(fig3, pendulum, interval = 10)

plt.tight_layout()
plt.show()

#plotting an animated pendulum

x0, y0 = (0, 0) #rod's extremum
'''
iter = 0
while iter < len(t):
    imgshot = 'fig' + str(iter) + '.png'

    theta = state[iter,0]
    now = t[iter]

    xf, yf = (l * np.sin(theta), - l * np.cos(theta)) #rod's other extremum
    ax4.plot(x0[iter], x1[]),(x0[1], x1[1]), linewidth = 4)

    iter = iter + 1
'''
















#
