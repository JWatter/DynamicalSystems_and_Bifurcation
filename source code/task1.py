import numpy as np 
import matplotlib.pyplot as plt 
import math

def drawPhase(alpha, x1, x2):
    X1, X2 = np.meshgrid(x1, x2)
    dx1 = alpha * X1 + alpha *X2
    dx2 = -0.25*X1
    l1 = (alpha + math.sqrt(alpha**2-2*alpha)) / 2
    l2 = (alpha - math.sqrt(alpha**2-2*alpha)) / 2
    plt.figure()
    a1 = plt.subplot()
    a1.streamplot(X1, X2, dx1, dx2)
    a1.set_title(r'$\alpha=$'+str(alpha)+r', $\lambda _1=${:.2f}, $\lambda _2=${:.2f}'.format(l1, l2))
    plt.show()

# initialize x1 x2
x1 = np.arange(-1, 1.1, 0.1)
x2 = np.arange(-1, 1.1, 0.1)

# (n+, n-) = (1, 1)
drawPhase(-0.5, x1, x2)

# (n+, n-) = (2, 0)
drawPhase(2, x1, x2)

# no (n+, n-) = (0, 2), will explain in report