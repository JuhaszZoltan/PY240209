# lineáris keresés algoritmusa (általános)

allatok:list[str] = ['kutya', 'cica', 'hörcsög', 'ló', 'pingvin']
keresett_allat:str = input('írd be mit keresel: ')

index:int = 0
while index < len(allatok) and allatok[index] != keresett_allat:
    index += 1

if index < len(allatok):
    print(f'a {keresett_allat} a lista {index}. indexű eleme')
else:
    print(f'a keresett allat nincs benne a listába')