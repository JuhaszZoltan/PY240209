# szélsőérték meghatározás algoritmusa

szamok:list[int] = [4, 2, 5, 1, 3]

minimum_index:int = 0
for index in range(1, len(szamok)):
    if szamok[index] < szamok[minimum_index]:
        minimum_index = index

print(f'a legkisebb érték első előfordulásának indexe: {minimum_index}')
print(f'a legkisebb érték: {szamok[minimum_index]}')
print(f'ez a szám a lista {minimum_index + 1}. eleme')

maximum_index:int = 0
for index in range(1, len(szamok)):
    if szamok[index] > szamok[maximum_index]:
        maximum_index = index
print(f'a legnagyobb elem első előfordulásának indexe: {maximum_index}')
print(f'a legnagyobb elem: {szamok[maximum_index]}')
print(f'ez a szám a lista {maximum_index + 1}. eleme')