#random számokhoz kell
from random import randint

dobasokszama = int(input("1. feladat\nAdd meg a dobások számát! "))
Dobasok = []
szoveg = "alma"
atlag = 0
#atlag = atlag + 1 -> atlag += 1
hatos = 0
paros = 0
dobas = 1

while dobas <= dobasokszama:
    Dobasok.append(randint(1,6))#hozzáadjuk a dobásokat a Dobasok listához
    atlag += Dobasok[dobas-1]   #atlagszamitashoz összeadjuk a dobásokat
    if Dobasok[dobas-1] == 6:   #ha 6ot dobtunk
        hatos += 1               #hatos változót növeljük 1-el
    if Dobasok[dobas-1] % 2 == 0:#ha párost dobtunk
        paros+= 1               #paros változót növeljük 1-el
    dobas += 1                  #dobas változót növeljük, hogy tudjuk, hanyadik dobásnál járunk

print(f"\n2. feladat\n{Dobasok}")#kiírja a Dobasok lista elemeit
sum = atlag #sum változóban lez a dobások összege
atlag /= dobasokszama   #átlag változóban lesz az összes dobás összege és a dobások számának hányadosa
print(f"\n3. feladat\nA játékos átlagosan {atlag} mezőt, összesen {sum} mezőt haladt előre.")

print('\n4. feladat')
if hatos == 0:
    print('A játékos sajnos egy alkalommal sem dobott hatost.')
else:
    print(f'A játékos {hatos} alkalommal dobott hatost.')

print(f'\n5. feladat\nA játékos {paros} alkalommal dobott páros számot.')

kevesebb = 0
print('\n6. feladat')
#dobasokszama -2-ig megyünk, hogy ne fussunk túl a tömbön
#-1 -> mi 1 től számolunk a gépnek az a 0.
#-1 -> utolsó elemet nem tudjuk mivel összehasonlítani, mert nincs utána több elem
#[0,1,2,3,4,5] 6 elem
for i in range(dobasokszama):
    if Dobasok[i] < Dobasok[i+1]:
        kevesebb += 1
print(f'A játékos {kevesebb} alkalommal dobott kevesebbet, mint előző körben.')