# --------------------------------------------------------
# Dateiname: Teilpruefung4_v1.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 17.07.2025
# --------------------------------------------------------
import re
import json

# --------------------------------------------------------
# Funktion: Lies die Datei feedback.txt und gib den Inhalt zurück.
# Wir nutzen die with-Anweisung, damit die Datei nach dem Lesen
# automatisch geschlossen wird. Außerdem fangen wir Fehler ab.
# --------------------------------------------------------
def lese_feedback(dateiname):
    try:
        with open(dateiname, 'r', encoding='utf-8') as file:
            inhalt = file.read()
        print(f"\u2705 Datei '{dateiname}' erfolgreich gelesen!")  # ✅ Emoji für Erfolg
        return inhalt
    except FileNotFoundError:
        print(f"\u274C Fehler: Datei '{dateiname}' wurde nicht gefunden.")  # ❌ Emoji für Fehler
    except Exception as e:
        print(f"\u274C Unerwarteter Fehler beim Lesen: {e}")
    return ""


# --------------------------------------------------------
# Funktion: Extrahiere alle Datumsangaben im Format DD.MM.YYYY
# mittels regulärem Ausdruck (Regex).
# Beispiel: 12.05.2023 -> Treffer
# --------------------------------------------------------
def extrahiere_datumsangaben(text):
    # Regex-Muster: zwei Ziffern, Punkt, zwei Ziffern, Punkt, vier Ziffern
    muster = r'\b\d{2}\.\d{2}\.\d{4}\b'
    return re.findall(muster, text)


# --------------------------------------------------------
# Funktion: Zähle, wie oft jedes Datum vorkommt.
# Wir nutzen ein Dictionary, wobei das Datum der Schlüssel ist
# und die Anzahl der Vorkommen der Wert.
# --------------------------------------------------------
def zaehle_datumsvorkommen(datums_liste):
    vorkommen = {}
    for datum in datums_liste:
        vorkommen[datum] = vorkommen.get(datum, 0) + 1
    return vorkommen


# --------------------------------------------------------
# Funktion: Finde alle Kommentare, die das Wort "exzellent"
# (unabhängig von Groß-/Kleinschreibung) enthalten.
# Wir gehen davon aus, dass jeder Kommentar in einer eigenen Zeile steht.
# --------------------------------------------------------
def finde_exzellente_feedbacks(text):
    zeilen = text.splitlines()
    exzellente = [zeile for zeile in zeilen if re.search(r'\bexzellent\b', zeile, re.IGNORECASE)]
    return exzellente


# --------------------------------------------------------
# Funktion: Speichere Daten als JSON-Datei.
# Wir nutzen ensure_ascii=False, damit Umlaute und Sonderzeichen lesbar bleiben.
# --------------------------------------------------------
def speichere_json(dateiname, daten):
    try:
        with open(dateiname, 'w', encoding='utf-8') as file:
            json.dump(daten, file, ensure_ascii=False, indent=4)
        print(f"\u2705 Datei '{dateiname}' wurde erfolgreich gespeichert!")  # ✅ Emoji
    except Exception as e:
        print(f"\u274C Fehler beim Speichern in '{dateiname}': {e}")


# --------------------------------------------------------
# Hauptlogik: Alle Schritte zusammen
# --------------------------------------------------------
def main():
    quell_datei = 'feedback.txt'

    # 1. Datei lesen
    text = lese_feedback(quell_datei)
    if not text:
        return  # Falls Lesen fehlschlägt, Programm beenden

    # 2. Alle Datumsangaben extrahieren
    datumsangaben = extrahiere_datumsangaben(text)
    print(f"Gefundene Datumsangaben: {datumsangaben}")

    # 3. Vorkommen zählen
    datumsvorkommen = zaehle_datumsvorkommen(datumsangaben)
    print(f"Zählung der Datumsvorkommen: {datumsvorkommen}")

    # 4. Alle Kommentare mit "exzellent" finden
    exzellente_feedbacks = finde_exzellente_feedbacks(text)
    print(f"Gefundene 'exzellente' Kommentare: {exzellente_feedbacks}")

    # 5. Ergebnisse in JSON-Dateien speichern
    speichere_json('datums_vorkommen.json', datumsvorkommen)
    speichere_json('exzellente_feedbacks.json', exzellente_feedbacks)

    print("\n\u2728 Analyse abgeschlossen! Ergebnisse wurden gespeichert. \u2728")  # ✨ Erfolgsnachricht


# --------------------------------------------------------
# Testdatei erstellen (für Aufgabe h)
# Diese Funktion erzeugt eine Beispiel-Textdatei mit Feedback.
# --------------------------------------------------------
def erzeuge_testdatei():
    inhalt = """12.05.2023 Exzellenter Service! Sehr freundlich.
15.05.2023 Der Service war okay.
12.05.2023 Wirklich exzellent, ich bin sehr zufrieden.
20.06.2023 Leider nicht gut.
15.05.2023 Exzellent! Besser geht's nicht.
"""
    with open('feedback.txt', 'w', encoding='utf-8') as file:
        file.write(inhalt)
    print("\u2705 Testdatei 'feedback.txt' wurde erstellt.")


# --------------------------------------------------------
# Ausführung
# --------------------------------------------------------
if __name__ == "__main__":
    erzeuge_testdatei()  # Zum Testen: Datei anlegen
    main()
