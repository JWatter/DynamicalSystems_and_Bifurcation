import numpy as np 
import matplotlib.pyplot as plt 
import math

def drawPhase(alpha, x1, x2):
    X1, X2 = np.meshgrid(x1, x2)
    dx1 = (alpha**2)*X1 + (2*alpha)*X2
    dx2 = (-alpha**2)*X1 + (-alpha)*X2
    coefficients = [1, -alpha**2+alpha, alpha**3]
    roots = np.roots(coefficients)
    roots = roots.tolist()
    l1 = roots[0]
    l2 = roots[1]
    plt.figure()
    a1 = plt.subplot()
    a1.streamplot(X1, X2, dx1, dx2)
    a1.set_title(r'$\alpha=$'+str(alpha)+r', $\lambda _1=${:.2f}, $\lambda _2=${:.2f}'.format(l1, l2))
    plt.show()

# initialize x1 x2
x1 = np.arange(-1, 1.1, 0.1)
x2 = np.arange(-1, 1.1, 0.1)

# (n+, n-) = (1, 1)
drawPhase(-1, x1, x2)

# (n+, n-) = (2, 0)
drawPhase(6, x1, x2)
drawPhase(2, x1, x2)

# (n+, n-) = (0, 2)
drawPhase(0.1, x1, x2)
drawPhase(0.6, x1, x2)
