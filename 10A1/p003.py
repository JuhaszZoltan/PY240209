# linker ("csak" pythonban)

szavak:list[str] = ['cica', 'kutya', 'ló', 'delfin', 'sün', 'hörcsög']

keresett_szo:str = input('írd be mit keresel: ')

for index in range(len(szavak)):
    if szavak[index] == keresett_szo:
        print(f'a keresett szó indexe: {index}')
        break
else: print('nincs benne a keresett szó')

print('itt a vége')