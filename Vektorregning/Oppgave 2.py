# Lag et program som avgjør om to vektorer er ortogonale.
# Hvis de ikke er ortogonale, skal programmet fortelle om vinkelen mellom dem er spiss eller stump.

# Lag et program som avgjør om to vektorer er ortogonale eller paralelle eller ingen av delene

# Oppgave a
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

skalarprodukt = x1*x2 + y1*y2

if skalarprodukt == 0:
    print("Vektorene er ortogonale")
elif skalarprodukt < 0:
    print("Vinkelen mellom vektorene er stump")
else:
    print("Vinkelen mellom vektorene er spiss")
    

# Oppgave b
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

t = 0
skalarprodukt = x1*x2 + y1*y2

if skalarprodukt == 0:
    print("Vektorene er ortogonale")
else:
    while t < 9999:
        if x1 == x2 and y1 == y2:
            print("Vektorene er parallelle")
            break
        t += 1
