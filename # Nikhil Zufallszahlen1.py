#----------------------------------------------------------------
# Dateiname: Zufallszahlen1.py
# Zufallszahlen
# Autor: Nikhil Schmelzle
# Letzte Änderung: 06.07.2025
#----------------------------------------------------------------
# Teil a) Importieren der benötigten Module
import random  # Für die Generierung von Zufallszahlen
import math    # Wird hier nicht verwendet, aber laut Aufgabenstellung mit importieren

# Teil b) Funktion zur Generierung einer Liste von Zufallszahlen
def erzeuge_zufallszahlen_liste(anzahl, max_wert):
    # Erstellt eine Liste mit 'anzahl' Zufallszahlen zwischen 1 und 'max_wert'
    return [random.randint(1, max_wert) for _ in range(anzahl)]

# Teil c) Funktion zur Berechnung des Durchschnitts einer Zahlenliste
def berechne_durchschnitt(zahlenliste):
    # Berechnet den Mittelwert (arithmetisches Mittel)
    return sum(zahlenliste) / len(zahlenliste)

# Teil d) Funktion zum Sortieren und Teilen der Liste in zwei Hälften
def sortiere_und_teile(zahlenliste):
    zahlenliste.sort()  # Sortiert die Liste in-place (aufsteigend)
    mitte = len(zahlenliste) // 2  # Berechnet die "Mitte" der Liste

    if len(zahlenliste) % 2:
        # Wenn ungerade Anzahl: mittleres Element geht in die erste Hälfte
        return zahlenliste[:mitte + 1], zahlenliste[mitte + 1:]
    else:
        # Wenn gerade Anzahl: exakt in zwei Hälften teilen
        return zahlenliste[:mitte], zahlenliste[mitte:]

# Teil e) Erzeugen einer Liste mit 10 Zufallszahlen zwischen 1 und 100
zufallszahlen = erzeuge_zufallszahlen_liste(10, 100)

# Teil f) Ausgabe der Zufallszahlenliste
print("Zufallszahlen:", zufallszahlen)

# Teil g) Berechnung und Ausgabe des Durchschnitts
durchschnitt = berechne_durchschnitt(zufallszahlen)
print("Durchschnitt:", durchschnitt)

# Teil h) Sortieren und Teilen der Liste in zwei Hälften
erste_haelfte, zweite_haelfte = sortiere_und_teile(zufallszahlen)
print("Erste Hälfte:", erste_haelfte)
print("Zweite Hälfte:", zweite_haelfte)
