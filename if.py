
pontok = int(input("Hány pontot szereztél?"))
a = 2

if pontok < 50:
    print("1-es")
    a += 2
elif pontok < 60:
    print("2-es")
    a *= 2
elif pontok < 70:
    print("3-as")
    a *= 4
elif pontok < 85:
    print("4-es")
    a /= 2
else:
    print("5-ös")

print(a)

print("1. Összeadás\n2. Szorzás\n3. Kivonás")
valasz = int(input("Válasza(1-3): "))

a = 5
b = 10

if valasz == 1:
    print(a , "+", b)
    valasz = int(input("Helyes válasz: "))
    if valasz == a+b:
        print("Helyesen válaszoltál")
    else:
        print("Helytelen válasz")
elif valasz == 2:
    print(a, "*", b)
    valasz = int(input("Helyes válasz: "))
    if valasz == a * b:
        print("Helyesen válaszoltál")
    else:
        print("Helytelen válasz")
elif valasz == 3:
    print(a, "-", b)
    valasz = int(input("Helyes válasz: "))
    if valasz == a - b:
        print("Helyesen válaszoltál")
    else:
        print("Helytelen válasz")
else:
    print("Nincs ilyen művelet")
