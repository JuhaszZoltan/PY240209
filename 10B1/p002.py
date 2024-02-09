# szélsőérték meghatározás algoritmusa

#                   0  1  2  3  4
szamok:list[int] = [3, 2, 4, 1, 5]

minimum_index:int = 0
for index in range(1, len(szamok)):
    if szamok[index] < szamok[minimum_index]:
        minimum_index = index
print(f'legkisebb elem indexe: {minimum_index}')
print(f'legkisebb érték: {szamok[minimum_index]}')

maximum_index:int = 0
for index in range(1, len(szamok)):
    if szamok[index] > szamok[maximum_index]:
        maximum_index = index
print(f'a legnagyobb elem indexe: {maximum_index}')
print(f'a legnagyobb értéke: {szamok[maximum_index]}')