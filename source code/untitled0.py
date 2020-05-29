from scipy import linspace
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def lorenz(t, xyz):
    x, y, z = xyz
    s, r, b = 10, 28, 8/3. # parameters Lorentz used
    return [s*(y-x), x*(r-z) - y, x*y - b*z]

a, b = 0, 40
t = linspace(a, b, 4000)

sol1 = solve_ivp(lorenz, [a, b], [1,1,1], t_eval=t)
sol2 = solve_ivp(lorenz, [a, b], [1,1,1.00001], t_eval=t)

plt.plot(sol1.y[0], sol1.y[2])
plt.xlabel("$x$")
plt.ylabel("$z$")
#plt.savefig("lorenz_xz.png")
plt.show()