# Fordere den Benutzer auf, eine Operation auszuwählen
print("Hallo! Willkommen zu meinem Taschenrechner.")
print("Bitte wähle eine Operation:")
print("A für Addition")
print("S für Subtraktion")
print("M für Multiplikation")
print("D für Division")

operation = input("Bitte gib deine Wahl ein (A, S, M, D): ")

# Überprüfe, ob die Eingabe gültig ist
while operation.upper() not in ["A", "S", "M", "D"]:
    print("Ungültige Eingabe. Bitte wähle aus folgenden Optionen aus: A, S, M, D")
    operation = input("Bitte gib deine Wahl ein (A, S, M, D): ")

# Frage den Benutzer nach zwei Zahlen
zahl1 = input("Bitte gib die erste Zahl ein: ")
while not zahl1.replace('.', '', 1).replace('-', '', 1).isdigit():
    print("Ungültige Eingabe! Bitte gib eine Zahl ein.")
    zahl1 = input("Bitte gib die erste Zahl ein: ")
zahl1 = float(zahl1)

zahl2 = input("Bitte gib die zweite Zahl ein: ")
while not zahl2.replace('.', '', 1).replace('-', '', 1).isdigit():
    print("Ungültige Eingabe! Bitte gib eine Zahl ein.")
    zahl2 = input("Bitte gib die zweite Zahl ein: ")
zahl2 = float(zahl2)

# Führe die ausgewählte Operation durch
if operation.upper() == "A":
    ergebnis = zahl1 + zahl2
    print(f"Das Ergebnis der Addition ist: {ergebnis}")
elif operation.upper() == "S":
    ergebnis = zahl1 - zahl2
    print(f"Das Ergebnis der Subtraktion ist: {ergebnis}")
elif operation.upper() == "M":
    ergebnis = zahl1 * zahl2
    print(f"Das Ergebnis der Multiplikation ist: {ergebnis}")
elif operation.upper() == "D":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
        print(f"Das Ergebnis der Division ist: {ergebnis}")
    else:
        print("Fehler! Division durch Null ist nicht möglich.")