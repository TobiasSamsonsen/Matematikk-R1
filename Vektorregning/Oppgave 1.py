# Lag et program som regner ut lengden av en vektor v = [x,y]
# Lag et program som finner avstanden mellom to punkter A(xa, ya) og B(xb,yb)
# Rund av svarene til 2 desimaler

# Oppgave a
x = float(input("x = "))
y = float(input("y = "))

absoluttverdi = (x**2 + y**2)**(1/2)
vektor = [x,y]

print(f"Lengden til vektor {vektor} er {absoluttverdi:0.2f}")


# Oppgave b
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

lengde = (((x2-x1)**2)+((y2-y1)**2))**0.5

print(f"Lengden mellom punktene er = {lengde:0.2f}")