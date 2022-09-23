print("Milyen műveletet szeretne gyakorolni?")
print("\t1. Összeadás \n\t2. Szorzás \n\t3. Kivonás") #\t - tabulátor; \n - új sor

valasz = input("Választás (1-3): ")
print(valasz)

#ez egy komment

a = 2
b = 5

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(b/a)
print(b%a) #maradékos osztás

szoveg = "alma"
szoveg2 = "banán"

print(szoveg + szoveg2)

szoveg = "körte"

print("Alma-", szoveg)

db = 0
ok = 0
print(db)
db += 5 # db = db + 5
print(db)
db -= 1 # db = db - 1
print(db)
db *= 2 # db = db * 2
print(db)
db /= 3 # db = db / 3
print(db)

nev = input("Hogy hívnak?")
print("Hello ", nev)
