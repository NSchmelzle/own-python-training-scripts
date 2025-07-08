#----------------------------------------------------------------
# Dateiname: Buecherdatenbank_Schmelzle_teilpruefung2.py
# Buecherdatenbank
# Autor: Nikhil Schmelzle
# Letzte Änderung: 04.07.2025
# Feedback: Diese Prüfung ist sehr viel, für die 90min, die im Stundenplan dafür angesetzt sind in Woche 2.
# Ich habe bestimmt 6 Stunden dafür gebraucht, die ganze Woche über.
#----------------------------------------------------------------

#Erstellung der Datenbank, Lieblings-Kinderbuecher als Beispiel:
buecherei_datenbank = [
    {"Titel": "Harry Potter und der Stein der Weisen", "Autor": "J.K. Rowling", "Jahr": 1997},
    {"Titel": "Harry Potter und die Kammer des Schreckens", "Autor": "J.K. Rowling", "Jahr": 1998},
    {"Titel": "Harry Potter und der Gefangene von Askaban", "Autor": "J.K. Rowling", "Jahr": 1999},
    {"Titel": "Harry Potter und der Feuerkelch", "Autor": "J.K. Rowling", "Jahr": 2000},
    {"Titel": "Harry Potter und der Orden des Phönix", "Autor": "J.K. Rowling", "Jahr": 2003},
    {"Titel": "Harry Potter und der Halbblutprinz", "Autor": "J.K. Rowling", "Jahr": 2005},
    {"Titel": "Harry Potter und die Heiligtümer des Todes", "Autor": "J.K. Rowling", "Jahr": 2007},
    {"Titel": "Die unendliche Geschichte", "Autor": "Michael Ende", "Jahr": 1979},
    {"Titel": "Krabat", "Autor": "Otfried Preußler", "Jahr": 1971},
    {"Titel": "Der kleine Hobbit", "Autor": "J.R.R. Tolkien", "Jahr": 1937}
]

# Erstellung einer eigenen Funktion mit Filter zur Buchsuche, Standard-Argument fuer Autor = None
def suche_buch(titel, autor=None):
    # Filtert alle Bücher, deren Titel (und ggf. Autor) mit den Suchkriterien übereinstimmen
    if autor:  # fuer Autor und Titel
        ergebnis_buchsuche = filter(lambda buch: buch["Titel"] == titel and buch["Autor"] == autor, buecherei_datenbank)
    else:  # fuer Titel
        ergebnis_buchsuche = filter(lambda buch: buch["Titel"] == titel, buecherei_datenbank)
    return list(ergebnis_buchsuche)  # gibt das Ergebnis aus der inneren funktion zurueck

# Erstellt ein neues Buch-dictionary und fügt es der obrigen bestehenden Datenbank hinzu
# Erstellung einer eigenen Funktion, um Buecher hinzuzufuegen (mit type hint, Idee aus Volumen.py uebernommen)
def fuege_buch_hinzu(titel: str, autor: str, jahr: int):
    neues_buch = {"Titel": titel, "Autor": autor, "Jahr": jahr}
    buecherei_datenbank.append(neues_buch)  # Liste neues_buch innerhalb der Funktion wird der Datenbank außerhalb der Funktion hinzugefuegt.

# Erstellung einer eigenen Funktion zur Filterung nach Jahr (wieder mit type hint)
def buecher_gefiltert_nach_jahr(jahr: int):
    ergebnis_gefiltert_nach_jahr = filter(lambda buch: buch["Jahr"] == jahr, buecherei_datenbank)
    return list(ergebnis_gefiltert_nach_jahr)

# Erstellen einer eigenen Funktion zur Anzeige der (neuen) Datenbank
def zeige_datenbank():
    for buch in buecherei_datenbank:
        print(f"{buch['Titel']} von {buch['Autor']} ({buch['Jahr']})")
# Formatiert und gibt die Buchdaten ilesbar in einer Zeile aus (F-String)
# Keine Funktion fuer leere Liste, da nicht gefordert

