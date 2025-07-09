#--------------------------------------------
# Dateiname: kontakte.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 09.07.2025
#--------------------------------------------

import json
import os

# Funktion zum Speichern eines einzelnen Kontakts in einer JSON-Datei
def speichere_kontakt(name, email, telefon):
    kontakt = {"Name": name, "E-Mail": email, "Telefon": telefon}
    dateiname = "kontakte.json"

    try:
        # Falls es die Datei schon gibt, laden wir sie zuerst
        if os.path.exists(dateiname):
            with open(dateiname, 'r') as datei:
                kontakte = json.load(datei)
        else:
            kontakte = []  # Noch keine Datei? Dann starten wir mit einer leeren Liste

        # Neuen Kontakt hinten anhängen
        kontakte.append(kontakt)

        # Neue Liste wieder zurückschreiben, schön formatiert
        with open(dateiname, 'w') as datei:
            json.dump(kontakte, datei, indent=4)

        print("✅ Kontakt wurde gespeichert.")

    except (IOError, json.JSONDecodeError):
        print("❌ Fehler beim Speichern des Kontakts.")


# Funktion zum Laden aller gespeicherten Kontakte
def lade_kontakte():
    dateiname = "kontakte.json"

    try:
        with open(dateiname, 'r') as datei:
            kontakte = json.load(datei)
            return kontakte
    except FileNotFoundError:
        print("⚠️ Noch keine Kontakte gespeichert.")
        return []
    except json.JSONDecodeError:
        print("⚠️ Dateiinhalt ist beschädigt oder nicht lesbar.")
        return []


# Kleine Benutzeroberfläche über die Konsole
def main():
    while True:
        print("\n--- Kontaktverwaltung ---")
        print("H. Neuen Kontakt hinzufügen")
        print("A. Kontakte anzeigen")
        print("ENDE. Beenden")

        wahl = input("Was möchtest du tun? ").strip().upper()

        if wahl == 'H':
            name = input("Name: ")
            email = input("E-Mail: ")
            telefon = input("Telefonnummer: ")
            speichere_kontakt(name, email, telefon)

        elif wahl == 'A':
            kontakte = lade_kontakte()
            if kontakte:
                print("\n--- Gespeicherte Kontakte ---")
                for i, k in enumerate(kontakte, 1):
                    print(f"{i}. {k['Name']} | {k['E-Mail']} | {k['Telefon']}")
            else:
                print("Noch keine Kontakte vorhanden.")

        elif wahl == 'ENDE':
            print("Tschüss! Programm wird beendet.")
            break

        else:
            print("❗ Ungültige Eingabe – bitte H, A oder ENDE eingeben.")

# Nur starten, wenn dieses Skript direkt ausgeführt wird
if __name__ == '__main__':
    main()