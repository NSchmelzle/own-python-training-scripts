#--------------------------------------------
# Dateiname: Namensliste_Umwandlung.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 09.07.2025
#--------------------------------------------
import json  # Zum Arbeiten mit JSON-Dateien

#Namen aus Textdatei lesen
def lese_namen():
    try:
        with open("namensliste.txt","r") as datei:  # "r" für Lesen
            for zeile in datei:
                print(zeile.strip())  #.strip entfernt Zeilenumbruch etc.
    except Exception as Fehler:
        print("Fehler beim Lesen der Datei:",Fehler)

# Namen in JSON-Datei schreiben
def schreibe_json_liste():
    try:
        with open("namensliste.txt","r") as text_liste:  # Lesen der ursprünglichen Datei
            namen_liste = [zeile.strip() for zeile in text_liste]  # alle Namen in eine Liste (Übernommen aus Ü8.5)

        with open("namensliste.json","w") as json_liste:  #Schreiben als JSON-Datei
            json.dump(namen_liste, json_liste, indent=2, ensure_ascii=False)  # schön formatiert (Übernommen aus Ü8.7 1&2)

        print("Die Namensliste wurde erfolgreich als JSON-Datei gespeichert.")
    except Exception as e:
        print("Fehler beim Schreiben der JSON-Datei:", e)

# Einfache Konsolen-Benutzeroberfläche
while True:
    print("\nHallo, wähle eine Option:") #Zeilenumbruch für bessere Lesbarkeit
    print("(L)esen der Namensliste")
    print("(S)peichern der Namensliste als JSON")
    print("ENDE")
    
    menu = input("Bitte wähle L, S oder ENDE: ").strip().upper() #Nur Großbuchstaben, entfernt Leerzeichen etc., um Eingabefehler zu vermeiden

    if menu == "L":
        lese_namen()
    elif menu == "S":
        schreibe_json_liste()
    elif menu == "ENDE":
        print("beende Programm.")
        break # Abbruch bei beenden des Programms
    else:
        print("Ungültige Eingabe! Bitte wähle L, S, ENDE.")