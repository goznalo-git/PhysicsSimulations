import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import solve_ivp, odeint
import numpy as np
import random

'''
x´´ = xy
y´´ = -y + x^2
'''

#vars = [x, xdot, y, ydot]
stateinit = [1,1,2,1]
t = np.linspace(0,2,50)

def equations(state, t):
    x = state[0]
    xdot = state[1]
    y = state[2]
    ydot = state[3]

    dx = xdot
    dxdot = x * y
    dy = ydot
    dydot = -y + x ** 2

    return np.array([dx, dxdot, dy, dydot])

sol = odeint(equations, stateinit, t)

#print(res)

plt.plot(sol[:,0],sol[:,2])
#plt.plot(t,sol[:,1])
#plt.plot(t,sol[:,2])

plt.show()










#
