#----------------------------------------------------------------
# Dateiname: Taschenrechner_Schmelzle_pruefung1.py
# Taschenrechner
# Autor: Nikhil Schmelzle
# Letzte Änderung: 26.06.2025
#----------------------------------------------------------------
# Eingabe und Wahl der Operation
print("Hallo! Willkommen zu meinem Taschenrechner. (einfache Operation zweier Zahlen.)")
print("Bitte wähle was du berechnen willst:")
print("A = Addition")
print("S = Subtraktion")
print("M = Multiplikation")
print("D = Division")
print("bitte Beachte: Dezimal = Punkt, nicht Komma!") # Kommentar, da ich an diesem Punkt noch nicht verstehe, wie ich einen falschen Input gut umwandeln kann.
task1 = input("Hallo Prüfer. Was möchtest du berechnen? A S M D: ") # Eingabe und Ausschluss zur evtl neu Eingabe
while task1 not in ["A", "S", "M", "D"]: 
    print("Ungültige Eingabe. Bitte wähle aus folgenden Optionen aus: A, S, M, D")
    task1 = input("Bitte wähle eine Operation A S M D: ")

zahl1 = float(input("Gebe die erste Zahl ein: ")) # Eingabe als Dezimal, keine Umwandlung, da nicht Teil der Aufgabe.

zahl2 = float(input("Gebe die zweite Zahl ein: ")) #  Eingabe der zweiten Zahl

if task1 == "A":            # If Elif schleife zur Wahl der korrekten Berechnung
    ergebnis = zahl1 + zahl2
    print(f"Das Ergebnis der Addition ist: {ergebnis}")
elif task1 == "S":
    ergebnis = zahl1 - zahl2
    print(f"Das Ergebnis der Subtraktion ist: {ergebnis}")
elif task1 == "M":
    ergebnis = zahl1 * zahl2
    print(f"Das Ergebnis der Multiplikation ist: {ergebnis}")
elif task1 == "D":
    if zahl2 != 0: # Ausschluss Zahl 2 ungleich Null, ansonsten Fehlermeldung, weil Teilen durch Null nicht möglich.
        ergebnis = zahl1 / zahl2
        print(f"Das Ergebnis der Division ist: {ergebnis}")
    else:
        print("Fehler! Division durch Null ist nicht möglich.") # An der Stelle würde ich gerne eine Neueingabe fordern, weiß aber nicht wie.
