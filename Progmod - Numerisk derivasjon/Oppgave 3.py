import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return x**3+1/3*x

def derivert(f, x, dx=1E-6):
    return (f(x+dx)-f(x))/dx

def g(x):
    return derivert(f, x)

def h(x):
    return derivert(g, x)


x = np.linspace(0,10,100)

plt.plot(x, f(x), label="f(x)")
plt.plot(x, g(x), label="f'(x)")
plt.plot(x, h(x), label="f''(x)")
plt.legend()
plt.grid()
plt.show()