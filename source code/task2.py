import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import matplotlib.pyplot as plt

# return the data for ploting
def drawDiagram(a_low, a_high, a, b, c):
    """
    Plots bifurcation diagram for given inputs.
    Input: range of parameter alpha (a_low and a_high) 
    function / polynomial a*x^2 + b*x + c 
    
    Returns arrays for alpha steady/unsteady and corresponding x values
    in order to plot bifurcation diagram
    """
    alpha_np = np.linspace(a_low, a_high, 10000)
    a_steady = []
    a_unsteady = []
    root_steady = []
    root_unsteady = []

    #iterate over range of alphas
    for alpha in alpha_np :
        coefficients = [a, b, alpha+c]
        roots = np.roots(coefficients)
        roots = roots.tolist()

        #check roots for imaginary part: if yes --> unsteady otherwise steady
        if roots[0].imag == 0 and roots[1].imag == 0:
            root_steady.append(roots)
            a_steady.append(alpha)       
        else: 
            root_unsteady.append(roots)
            a_unsteady.append(alpha)
        
    root_steady = np.array(root_steady)
    root_unsteady = np.array(root_unsteady, dtype=complex)

    return a_steady, a_unsteady, root_steady, root_unsteady


"""
Call function for different dynamical systems and alpha values as stated
in worksheet:
"""
# dx = a - x^2
a_steady, a_unsteady, root_steady, root_unsteady = drawDiagram(-1, 1, -1, 0, 0)
plt.plot(a_steady,root_steady[:,0],label = "steady state", color = 'b')
plt.plot(a_steady,root_steady[:,1], color = 'b')
plt.plot(a_unsteady,root_unsteady[:,0],color = 'r',label = "no steady state", linestyle="--")
plt.plot(a_unsteady,root_unsteady[:,1],color = 'r',linestyle="--")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$x_0 (\alpha)$')
plt.legend()
plt.title(r'$ \dot{x} = \alpha - x^2$' )
plt.show()

# dx = a - 2x^2 - 3
a_steady, a_unsteady, root_steady, root_unsteady = drawDiagram(-3, 6, -2, 0, -3)
plt.plot(a_steady,root_steady[:,0],label = "steady state", color = 'b')
plt.plot(a_steady,root_steady[:,1], color = 'b')
plt.plot(a_unsteady,root_unsteady[:,0],color = 'r',label = "no steady state", linestyle="--")
plt.plot(a_unsteady,root_unsteady[:,1],color = 'r',linestyle="--")
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$x_0 (\alpha)$')
plt.legend()
plt.title(r'Bifurcation diagramm, $ \dot{x} = \alpha - 2x^2 -3$')
plt.show()


# alpha = 1
X = np.linspace(-10,10,100)
fig = plt.figure()
gs = gridspec.GridSpec(nrows=1, ncols=2)

ax1 = fig.add_subplot(gs[0,0])
Y1 = -X**2 + 1
ax1.plot(Y1,X)
ax1.set_title(r'$ \dot{x} = \alpha - x^2$, $\alpha$ = 1')

ax2 = fig.add_subplot(gs[0,1])
Y2 = -2 * X**2 - 2
ax2.plot(Y2,X)
ax2.set_title(r'$ \dot{x} = \alpha - 2x^2-3$, $\alpha$ = 1')
plt.show()

# alpha = -1
X = np.linspace(-10,10,100)
fig = plt.figure()
gs = gridspec.GridSpec(nrows=1, ncols=2)

ax1 = fig.add_subplot(gs[0,0])
Y1 = -X**2 - 1
ax1.plot(Y1,X)
ax1.set_title(r'$ \dot{x} = \alpha - x^2$, $\alpha$ = -1')

ax2 = fig.add_subplot(gs[0,1])
Y2 = -2 * X**2 - 4
ax2.plot(Y2,X)
ax2.set_title(r'$ \dot{x} = \alpha - 2x^2-3$, $\alpha$ = -1')
plt.show()