import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Progmod - Numerisk derivasjon\heistur_kjemi_fysikk.txt")
p = data["height_m"]
t = data["time_s"]
v = [] # fart i m/s
a = [] # akselerasjon i m/s^2

for i in range(len(p)-1):
  dt = t[i+1] - t[i]
  fart = (p[i+1] - p[i])/dt
  v.append(fart)
  
for i in range(len(v)-1):
    dt = t[i+1] - t[i]
    akselerasjon = (v[i+1] - v[i])/dt
    a.append(akselerasjon)

v.append(None)
a.append(None)
a.append(None)

data["fart"] = v
data["akselerasjon"] = v

plt.subplot(3,1,1)
plt.ylabel("Posisjon (m)")
plt.plot(t, p, color = "limegreen")
plt.subplot(3,1,2)
plt.ylabel("Fart (m)")
plt.ylim(-1,1)
plt.plot(t, v, color = "navy")
plt.subplot(3,1,3)
plt.ylabel("Akselerasjon (m)")
plt.plot(t, a, color = "firebrick")
plt.ylim(-1,1)
plt.xlabel("Tid (s)")
plt.tight_layout()
plt.show()