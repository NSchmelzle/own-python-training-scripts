#----------------------------------------------------------------
# Dateiname: Buecherdatenbank_Schmelzle_pruefung2.py
# Buecherdatenbank
# Autor: Nikhil Schmelzle
# Letzte Änderung: 01.07.2025
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
# While schleife, die Funktionen anhand von Kuerzeln abfragt
while True:
    print("\n=== Bücherei-Menü ===")
    print("S: Buch suchen")
    print("H: Buch hinzufügen")
    print("F: Bücher nach Jahr filtern")
    print("A: Datenbank anzeigen")
    print("ENDE: Beenden")

    # .upper um Fehler in der Eingabeverarbeitung zu Vermeiden
    menu_auswahl = input("Bitte wähle eine Option: ").upper()

    if menu_auswahl == "S":
        print("Du hast die Buchsuche gewählt.")
    elif menu_auswahl == "H":
        print("Du hast Buch hinzufügen gewählt.")
    elif menu_auswahl == "F":
        print("Du hast Bücher nach Jahr filtern gewählt.")
    elif menu_auswahl == "A":
        print("Du hast die Datenbank-Anzeige gewählt.")
    elif menu_auswahl == "ENDE":
        print("Programm wird beendet.")
        break
    # else Schleife fuer ungueltige Eingaben (aus anderen Uebungsskripten adaptiert)
    else:
        print("Ungültige Eingabe. Bitte einen Buchstaben aus dem Menü wählen.")
# while-Schleife sorgt fuer laufende menu abfragen