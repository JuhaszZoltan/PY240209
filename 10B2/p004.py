# linker (python specifikus verzió)

szavak:list[str] = ['cica', 'kabát', 'mókus', 'bicikli', 'egér']
keresett_szo:str = input('írd be a keresett szót: ')

for i in range(len(szavak)):
    if szavak[i] == keresett_szo:
        print(f'van találat, indexe: {i}')
        break
else: print('nincs találat')

print('ez a kövi sor, ami lefut')