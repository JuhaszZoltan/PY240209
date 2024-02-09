# szélsőérték meghatározás algoritmusa(i):

#                    0   1  2   3  4
szamok:list[int] = [22, 11, 5, 31, 9]

minimum_index:int = 0
for index in range(1, len(szamok)):
    if szamok[index] < szamok[minimum_index]:
        minimum_index = index

print(f'legkisebb szám indexe: {minimum_index}')
print(f'legkisebb szám sorszáma a listában: {minimum_index + 1}')
print(f'legkisebb szám értéke: {szamok[minimum_index]}')

maxi:int = 0
for i in range(1, len(szamok)):
    if szamok[i] > szamok[maxi]:
        maxi = i

print(f'legnagyobb szám indexe: {maxi}')
print(f'legnagyobb szám sorszáma: {maxi + 1}')
print(f'legnagyobb szám: {szamok[maxi]}')