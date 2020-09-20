import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.integrate import odeint
import numpy as np

'''
Phase space exploration
'''

#sets of parameters & definitions
params1 = {"R":1, "g":9.8, "m":1, "init_theta": [2.5,1], "init_phi": [0,1], "color": "blue"}
params2 = {"R":1, "g":9.8, "m":1, "init_theta": [2.5,1], "init_phi": [0,5], "color": "green"}
params3 = {"R":1, "g":9.8, "m":1, "init_theta": [2.5,1], "init_phi": [0,10], "color": "red"}
params4 = {"R":1, "g":9.8, "m":1, "init_theta": [1.5,1], "init_phi": [0,1], "color": "cyan"}
params5 = {"R":1, "g":9.8, "m":1, "init_theta": [2.5,4], "init_phi": [0,1], "color": "magenta"}
params5 = {"R":1, "g":9.8, "m":1, "init_theta": [2.5,-3], "init_phi": [0,1], "color": "yellow"}
params6 = {"R":5, "g":9.8, "m":1, "init_theta": [2.5,1], "init_phi": [0,1], "color": "black"}
params7 = {"R":1, "g":9.8, "m":5, "init_theta": [2.5,1], "init_phi": [0,1], "color": "brown"}

paramstot = {1:params1, 2:params2, 3:params3, 4:params4, 5:params5, 6:params6, 7:params7}

t = np.linspace(0,20,400)

#equations of motion: r=R fixed, phi = phi_0 + w * t and
def equation_theta(state, t, params):
    theta = np.mod(state[0], 2 * np.pi) - np.pi
    thetadot = state[1]
    dtheta = thetadot
    dthetadot = -(params["g"] / params["R"]) * np.sin(theta) + (params["init_phi"][1] ** 2) / 2 * np.sin(2*theta)
    return [dtheta,dthetadot]


###### phase space #######
plt.style.use('seaborn')

fig, ax= plt.subplots()

fig.suptitle(r"$\theta$ phase space")
ax.set_xlabel(r"$\theta$")
ax.set_ylabel(r"$P_\theta$")
ax.set_xlim(-np.pi , np.pi)


i = 1
for params in paramstot.values():
    state = odeint(equation_theta, params["init_theta"], t, args = (params,))
    theta = np.mod(state[:,0], 2*np.pi) - np.pi
    thetadot = state[:,1]
    ax.plot(theta, 2 * params["m"] * params["R"] * thetadot, color = params["color"], label = "params" + str(i))
    i += 1

ax.legend(title='Legend',loc='best')

figfile = f"./ConstrainedPointMass/PhaseSpacesExpl-{len(params)}params.png"
fig.savefig(figfile, facecolor='w', edgecolor='w',format='png')

plt.show()











#
