# --------------------------------------------------------
# Dateiname: Teilpruefung4_v2.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 17.07.2025
# ------------------------------------------------------
import re
import json
# Import der verwendeten Module
# -----------------------------------------------------
#Lese den Inhalt der Kundenfeedback-Datei.
# Nutzt die with-Anweisung, um Datei nach dem lesen automatisch zu schließen
# mit Fehlerbehandlung
# --------------------------------------------------------
def lese_feedback(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as file:
            inhalt = file.read()
        print(f"Datei '{dateiname}' wurde erfolgreich gelesen.")
        return inhalt
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' wurde nicht gefunden.")
    except Exception as e:
        print(f"Unerwarteter Fehler beim Lesen: {e}")
    return ""
# --------------------------------------------------------
# Extrahiert alle Datumsangaben ( DD.MM.YYYY )
# durch Hilfe des regulären Ausdrucks (engl:regex)
#Beispiel: 12.05.2025 -> ergibt 1 Treffer
# ----------------------------------------------------
def extrahiere_datumsangaben(text):
    #Regex sucht zwei Buchstaben, Punkt, zwei BS, Punkt, vier BS ( spiegelt DD.MM.YYYY wieder )
    regex_ddmmyyyyy = r'\b\d{2}\.\d{2}\.\d{4}\b'
    return re.findall(regex_ddmmyyyyy, text)
# ------------------------------------------------------
# Zählt, wie oft jedes Datum vorkommt.
#Nutzt ein Dictionary, mit Datum als Schlüssel
# und Anzahl der Vorkommen (der Daten)
# -----------------------------------------------------------
def datumsvorkommen(datums_liste):
    vorkommen = {}
    for datum in datums_liste:
        vorkommen[datum] = vorkommen.get(datum, 0) + 1
    return vorkommen
# -----------------------------------------------------------
# Funktion: Sucht alle Kommentare, die das Wort "exzellent"
#oder seine Übersetzungen enthalten (excellent, excelente, excellent ).
# Es wird nicht zwischen Groß- und Kleinschreibung unterschieden.
# (mit type hint, Idee aus Volumen.py übernommen)
# ------------------------------------------------------
def finde_exzellente_feedbacks(text: str):
    zeilen = text.splitlines()
    # Regex deckt Deutsch, Englisch, Spanisch, Französisch ab für das wort Exzellent, aber nciht Chinesisch (zu kompliziert)
    regex_excell_xyz = r'\b(exzellent|excellent|excelente)\b'
    return [zeile for zeile in zeilen if re.search(regex_excell_xyz, zeile, re.IGNORECASE)]
# --------------------------------------------------------
# Speichert Daten als JSON-Datei.
#ensure_ascii=False -> Umlaute sollten lesbar sein (Übernommen aus Ü9.3.01)
# indent=4 -> Bessere Lesbarkeit durch einrückung ( Übernommen aus Ü9.3.02 )
# try except Schleife zur Fehlerbehandlung (Übernommen aus Übungen wie 9.3.01)
# -------------------------------------------------------
def speichere_json(dateiname, daten):
    try:
        with open(dateiname, 'w', encoding='utf-8') as file:
            json.dump(daten, file, ensure_ascii=False, indent=4)
        print(f"Datei '{dateiname}' wurde erfolgreich gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern in '{dateiname}': {e}")
#--------------------------------------------------------
# Hauptfunktion: hier werden alle Schritte ausgeführt
# -------------------------------------------------------------
def main():
    quell_datei = 'Kundenfeedback.txt'

    #Datei lesen
    text = lese_feedback(quell_datei)
    if not text:
        return  # Falls Lesen misslingt, wird abgebrochen

    #Alle Datumsangaben extrahieren
    datumsangaben = extrahiere_datumsangaben(text)
    print(f"Gefundene Datumsangaben: { datumsangaben}")

    # Zählen, wie oft jedes Datum vorkommt
    vorkommen = datumsvorkommen( datumsangaben)
    print( f"Häufigkeit der Datumsangaben: {vorkommen}")

    # Alle Kommentare mit "exzellent" (oder excellent aus Übersetzungen) finden
    exzellente_kunden_feedbacks = finde_exzellente_feedbacks(text)
    print(f"Gefundene Kommentare mit 'exzellent/excellent': {exzellente_kunden_feedbacks}")

    #Ergebnisse in JSON-Dateien (als Listen) speichern
    speichere_json( 'datums_vorkommen.json', vorkommen)
    speichere_json('exzellente_Kunden-feedbacks.json', exzellente_kunden_feedbacks)

    print("\nAnalyse abgeschlossen. Ergebnisse wurden gespeichert.")
#--------------------------------------------------------
#Erzeugt eine Testdatei mit mehrsprachigen Kundenbewertungen.
# - Verschiedene Sprachen/ Datumsangaben in DD.MM.YYYY
# Exzellent auf D/En/Esp (von google translate)
# -----------------------------------------------------
def erzeuge_testdatei():
    inhalt = """08.01.2025 Exzellenter Service! Sehr freundlich.
02.03.2025 Der Service war gut, aber leider nicht perfekt.
18.04.2025 Excellent service! Very fast delivery.
12.05.2025 ¡Servicio excelente! Estoy muy satisfecho.
06.06.2025 Service excellent et très rapide, merci beaucoup!
06.06.2025 客户服务很好 我很满意
06.06.2025 Alles perfekt.
17.07.2025 Good job, well done.
"""
    with open('Kundenfeedback.txt', 'w', encoding='utf-8') as file:
        file.write(inhalt)
    print("Testdatei 'Kundenfeedback.txt' wurde erstellt.")

# ----------------------------------------------------
# Ausführung (Übernommen aus Ü 7.3)
#--------------------------------------------------------
if __name__ == "__main__":
    erzeuge_testdatei()  # Erstellt Testdatei mit Kommentaren aus verschiedenen Sprachen.
    main()