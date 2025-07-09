#--------------------------------------------
# Dateiname: Einkaufsliste.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 09.07.2025
#--------------------------------------------
# Anfangsliste
einkaufsliste = ["Eier", "Milch", "Käse", "Brot", "Kirschen", "Gurke"]

# Funktion zum Hinzufügen
def einkauf_hinzufuegen(neues_lebensmittel):
    if neues_lebensmittel not in einkaufsliste:
        einkaufsliste.append(neues_lebensmittel)
        print(f"{neues_lebensmittel} wurde zur Einkaufsliste hinzugefügt.")
    else:
        print("❗ Lebensmittel bereits in der Liste!")

# Benutzer kann beliebig viele Dinge hinzufügen, bis er "fertig" schreibt
def eingabe_schleife():
    print("\nGib neue Lebensmittel ein. Tippe 'fertig', um zu beenden.")
    while True:
        neues_lebensmittel = input("Lebensmittel: ")
        if neues_lebensmittel.lower() == "fertig":
            break
        einkauf_hinzufuegen(neues_lebensmittel)

# Einkaufsliste speichern (mit Fehlerbehandlung)
def speichere_liste():
    try:
        with open("einkaufsliste.txt", "w") as datei:
            for item in einkaufsliste:
                datei.write(item + "\n")
        print("✅ Einkaufsliste wurde gespeichert.")
    except IOError:
        print("❌ Fehler beim Schreiben der Datei.")

# Einkaufsliste aus Datei lesen und Zeile für Zeile anzeigen
def zeige_liste():
    try:
        with open("einkaufsliste.txt", "r") as datei:
            print("\n📄 Inhalt der gespeicherten Einkaufsliste:")
            for zeile in datei:
                print(zeile.strip())
    except FileNotFoundError:
        print("❌ Die Datei wurde nicht gefunden.")
    except IOError:
        print("❌ Fehler beim Lesen der Datei.")

# Hauptablauf
if __name__ == "__main__":
    eingabe_schleife()
    speichere_liste()
    zeige_liste()
