# lineáris keresés algoritmusa (általános)

allatok:list[str] = ['ló', 'cica', 'patkány', 'kutya', 'pingvin']
keresett_allat:str = input('írj be egy állatfajtát: ')
index:int = 0

while index < len(allatok) and allatok[index] != keresett_allat:
    index += 1
if index < len(allatok):
    print(f'van találat, indexe: {index}')
else:
    print('nincs találat')