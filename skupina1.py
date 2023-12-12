x = input("Zadeje proměnou x: ")
y = input("Zadeje proměnou y: ")

x = int(x)
y = int(y)

print("Pro sčítání zadejte +")
print("Pro odčítání zadejte -")
print("Pro násobení zadejte *")
print("Pro dělení zadejte /")
print("Pro mocnění zadejte **")
print("Pro odmocenění zadejte /*")

znamenko = input("Zvolte si operátor: ")


if znamenko == "+":
    vysledek = x + y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "-":
    vysledek = x - y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "*":
    vysledek = x * y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)
elif znamenko == "/":
    if y != 0:
        vysledek = x / y
        vysledek = str(vysledek)
        print("Výsledek je: " + vysledek)
    else:
        print("Nemůžeš dělit nulou, ty nebýt Chack Noris.")
elif znamenko == "**":
    vysledek = x ** y
    vysledek = str(vysledek)
    print("Výsledek je: " + vysledek)