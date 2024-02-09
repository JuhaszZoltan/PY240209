szamok:list[int] = [11, 26, 73, 8, 62]

osszeg:int = 0
for szam in szamok:
    osszeg += szam
print(f'számok összege: {osszeg}')

db:int = 0
for szam in szamok:
    if szam % 2 == 0:
        db += 1
print(f'páros számok száma: {db}')