# Endlosschleife für das Hauptmenü — diese läuft so lange, bis "ENDE" eingegeben wird
# While schleife, die Funktionen anhand von Kürzeln abfragt
while True:
    print("\n=== Bücherei-Menü ===")
    print("S: Buch suchen")
    print("H: Buch hinzufügen")
    print("F: Bücher nach Jahr filtern")
    print("A: Datenbank anzeigen")
    print("ENDE: Beenden")

    # .upper um Fehler in der Eingabeverarbeitung zu Vermeiden
    menu_auswahl = input("Bitte eine Option wählen: ").upper()

    if menu_auswahl == "S":
        print("Buchsuche wurde gewählt.")
        titel = input("Titel des Buches: ")
        autor = input("Autor (optional, Enter für alle): ")
        if autor == "":
            ergebnis = suche_buch(titel)
        else:
            ergebnis = suche_buch(titel, autor)
        if ergebnis:
            for buch in ergebnis:
                print(f"{buch['Titel']} von {buch['Autor']} ({buch['Jahr']})")
        else:
            print("Kein Buch gvorhanden.")

    elif menu_auswahl == "H":
        print("Buch hinzufügen wurde gewählt.")
        titel = input("Titel des neuen Buches: ")
        autor = input("Autor des neuen Buches: ")
        jahr = int(input("Erscheinungsjahr des neuen Buches: "))
        fuege_buch_hinzu(titel, autor, jahr)
        print("Buch wurde hinzugefügt.")

    elif menu_auswahl == "F":
        print("Bücher nach Jahr filtern wurde gewählt.")
        jahr = int(input("Bitte Erscheinungsjahr eingeben: "))
        ergebnis = buecher_gefiltert_nach_jahr(jahr)
        if ergebnis:
            for buch in ergebnis:
                print(f"{buch['Titel']} von {buch['Autor']} ({buch['Jahr']})")
        else:
            print("Keine Bücher aus dem Jahr gefunden.")

    elif menu_auswahl == "A":
        print("Datenbank-Anzeige wurde gewählt.")
        zeige_datenbank()

    elif menu_auswahl == "ENDE":
        print("Programm wird beendet.")
        break
    # else Schleife fuer ungueltige Eingaben (aus anderen Uebungsskripten adaptiert)
    else:
        print("Ungültige Eingabe. Bitte einen Buchstaben aus dem Menü wählen.")
# while-Schleife sorgt fuer laufende menu abfragen, die Funktionen anhand von Kuerzeln abfragt
# Endlosschleife für das Hauptmenü — diese läuft so lange, bis "ENDE" eingegeben wird
while True:
    print("--- Bücherei Menü ---")
    print("S: Buch suchen")
    print("H: Buch hinzufügen")
    print("F: Bücher nach Jahr filtern")
    print("A: Datenbank anzeigen")
    print("ENDE: Beenden")

    # .upper um Fehler in der Verarbeitung der Eingabe zu vermeiden
    menu_auswahl = input("Bitte wähle eine Option: ").upper()
    #Das komplette Menü ist eingerückt, da eine große if schleife und die Menü Funktionen sind natürlich eins weiter eingerückt, da eigene if schleifen (innerhalb des Blocks)
    if menu_auswahl == "S":
        print("Du hast die Buchsuche gewählt.")
        # Abfrage Titel und optional Autor
        titel = input("Titel des Buches: ")
        autor = input("Autor (optional, Enter für alle): ")
        # Aufruf der Suchfunktion mit oder ohne Autor
        if autor == "":
            ergebnis = suche_buch(titel)
        else:
            ergebnis = suche_buch(titel, autor)
        # Ausgabe der Suchergebnisse, falls vorhanden
        if ergebnis:
            for buch in ergebnis:
                print(f"{buch['Titel']} von {buch['Autor']} ({buch['Jahr']})")
        else:
            print("Kein Buch gefunden.")

    elif menu_auswahl == "H":
        print("Du hast Buch hinzufügen gewählt.")
        # Abfrage der neuen Buchdaten
        titel = input("Titel des neuen Buches: ")
        autor = input("Autor des neuen Buches: ")
        jahr = int(input("Erscheinungsjahr des neuen Buches: "))
        # Aufruf zum Hinzufügen (eines neuen Buches)
        fuege_buch_hinzu(titel, autor, jahr)
        print("Buch wurde der Datenbank hinzugefügt.")

    elif menu_auswahl == "F":
        print("Du hast Bücher nach Jahr filtern gewählt.")
        # Abfrage des gewählten Jahres
        jahr = int(input("Bitte Erscheinungsjahr eingeben: "))
        # Aufruf fuer die Filterung nach Jahr
        ergebnis = buecher_gefiltert_nach_jahr(jahr)
        # Ausgabe der gefilterten Bücher
        if ergebnis:
            for buch in ergebnis:
                print(f"{buch['Titel']} von {buch['Autor']} ({buch['Jahr']})")
        else:
            print("Keine Bücher aus diesem Jahr gefunden.")

    elif menu_auswahl == "A":
        print("Du hast die Datenbank-Anzeige gewählt.")
        # Aufruf zur Anzeige der (neuen) Datenbank
        zeige_datenbank()

    elif menu_auswahl == "ENDE":
        print("Programm wird beendet.")
        break

    # else Schleife für ungültige Eingaben (aus anderen Uebungsskripten adaptiert)
    else:
        print("Ungültige Eingabe. Bitte einen Buchstaben aus dem Menü wählen.")
# while-Schleife sorgt für laufende menu abfragen