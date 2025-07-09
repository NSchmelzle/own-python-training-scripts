#--------------------------------------------
# Dateiname: personendaten.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 09.07.2025
#--------------------------------------------
import json  # Modul zum Arbeiten mit JSON-Dateien

# Alter als Ganzzahl
alter = 38

# Liste mit Hobbies
hobbies = ["Gärtnern", "Handwerkern", "Vater sein", "Programmierung", "Zocken"]

# Tupel mit Lieblingsfarben
lieblingsfarben = ("rot", "orange", "grün")

# Ausgabe jedes Hobbys in einer Schleife
for hobby in hobbies:
    print("Eines meiner Hobbies ist:", hobby)

# Funktion, um die Jahre bis zur Rente (mit 65) zu berechnen
def jahre_bis_rente(alter, rentenalter=85):
    return rentenalter - alter

# Test der Funktion (optional)
print(f"Du hast noch {jahre_bis_rente(alter)} Jahre bis zur Rente (bei 85).")

# Dictionary mit persönlichen Daten
personendaten = {
    "Hobbies": hobbies,
    "Lieblingsfarben": lieblingsfarben
}

# Versuch, die Daten als JSON-Datei zu speichern
try:
    # Die Datei wird im Schreibmodus geöffnet und automatisch korrekt geschlossen
    with open("persoenliche_daten.json", "w", encoding="utf-8") as datei:
        json.dump(personendaten, datei, indent=4, ensure_ascii=False)
    print("✅ Daten wurden erfolgreich gespeichert.")
except IOError:
    # Falls beim Schreiben ein Fehler passiert (z. B. kein Schreibrecht)
    print("❌ Fehler beim Speichern der Daten.")
