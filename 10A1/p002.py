# lineáris keresés algoritmusa

szavak:list[str] = ['cica', 'kutya', 'ló', 'delfin', 'sün', 'hörcsög']

keresett_szo:str = input('írd be mit keresel: ')

index:int = 0
while index < len(szavak) and szavak[index] != keresett_szo:
    index += 1

if index < len(szavak):
    print(f'a(z) {keresett_szo} benne van a listában')
    print(f'indexe: {index} (ez a {index+1}. elem)')
else:
    print(f'a(z) {keresett_szo} nincs benne a listában')