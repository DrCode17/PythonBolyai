
sum = 0
for i in range (101):
    sum += i
print(sum)

sum = 0
for i in range(1,101): #100-szor fut le
    if i % 2 == 0:
        sum += i
print(sum)

words = ["apple", "cookie", "pie"]
for word in words:
    print(word)

print(word)

colour = ["red", "blue", "green"]
#words = ["apple", "cookie", "pie"]
for c in colour:
    for w in words:
        print(c+" "+w)

szam = 1
while szam != 101: # 50-szer fut le
    print(szam)
    szam += 2

feltetel = True #False
while feltetel:
    print("Lefusson még egyszer?")
    valasz = input()
    if valasz == "nem":
        feltetel = False

print("Vége!")

for i in range(11):
    for j in range(11):
        print(i*j)
    print()

ok = 0
jo = 0
while jo < 5:
    print("Jó vagy rossz?")
    valasz = input()
    if valasz == "rossz":
        jo -= 1
    elif valasz == "jo":
        jo += 1
        ok += 1
print ("Ciklus vége, ", ok, " jó válaszod volt.")
