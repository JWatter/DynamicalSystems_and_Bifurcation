#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def logistic(r, x):
    return r * x * (1-x)

#simulate system for 1000 values or r    
n = 1000
r = np.linspace(0, 4, n)

#1000 iterations of the logistic map and keep the last 100 iterations for visualization
iterations = 1000
last = 100

# initialize x0 = 0.1
x = 0.1 * np.ones(n)

#run n iterations and plot bifurcation diagram
for i in range(0,iterations):
    x = logistic(r, x)
    
    #display bifurcation diagram for the last 100 iterations
    if i >= (iterations - last):
        plt.plot(r,x, ',k')
        #plt.show
             
plt.xlabel("r")
plt.ylabel("x")
plt.title("Bifurcation diagram")
#plt.show    
    