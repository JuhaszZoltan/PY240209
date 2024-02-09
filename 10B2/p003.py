# lineáris keresés algoritmusa (általános)

szavak:list[str] = ['cica', 'kabát', 'mókus', 'bicikli', 'egér']
keresett_szo:str = input('írd be a keresett szót: ')

index:int = 0
while index < len(szavak) and szavak[index] != keresett_szo:
    index += 1
if index < len(szavak):
    print(f'van eredmény, a {keresett_szo} indexe: {index}')
else:
    print('a keresett szó nincs benne a listában')