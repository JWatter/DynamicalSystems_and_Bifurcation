#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#define logistic map
def logistic(r, x):
    """
    Takes r and x_n as input and returns x_n+1 according to the logistic map:
    x_n+1 = r*x_n*(1-x_n)    
    """
    return r * x * (1-x)

# #iterations of the logistic map and keep the last 100 iterations for visualization later
iterations = 2000
last = 100

#run n iterations and plot bifurcation diagram
def bifurcationDiagram(r, x):
    """
    runs #iterations with differnet r values.
    plots r against x for the last 100 iterations.
    """
    for i in range(0,iterations):
        x = logistic(r, x)
        
        #display bifurcation diagram for the last 100 iterations
        if i >= (iterations - last):
            plt.plot(r,x, ',b')
    return             

#simulate system for 1000 values for r    
r = np.linspace(0, 2, iterations)
# exclude first element since r should be (0,4]
r = np.delete(r,0)
# initialize x0 = 0.1
x = 0.1 * np.ones(iterations-1)
fig = plt.figure() 
# run bifurcationDiagram and plot results
bifurcationDiagram(r,x)            
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation diagram Logistic map, r = (0,2]")
plt.show    

#change r to vary from 3 to 4
r = np.linspace(2, 4, iterations)
r = np.delete(r, 0)
x = 0.1 * np.ones(iterations-1)
fig = plt.figure()
bifurcationDiagram(r,x)
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation diagram Logistic map, r = (2,4]")

#change r to vary over the whole interval: (0,4] 
r = np.linspace(0, 4, iterations)
r = np.delete(r, 0)
x = 0.1 * np.ones(iterations-1)
fig = plt.figure()
bifurcationDiagram(r,x)
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation diagram Logistic map, r = (0,4]")   

