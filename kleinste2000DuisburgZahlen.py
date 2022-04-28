z = 0
duisburg_zahl = 7
liste = []
qs = 0
while z >= 0:
    for i in str(z):
        qs += int(i)
    if qs == duisburg_zahl:
        print(z)
        liste.append(z)
    if len(liste) > 2000:
        break

    qs = 0
    z = int(z)
    z += 1
