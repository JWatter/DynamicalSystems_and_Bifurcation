#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from mpl_toolkits.mplot3d import Axes3D

#initialize time
t_start, t_end = 0, 1000
t = np.linspace(t_start, t_end, 30000)

def lorenz(t, x0):
    """
    t: independent variable (time)
    state: initial values
    
    returns values for x, y and z according to the lorenz system
    """
    x, y, z = x0
    return sigma * (y - x), x * (rho - z) - y, x * y - beta * z
 
#setting up parameters
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0
#initialize x_0 vector
x0 = [10, 10, 10]    
#solve lorenz attractor using solve_ivp
sol1 = solve_ivp(lorenz, [t_start, t_end], x0, t_eval=t)
#plot results in 3d plot
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(sol1.y[0], sol1.y[1], sol1.y[2], 'r-', linewidth=0.05, label='x0 = '+str(x0))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(r'$\rho=$'+str(rho) + r' $\sigma=$'+str(sigma) + r' $\beta=$'+str(round(beta,2)))
ax.grid()
plt.draw()

#second plot with slightly perturbed initial conditions
x0 = [10+10e-8, 10, 10]
sol2 = solve_ivp(lorenz, [t_start, t_end], x0, t_eval=t)
ax.plot(sol2.y[0], sol2.y[1], sol2.y[2], 'k-', linewidth=0.05, label='x0 = '+str(x0))
ax.legend()
plt.draw()
plt.show()

#change parameter rho and plot system again
rho = 0.5
x0 = [10, 10, 10]    
sol3 = solve_ivp(lorenz, [t_start, t_end], x0, t_eval=t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(sol3.y[0], sol3.y[1], sol3.y[2], 'r-', label='x0 = '+str(x0))
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_title(r'$\rho=$'+str(rho) + r' $\sigma=$'+str(sigma) + r' $\beta=$'+str(round(beta,2)))
ax.grid()
plt.draw() 

#second plot with slightly perturbed initial conditions
x0 = [10+10e-8, 10, 10]
sol4 = solve_ivp(lorenz, [t_start, t_end], x0, t_eval=t)
ax.plot(sol4.y[0], sol4.y[1], sol4.y[2], 'ko', label='x0 = '+str(x0))
ax.legend()
plt.draw()
plt.show()

#Analysis
def traj_dist(x1, y1, z1, x2, y2, z2):
    """
    Calculates euclidean distance of 2 vectors in 3d (evaluated as array)
    here it can be interpreted as the distance of our 2 trajectories.
    returns index (=timestep) where distance is initially >= 1
    """
    dist = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    indices, = np.where(dist >= 1)
    return indices[0]

def traj_dist1(x1, y1, z1, x2, y2, z2):
    """
    Calculates euclidean distance of 2 vectors in 3d (evaluated as array)
    here it can be interpreted as the distance of our 2 trajectories.
    returns array which shows the difference for each two corresponding points
    of the trajectories
    """
    dist = np.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
    return dist

# timestep where difference of the 2 trajectories becomes > 1
iteration_t = traj_dist(sol1.y[0], sol1.y[1], sol1.y[2], sol2.y[0], sol2.y[1], sol2.y[2])
# calculate difference between the two trajectories for rho = 0.5
iteration_t1 = traj_dist1(sol3.y[0], sol3.y[1], sol3.y[2], sol4.y[0], sol4.y[1], sol4.y[2])