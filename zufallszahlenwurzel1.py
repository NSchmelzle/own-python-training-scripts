#----------------------------------------------------------------
# Dateiname: Zufallszahlenwurzel1.py
# Zufallszahlen Quadrahtwurzel
# Autor: Nikhil Schmelzle
# Letzte Änderung: 04.07.2025
#----------------------------------------------------------------
# Teil a) Importieren der benötigten Module
import random  # Für das Erzeugen von Zufallszahlen
import math    # Für mathematische Funktionen wie Quadratwurzel

# Teil b) Funktion zur Erzeugung einer Liste mit n Zufallszahlen von 1 bis 100
def erzeuge_zufallszahlen_liste(n):
    # List Comprehension erzeugt eine Liste mit n Zufallszahlen zwischen 1 und 100
    return [random.randint(1, 100) for _ in range(n)]

# Teil c) Funktion zur Berechnung der Quadratwurzeln jeder Zahl in einer Liste
def berechne_wurzeln(liste):
    # Für jede Zahl in der Eingabeliste wird die Quadratwurzel berechnet
    return [math.sqrt(zahl) for zahl in liste]

# Teil d) Funktion zur Erzeugung einer sortierten Tupelliste (Zahl, Quadratwurzel)
def sortiere_und_erzeuge_tupel(liste):
    # Liste mit Tupeln (Originalzahl, Quadratwurzel)
    tupel_liste = [(zahl, math.sqrt(zahl)) for zahl in liste]
    # Sortieren nach dem Wert der Quadratwurzel (x[1])
    return sorted(tupel_liste, key=lambda x: x[1])

# Teil e) Funktion zur Erstellung eines Dictionaries aus der Tupelliste
def erstelle_dictionary(tupel_liste):
    # Dictionary Comprehension: Zahl → Quadratwurzel
    return {tupel[0]: tupel[1] for tupel in tupel_liste}

# Teil f) Hauptfunktion zur Steuerung des Programmablaufs
def main():
    # Schritt 1: Erzeuge Liste mit 10 Zufallszahlen
    zufallszahlen_liste = erzeuge_zufallszahlen_liste(10)

    # Schritt 2: Berechne die Quadratwurzeln der Zufallszahlen (optional für spätere Nutzung)
    wurzeln_liste = berechne_wurzeln(zufallszahlen_liste)

    # Schritt 3: Erzeuge Tupel (Zahl, Quadratwurzel) und sortiere nach Quadratwurzel
    tupel_liste = sortiere_und_erzeuge_tupel(zufallszahlen_liste)

    # Schritt 4: Erzeuge ein Dictionary aus der sortierten Tupelliste
    dictionary = erstelle_dictionary(tupel_liste)

    # Schritt 5: Gib das Ergebnis-Dictionary aus
    print("Erzeugtes Dictionary (Zahl → Quadratwurzel):")
    print(dictionary)

# Teil g) Ausführen der Hauptfunktion
main()
