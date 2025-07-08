import threading
import time

def primzahl_ueberpruefung(zahl):
    # Bekannte Primzahlen innerhalb der Zahlen 1-100, um viel Rechenarbeit zu sparen.
    # Erklärung: Wenn eine Zahl durch 6 teilbar ist, ist sie auch durch 3 und 2 teilbar
    # Die Überprüfung von reinen prim-teilern reicht daher aus.
    # Vorüberprüfung durch bekannte Primzahlen
    bekannte_primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    is_primzahl = True
    for primzahl in bekannte_primzahlen:
        if zahl % primzahl == 0 and zahl != primzahl:
            is_primzahl = False
            break
    # Wenn die Zahl größer als die größte bekannte Primzahl ist,
    # überprüfen wir weitere mögliche ungerade Teiler
    # Wir brauchen nur Teiler, bis maximal zu der Wurzel, da x^2=x*x
    # Das heißt, wenn ein Teiler größer wird als x, wird der andere kleiner als x
    # Das heißt wir müssen maximal bis x überprüfen, also die Wurzel der Zahl
    if is_primzahl and zahl > bekannte_primzahlen[-1]:
        root1 = round(zahl ** 0.5)
        ungeradeTeilermenge1 = set(range(max(bekannte_primzahlen[-1] + 1, 3), round(root1) + 1, 2))
        for i in ungeradeTeilermenge1:
            if zahl % i == 0:
                is_primzahl = False
                break

    return is_primzahl

def berechne_primzahl(zahl):
    result = [None]
    def worker():
        result[0] = primzahl_ueberpruefung(zahl)
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join(timeout=60)  # Timeout nach 60 Sekunden
    if thread.is_alive():
        print("Berechnung abgebrochen")
        return None
    else:
        return result[0]
# Ausgabe des Ergebnisses
zahl = int(input("Gebe eine Zahl ein, von der du denkst, sie wäre eine Primzahl, Alter: "))
result = berechne_primzahl(zahl)
if result is not None:
    if result and zahl > 1:
        print(zahl, "ist eine Primzahl Alter! Super!")
    else:
        print(zahl, "ist keine Primzahl Alter!")
