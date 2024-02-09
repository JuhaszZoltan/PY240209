# linker (python exclusive version)

allatok:list[str] = ['ló', 'cica', 'patkány', 'kutya', 'pingvin']
keresett_allat:str = input('írj be egy állatfajtát: ')

for i in range(len(allatok)):
    if allatok[i] == keresett_allat:
        print(f'van találat, indexe: {i}')
        break
else: print('nincs találat')

print('ez')