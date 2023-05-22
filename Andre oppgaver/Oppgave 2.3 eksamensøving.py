xu = -3
yu = 1
xv = int(input("Skriv inn x-koordinaten: "))
yv = int(input("Skriv inn y-koordinaten: "))

if xu*xv + yu*yv == 0:
    print("Vektorene u og v er ortogonale")
else:
    print("Vektorene u og v er ikke ortogonale")