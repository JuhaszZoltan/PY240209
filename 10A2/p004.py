# python specifikus megoldás:

allatok:list[str] = ['kutya', 'cica', 'hörcsög', 'ló', 'pingvin']
keresett_allat:str = input('írd be mit keresel: ')

for i in range(len(allatok)):
    if allatok[i] == keresett_allat:
        print(f'van találat, idenxe: {i}')
        break
else: print('nincs találat')

print('itt a kövi sor, ami lefut')