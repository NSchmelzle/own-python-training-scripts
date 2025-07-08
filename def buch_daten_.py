def buch_daten_speichern(titel, autor, jahr, seiten=0):
    buch_dict = {"titel": titel, "autor": autor, "jahr": jahr, "seiten": seiten}
    return buch_dict

def buecher_sammlung(buecher_liste):
    gesamt_seiten = sum(buch["seiten"] for buch in buecher_liste)
    return gesamt_seiten

buecher_liste = []
for _ in range(3):
    titel = input("Gib den Titel des Buches ein: ")
    autor = input("Gib den Autor des Buches ein: ")
    jahr = int(input("Gib das Veröffentlichungsjahr des Buches ein: "))
    seiten = input("Gib die Anzahl der Seiten des Buches ein (optional): ")
    try:
        seiten = int(seiten)
    except ValueError:
        seiten = 0
    buch_dict = buch_daten_speichern(titel, autor, jahr, seiten)
    buecher_liste.append(buch_dict)

gesamt_seiten = buecher_sammlung(buecher_liste)
print(f"Die Gesamtanzahl der Seiten aller Bücher beträgt: {gesamt_seiten}")