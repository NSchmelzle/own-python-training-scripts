def berechne_durchschnitt(zahlen_liste):
    if not zahlen_liste:  # Prüft, ob die Liste leer ist
        return None
    summe = 0
    for zahl in zahlen_liste:
        summe += zahl
    durchschnitt = summe / len(zahlen_liste)
    return durchschnitt
# Liste von Zahlen definieren
zahlen = [10, 20, 30, 40, 50]
# Funktion aufrufen und Ergebnis ausgeben
durchschnitt = berechne_durchschnitt(zahlen)
if durchschnitt is not None:
    print(f"Der Durchschnitt der Zahlenliste ist: {durchschnitt}")
else:
    print("Die Liste ist leer.")
# Beispiel mit einer leeren Liste
leere_liste = []
durchschnitt_leer = berechne_durchschnitt(leere_liste)
if durchschnitt_leer is not None:
    print(f"Der Durchschnitt der leeren Liste ist: {durchschnitt_leer}")
else:
    print("Die Liste ist leer.")