#2024 középszint minta
#from random import randint
import random as r

print("Melyik műveletet szeretnéd gyakorolni?")
print("\t1. Összeadás\n\t2. Kivonás\n\t3. Szorzás") # \n sortörés \t tabulátor

valasz = int(input("Választás (1-3): "))

db = 0 # kezdőérték, próbálkozások száma
ok = 0 # kezdőérték, jó válaszok

while ok < 5:
    db += 1
    a = r.randint(1,11) # a = ok; a *= 2; a += 1
    b = r.randint(1,11) # b = db; b %= 10; b += 1

    if valasz == 1: # +
        print(a, "+", b)
        d = a+b
    elif valasz == 2: # -
        print(a, "-", b)
        d = a-b
    elif valasz == 3: # *
        print(a, "*", b)
        d = a*b

    c = int(input())

    if c == d:
        print("Helyes!")
        ok += 1 #ok+1
    else:
        print("Hibás")
# while ciklus vége
print("Gratulálok!")
print("Sikerült ", ok," helyes műveletet elvégezni ", db," próbálkozásból." )

