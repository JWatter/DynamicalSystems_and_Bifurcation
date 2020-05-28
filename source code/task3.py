from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# plot phase diagram for Andronov-Hopf bifurcation
def plotPhaseDiagram(alpha, x1, x2):
    X1, X2 = np.meshgrid(x1, x2)
    # Andronov Hopf equations
    dx1 = alpha*X1 - X2 - X1*(X1**2+X2**2)
    dx2 = X1 + alpha*X2 - X2*(X1**2+X2**2)
    plt.figure()
    a1 = plt.subplot()
    a1.streamplot(X1, X2, dx1, dx2)
    a1.set_title(r'Andronov-Hopf bifurcation $\alpha =$'+str(alpha))
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.show()

# compute orbits with alpha=1
def orbit(start, delta=0.1):
    orbit = np.empty((2, 100+1)) # save with time step
    orbit[:, 0] = start
    for i in range(0, 100):
        x1 = orbit[0][i]
        x2 = orbit[1][i]
        # alpha = 1
        dx1 = 1*x1 - x2 - x1*(x1**2+x2**2)
        dx2 = x1 + 1*x2 - x2*(x1**2+x2**2)
        # use Euler's method to update x1, x2
        x1 += delta * dx1
        x2 += delta * dx2
        x_new = np.array([x1, x2])
        orbit[:, i+1] = x_new
    x1_list = orbit[0, :]
    x2_list = orbit[1, :]
    plt.figure()
    plt.plot(x1_list, x2_list, label='trajectory')
    plt.title('Trajectory with start point at: '+str(start))
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.plot(x1_list[0], x2_list[0], 'og', label='start point')
    plt.plot(x1_list[-1], x2_list[-1], 'ob')
    plt.legend()
    plt.show()

# visualize cusp bifurcation (a1, a2, x) where a1+a2*x-x^3=0
def plotCusp():
    x = np.linspace(-10, 10, 100)
    a2 = np.linspace(-1, 1, 100)
    x, a2 = np.meshgrid(x, a2)
    # solve a1 with known a2 and x
    a1 = x**3 - a2*x  
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot_surface(a1, a2, x, rstride=2, cstride=2, cmap='rainbow')
    ax.set_xlabel(r'$\alpha_1$')
    ax.set_ylabel(r'$\alpha_2$')
    ax.set_zlabel('x')
    ax.set_title('Cusp bifurcation')
    plt.show()


# task3.1: plot three phase diagrams
x1 = np.arange(-1, 1.1, 0.1)
x2 = np.arange(-1, 1.1, 0.1)
for alpha in [-0.5, 0, 0.5]:
    plotPhaseDiagram(alpha, x1, x2)

# task3.2: compute and visualize tow orbits with alpha=1
# start = (2, 0)
orbit(start=np.array([2, 0]))
# start = (0.5, 0)
orbit(start=np.array([0.5, 0]))

# task3.3: cusp bifurcation
plotCusp()
