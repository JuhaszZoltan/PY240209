from random import randint

szamok:list[int] = []

for _ in range(10):
    szamok.append(randint(0, 9))

print(szamok)

# lista elemeinek összege:
osszeg:int = 0
for szam in szamok:
    osszeg += szam
print(f'elemek összege: {osszeg}')

db:int = 0
for szam in szamok:
    if szam % 2 == 0:
        db += 1
print(f'páros elemek száma: {db}')

# szélsőérték meghatározás
# minimumkiválasztás

min_index:int = 0
for i in range(1, len(szamok)):
    if szamok[i] < szamok[min_index]:
        min_index = i
print(f'a legkisebb elem: {szamok[min_index]}')
print(f'a legkisebb elem első előfordulásának indexe: {min_index}')
print(f'ez a lista {min_index + 1}. eleme')

max_index = 0
for i in range (1, len(szamok)):
    if szamok[i] > szamok[max_index]:
        max_index = i
print(f'a legnagyobb elem: {szamok[max_index]}')
print(f'a legnagyobb elem első előfordulásának indexe: {max_index}')
print(f'ez a lista {max_index + 1}. eleme')