# Physics Simulations
Various simulations of physical systems with their own graphs (from trajectories to phase spaces), and animations. Also, related ideas such as Monte Carlo methods are shown and plotted

## Pre-requisites
Clearly, one needs python 3.x installed in their system. We would also need the following modules:
1. numpy (of course), for most computations using lists/arrays.
2. matplotlib (again, of course), for plots, graphs and animations. It would be better if using the same backend as me, Qt.
3. scipy, for numerically solving the ODE's appearing in each system.
3. random, for the Monte Carlo simulation.

## Content
The repository has the following structure-tree:
* Home directory. 
    * simple_pen.py, script illustrating the most basic plotting and tools (odeint, for instance) used in the rest of the scripts.
    * MonteCarlo.py and its animations, a simple numerical estimation of Pi by "throwing darts" to a circular target inscribed in a square.
    1. DynamicalOrbits.
        * orbits.py and its figures and animations, an example of a simulation of a point mass subject to a ficticious central force.  
    2. ConstrainedPointMass.
        * finalproject.pdf, a document I myself wrote (in Spanish) several years ago, where the system and analytical computations are described.
        * mechanics.py and its figures and animations, showing the computation and plots: phase space, theta plots and an animation of a particle constrained to a rotating ring.
        * phasespace.py and its figures, computing different phase space trajectories for different sets of parameters.


