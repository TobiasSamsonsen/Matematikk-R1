from matplotlib import pyplot as plt
import numpy as np

def T(t):
    return 70*np.e**(-0.065*t)
    
def derivert(f, x, dx=1E-6):
    return (f(x+dx)-f(x))/dx

t = np.linspace(0, 60, 1000)

print(f"Temperaturen synker med {derivert(T, t[41])} for element nr. 42 i lista over verdier for t")

plt.plot(t, T(t), label="T(t)")
plt.plot(t, derivert(T, t), label="T'(t)")
plt.legend()
plt.grid()
plt.show()