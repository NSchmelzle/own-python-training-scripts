#----------------------------------------------------------------
# Dateiname: Zufallszahlen2.py
# Zufallszahlen
# Autor: Nikhil Schmelzle
# Letzte Änderung: 07.07.2025
#----------------------------------------------------------------
# Teil a) Importieren des Moduls random und Erzeugen einer Liste mit 10 Zufallszahlen zwischen 1 und 100
import random

zufallszahlen = [random.randint(1, 100) for _ in range(10)]

# Ausgabe der ursprünglichen Liste zur Kontrolle
print("Ursprüngliche Zufallszahlen:", zufallszahlen)

# Teil b) Funktion zum Sortieren der Liste und Zählen der Elemente
def sortiere_und_zähle(zahlenliste):
    zahlenliste.sort()  # Sortiert die Liste aufsteigend (in-place)
    return len(zahlenliste)  # Gibt die Anzahl der Elemente zurück

# Aufruf der Funktion und Speichern der Anzahl
anzahl_elemente = sortiere_und_zähle(zufallszahlen)

# Ausgabe der sortierten Liste zur Kontrolle
print("Sortierte Liste:", zufallszahlen)
print("Anzahl der Elemente:", anzahl_elemente)

# Teil c) Erstellen einer neuen Liste mit Tupeln (Zahl, Quadrat der Zahl)
tupel_liste = [(zahl, zahl**2) for zahl in zufallszahlen]

# Teil d) Ausgabe der Tupel in lesbarer Form
for zahl, quadrat in tupel_liste:
    print(f"Die Zahl {zahl} hat das Quadrat {quadrat}")

# Teil e) Kontrollstruktur zur Prüfung der Anzahl der Elemente
if anzahl_elemente > 5:
    print("Mehr als 5 Elemente")
else:
    print("5 oder weniger Elemente")
