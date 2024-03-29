from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import fsolve

# Definerer funksjonen, derivert og dobbelderivert av funksjonen

def f(x):
    return -0.6*x**3+x**2+x #Fungerer ikke med konstantledd


h = 0.00001


def df(x):
    return (f(x+h)-f(x-h))/(2*h)


def ddf(x):
    return (df(x+h)-df(x-h))/(2*h)


nplist = []

# Bruker halveringsmetoden for å finne flere nullpunkter, denne blir brukt til å finne vendepunkter

def halveringsmetoden(nedre_grense, øvre_grense, funksjon, navn):
    for i in range(1, 20):
        x = (nedre_grense + øvre_grense)/2
        if funksjon(nedre_grense)*funksjon(x) < 0:
            øvre_grense = x
        else:
            nedre_grense = x

    nplist.append(round(x, 2))


# Monotoniegenskapene blir lett funnet ved å bruke ekstremalpunktene som allerede er funnet
# Bare masse if-statements 

def monotoniegenskaper(ekstremalpunkter):
    for ekstremalpunkt in ekstremalpunkter:
        if ekstremalpunkt == ekstremalpunkter[0]:
            if (ekstremalpunkt + ekstremalpunkter[ekstremalpunkter.index(ekstremalpunkt)+1])/2 < 0:
                print(f"Grafen stiger når x = <<---, {round(ekstremalpunkt, 2)}>")
            else:
                print(f"Grafen synker når x = <<---, {round(ekstremalpunkt, 2)}>")
        if ekstremalpunkt == ekstremalpunkter[-1]:
            if (ekstremalpunkt + ekstremalpunkter[ekstremalpunkter.index(ekstremalpunkt)-1])/2 < 0:
                print(f"Grafen stiger når x = <{round(ekstremalpunkt, 2)}, --->>")
            else:
                print(f"Grafen synker når x = <{round(ekstremalpunkt, 2)}, --->>")
        else:
            if (ekstremalpunkt + ekstremalpunkter[ekstremalpunkter.index(ekstremalpunkt)+1])/2 > 0:
                print(
                    f"Grafen stiger når x = <{round(ekstremalpunkt, 2)}, {round(ekstremalpunkter[ekstremalpunkter.index(ekstremalpunkt)+1], 2)}>")
            else:
                print(
                    f"Grafen synker når x = <{round(ekstremalpunkt, 2)}, {round(ekstremalpunkter[ekstremalpunkter.index(ekstremalpunkt)+1], 2)}>")


# Bruker fsolve funksjonen fra scipy til å finne alle nullpunkter
# Hadde tidligere problemer med å finne flere nullpunkter med halveringsmetoden
# Brukte derfor fsolve for å finne alle nullpunkt i et intervall

def nullpunktsfinder(funksjon, navn, finnkrumning, finnmonotoni):
    nullpunkter_withduplicates = (fsolve(
        funksjon, [x for x in range(int(graf_range_start), int(graf_range_end+1))]))
    nullpunkter = list(dict.fromkeys([round(x, 5)
                       for x in nullpunkter_withduplicates]))
    if finnkrumning:
        for x in nullpunkter:
            if ddf(x) < 0:
                navn = "Toppunkt"
            else:
                navn = "Bunnpunkt"
            print(f"{navn} = ({round(x, 2)}, {round(f(x), 2)})")
    if finnmonotoni:
        monotoniegenskaper(nullpunkter)
    else:
        nullpunktliste = (
            [f"{navn} = ({round(x, 2)}, {round(f(x), 2)})" for x in nullpunkter])
        for i in nullpunktliste:
            print(i)
    for i in nullpunkter:
        pp(i, f(i))


# Plotter punkt på grafen
def pp(x, y):
    plt.plot(x, y, marker=".", markersize=10)


graf_range_start = float(input("Startverdi: "))
graf_range_end = float(input("Sluttverdi: "))
print("-----------------------------")

# Bruker funksjonen "nullpunktsfinder" for å finne nullpunktene på en graf
# I dette tilfellet finner vi nullpunktet til f(x), altså finner vi nullpunktene
nullpunktsfinder(f, "Nullpunkt", finnkrumning=False, finnmonotoni=False)

# Bruker funksjonen "nullpunktsfinder" for å finne nullpunktene på en graf
# I dette tilfellet finner vi nullpunktet til den deriverte: df, altså finner vi ekstremalpunktene
nullpunktsfinder(df, "Ekstremalpunkt", finnkrumning=True, finnmonotoni=True)

# Bruker funksjonen "halveringsmetoden" for å finne nullpunktene på en graf
# I dette tilfellet finner vi nullpunktet til den dobbelderiverte: ddf, altså finner vi ekstremalpunktene
for i in range(int(graf_range_start)-10, int(graf_range_end)):
    halveringsmetoden(i, graf_range_end, ddf, "Vendepunkt")
# Tar siden funksjonen finner det samme punktet flere ganger tar vi vekk alle duplikater
nplist_no_duplicates = list(dict.fromkeys(nplist))
# Siste verdi i lista er ikke et bunnpunkt, men graf_range_end
nplist_no_duplicates.remove(nplist_no_duplicates[-1])
for x in nplist_no_duplicates:
    print((f"Vendepunkt = ({x:0.2f}, {round(f(x), 2)})"))
    pp(x, f(x))


# lager en liste med 1000 verdier mellom start og sluttverdiene
x = np.linspace(graf_range_start, graf_range_end, 1000)

# Plotter grafer og viser de til brukeren
plt.plot(x, f(x), label="f(x)")
plt.plot(x, df(x), label="df(x)")
plt.plot(x, ddf(x), label="ddf(x)")
plt.legend()
plt.grid()
plt.show()
