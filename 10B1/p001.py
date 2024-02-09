szamok:list[int] = [3, 2, 4, 1, 5]

osszeg:int = 0
for szam in szamok:
    osszeg += szam
print(f'számok összege: {osszeg}')

db:int = 0
for szam in szamok:
    if szam % 2 == 0:
        db += 1
print(f'páros elemek száma: {db}')