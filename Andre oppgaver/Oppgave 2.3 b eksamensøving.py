vx = int(input("X-koordinat: "))
vy = int(input("Y-koordinat: "))

wx = 5
wy_funnet = False

for wy in range(-10,11):
    if vx*wx + vy*wy == 0:
        print(f"Vektorene v og w er ortogonale når wy = {wy}")
        wy_funnet = True
        break

if wy_funnet == False:
    print("Det finnes ingen wy, som gjør at vektor v og vektor w er ortogonale")