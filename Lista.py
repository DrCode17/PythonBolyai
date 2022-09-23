Lista = [] # üres lista
Lista1 = ['Python', "C#", 'C++']

#végéhez hozzá fűzi
Lista1.append('valami') #['Python', "C#", 'C++','valami']

#sorba rendezi
Lista1.sort()#[ "C#", 'C++','Python','valami']

# vissza fele sorba rendezi
Lista1.reverse() #[ 'valami','Python',"C#", 'C++']

#kitörli
Lista1.clear() #[]

hetekszama = int(input("Hetek száma="))
kivanttestomeg = float(input("Elérni kívánt testtömeg (kg)="))

elerte = 0
hetek = 1
while hetek < hetekszama+1:
    suly = float(input(f'{hetek}. héten='))
    Lista.append(suly)
    if elerte == 0:
        if suly <= kivanttestomeg:
            elerte = hetek
    hetek += 1

if elerte != 0:
    print(f'Mari néni a(z) {elerte}. héten érte el a célt.')
else:
    print('Sajnos Mari néni nem érte el a célját')
nott = 0
#Lista[0,1,2,3,4] 5elem
for i in range(hetekszama -2):
    if Lista[i] < Lista[i+1]:
        nott += 1
print(f'A tömege {nott} esetben nőtt egyik hétről a másikra.')
print(Lista)
#törli a Lista 2.(3.) elemét
del Lista[2]
print(Lista)
#Törli a Lista 44.0 értékű első elemét
Lista.remove(44.0)
print(Lista)
#Megszámolja, hogy a Lista-ban hány 44.0 értékű elem van
print(Lista.count(44.0))