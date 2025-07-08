# Eingabe einer Zahl, die möglicherweise eine Primzahl ist
input1 = int(input("Gebe eine Zahl ein, von der du denkst, sie wäre eine Primzahl, Alter: "))

# Berechnung der Wurzel der Zahl
root1 = round(input1 ** 0.5)

# Erstellung einer Menge von ungeraden möglichen Teilern
# Wir starten bei 3, da 1 jede Zahl teilt und 2 bereits ausgeschlossen ist
# Wir brauchen nur Teiler, bis maximal zu der Wurzel, da x^2=x*x und nicht größer.
ungeradeTeilermenge1 = set(range(3, round(root1) + 1, 2))

# Überprüfung, ob die Zahl eine Primzahl ist
# Wir müssen überprüfen, ob die Zahl durch irgendeinen der ungerdaen Teiler teilbar ist
is_primzahl = True

# Überprüfung für den Teiler 2
if input1 % 2 == 0 and input1 > 2:
    is_primzahl = False

# Überprüfung für ungerade Teiler
for i in ungeradeTeilermenge1:
    if input1 % i == 0:  # Wenn die Zahl durch i teilbar ist
        is_primzahl = False
        break  # Wir können die Schleife abbrechen, da wir bereits wissen, dass die Zahl keine Primzahl ist

# Ausgabe des Ergebnisses
if is_primzahl and input1 > 1:  # 1 ist keine Primzahl
    print(input1, "ist eine Primzahl Alter! Super!")
else:
    print(input1, "ist keine Primzahl Alter!")
