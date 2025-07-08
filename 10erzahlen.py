# Benutzer bitten, eine ganze Zahl einzugeben
zahl1 = int(input("Bitte gib eine ganze Zahl ein: "))

# Überprüfen, ob die Zahl kleiner als 10, gleich 10 oder größer als 10 ist
if zahl1 < 10:
    print("Die Zahl ist kleiner als 10.")
elif zahl1 == 10:
    print("Die Zahl ist genau 10.")
else:
    print("Die Zahl ist größer als 10.")

# Liste von Zahlen von 1 bis zur eingegebenen Zahl ausgeben
for i in range(1, zahl1 + 1):
    print(i)