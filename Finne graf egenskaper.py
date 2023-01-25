from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import fsolve

#Toppunkt, Bunnpunkt, monotoniegenskaper, krumning og vendepunkt

def f(x):
    return -0.6*x**4-1.3*x**3+1.8*x**2+1.8*x

h = 0.00001
def df(x):
    return (f(x+h)-f(x-h))/(2*h)

def ddf(x):
    return (df(x+h)-df(x-h))/(2*h)

nplist = []
def halveringsmetoden(nedre_grense, øvre_grense, funksjon, navn):
    
    for i in range(1,20):
        x = (nedre_grense + øvre_grense)/2
        if funksjon(nedre_grense)*funksjon(x) < 0:
            øvre_grense = x
        else:
            nedre_grense = x
            
    nplist.append(round(x,2))
    nplist_no_duplicates = list(dict.fromkeys(nplist))
    nplist_no_duplicates.remove(nplist_no_duplicates[-1])
    for i in nplist_no_duplicates:
        print((f"{navn} = ({x:0.2f}, {round(f(x), 2)})"))
        pp(x, f(x))

def bigfuckingfunction(funksjon, navn, finnkrumning):
    nullpunkter_withduplicates = (fsolve(funksjon, [x for x in range(int(graf_range_start), int(graf_range_end+1))]))
    nullpunkter = list(dict.fromkeys([round(x, 5) for x in nullpunkter_withduplicates]))
    if finnkrumning:
        for x in nullpunkter:
            if ddf(x) < 0:
                navn = "Toppunkt"
            else:
                navn = "Bunnpunkt"
            print(f"{navn} = ({round(x, 2)}, {round(f(x), 2)})")
    else:
        nullpunktliste = ([f"{navn} = ({round(x, 2)}, {round(f(x), 2)})" for x in nullpunkter])
        for i in nullpunktliste:
            print(i)
    for i in nullpunkter:
        pp(i, f(i))
    
def pp(x, y):
    plt.plot(x, y, marker=".", markersize=10, markerfacecolor="red")

graf_range_start = float(input("Startverdi: "))
graf_range_end = float(input("Sluttverdi: "))

# Bruker funksjonen "bigfuckingfunction" for å finne nullpunktene på en graf
# I dette tilfellet finner vi nullpunktet til f(x), altså finner vi nullpunktene
bigfuckingfunction(f, "Nullpunkt", finnkrumning=False)
    
# Bruker funksjonen "bigfuckingfunction" for å finne nullpunktene på en graf
# I dette tilfellet finner vi nullpunktet til den deriverte: df, altså finner vi ekstremalpunktene
bigfuckingfunction(df, "Ekstremalpunkt", finnkrumning=True)

# Bruker funksjonen "halveringsmetoden" for å finne nullpunktene på en graf
# I dette tilfellet finner vi nullpunktet til den dobbelderiverte: ddf, altså finner vi ekstremalpunktene
for i in range(int(graf_range_start)-10, int(graf_range_end)):
    halveringsmetoden(i, graf_range_end, ddf, "Vendepunkt")
    

x = np.linspace(graf_range_start, graf_range_end, 1000) #lager en liste med 1000 verdier mellom start og sluttverdiene

plt.plot(x, f(x), label="f(x)")
plt.plot(x, df(x), label="df(x)")
plt.plot(x, ddf(x), label="ddf(x)")
plt.legend()
plt.grid()
plt.show()
