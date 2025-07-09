#----------------------------------------------------------------
# Dateiname: student_data.py
# 
# Autor: Nikhil Schmelzle
# Letzte Änderung: 08.07.2025
#----------------------------------------------------------------

# Funktion zum Speichern einer Liste von Studierenden-Datensätzen
# Jeder Datensatz ist ein Tupel: (Name, Matrikelnummer, Studiengang)
def speichere_daten(studenten):
    try:
        # Datei im Schreibmodus öffnen (überschreibt vorhandene Datei)
        with open('studentendaten.txt', 'w') as datei:
            for student in studenten:
                # Formatieren wir schön lesbar, alles in eine Zeile
                zeile = f"Name: {student[0]}, Matrikelnummer: {student[1]}, Studiengang: {student[2]}\n"
                datei.write(zeile)
        print("Daten wurden erfolgreich gespeichert.")
    except IOError:
        # Falls beim Schreiben was schiefgeht (z. B. kein Schreibrecht)
        print("Fehler beim Speichern der Datei.")

# Funktion zum Laden und Umwandeln der gespeicherten Daten
# Gibt eine Liste von Dictionaries zurück (ein Dictionary pro Student)
def lade_daten():
    daten = []
    try:
        # Datei im Lesemodus öffnen
        with open('studentendaten.txt', 'r') as datei:
            for zeile in datei:
                # Erstmal Zeilenumbruch loswerden und dann bei Komma trennen
                teile = zeile.strip().split(', ')
                student_dict = {}
                # Jetzt jeden Teil weiter zerlegen: "Schlüssel: Wert"
                for teil in teile:
                    key_value = teil.split(': ', 1)
                    if len(key_value) == 2:
                        key, value = key_value
                        student_dict[key] = value
                # Das Dictionary kommt in unsere Ergebnisliste
                daten.append(student_dict)
    except FileNotFoundError:
        # Falls die Datei noch gar nicht existiert
        print("Datei nicht gefunden.")
    except IOError:
        # Falls beim Lesen was schiefgeht (z. B. Datei beschädigt)
        print("Fehler beim Lesen der Datei.")
    return daten

# Kleines Beispiel zum Testen – nur ausführen, wenn Datei direkt gestartet wird
if __name__ == '__main__':
    # Testdaten – eine kleine Liste mit Studierenden-Tupeln
    beispiel_daten = [
        ("Max Mustermann", "123456", "Chemie"),
        ("Lisa Müller", "234567", "Physik"),
        ("Ali Kaya", "345678", "Informatik")
    ]
    # Daten speichern
    speichere_daten(beispiel_daten)
    # Daten wieder laden
    geladene_daten = lade_daten()
    # Mal ausgeben, ob alles korrekt geladen wurde
    print("\nGeladene Daten:")
    for eintrag in geladene_daten:
        print(eintrag)