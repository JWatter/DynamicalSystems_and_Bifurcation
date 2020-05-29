#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#initialize time
t_start, t_end = 0, 30
t = np.linspace(t_start, t_end, 1000)

def lorenz(t, state):
    """
    t: independent variable (time)
    state: initial values
    
    returns values for x, y and z according to the lorenz system
    """
    x, y, z = state
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z
 

#setting up parameters
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
#initialize x_0 vector
state0 = [10, 10, 10]    
#solve lorenz attractor using solve_ivp
sol1 = solve_ivp(lorenz, [t_start, t_end], state0, t_eval=t)
#plot results in 3d plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(sol1.y[0], sol1.y[1], sol1.y[2], 'r-')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.grid()
plt.draw()

#second plot with slightly perturbed initial conditions
state0 = [10+10e-8, 10, 10]
sol2 = solve_ivp(lorenz, [t_start, t_end], state0, t_eval=t)
ax.plot(sol2.y[0], sol2.y[1], sol2.y[2], 'k-')
plt.draw()
plt.show()


#change parameter rho and plot system again
rho = 0.5
state0 = [10, 10, 10]    
#solve lorenz attractor using solve_ivp
sol3 = solve_ivp(lorenz, [t_start, t_end], state0, t_eval=t)
#plot results in 3d plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(sol3.y[0], sol3.y[1], sol3.y[2], 'r-')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.grid()
plt.draw() 

#second plot with slightly perturbed initial conditions
state0 = [10+10e-8, 10, 10]
sol4 = solve_ivp(lorenz, [t_start, t_end], state0, t_eval=t)
ax.plot(sol4.y[0], sol4.y[1], sol4.y[2], 'ko')
plt.draw()
plt.show()