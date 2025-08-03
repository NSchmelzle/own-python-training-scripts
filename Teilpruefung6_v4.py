#----------------------------------------------------------------
# Dateiname: Schmelzle_Teilpruefung6_v4.py
# Online Bücherladen
# Autor: Nikhil Schmelzle
# Letzte Änderung: 03.08.2025
#--------------------------------------------------------------
# Klasse für einBuch
class Buch:
    def __init__(self, titel, autor, kategorie, preis):
        self.titel = titel
        self.autor = autor
        self.kategorie = kategorie
        self.preis = preis
    def __str__(self):
        return f"{self.titel} von {self.autor} ({self.kategorie}) – {self.preis:.2f} €"
#Klasse für online-Buchladen
class Buchladen:
    def __init__(self):
        self.inventar = []
    def buch_hinzufuegen(self, buch):
        self.inventar.append(buch)
    def zeige_buecher(self):
        for buch in self.inventar:
            print(buch)

#   starten des Buchladens
laden = Buchladen()
# Romane
laden.buch_hinzufuegen(Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", "Roman", 12.99))
laden.buch_hinzufuegen(Buch("Harry Potter und die Kammer des Schreckens", "J.K. Rowling", "Roman", 13.99))
laden.buch_hinzufuegen(Buch("Harry Potter und der Gefangene von Askaban", "J.K. Rowling", "Roman", 14.99))
laden.buch_hinzufuegen(Buch("Harry Potter und der Feuerkelch", "J.K. Rowling", "Roman", 15.99))
laden.buch_hinzufuegen(Buch("Harry Potter und der Orden des Phönix", "J.K. Rowling", "Roman", 16.99))
laden.buch_hinzufuegen(Buch("Harry Potter und der Halbblutprinz", "J.K. Rowling", "Roman", 17.99))
laden.buch_hinzufuegen(Buch("Harry Potter und die Heiligtümer des Todes", "J.K. Rowling", "Roman", 18.99))
# Fantasy
laden.buch_hinzufuegen(Buch("Die unendliche Geschichte", "Michael Ende", "Fantasy", 11.50))
laden.buch_hinzufuegen(Buch("Krabat", "Otfried Preußler", "Fantasy", 10.00))
laden.buch_hinzufuegen(Buch("Der kleine Hobbit", "J.R.R. Tolkien", "Fantasy", 12.00))
#Sachbuch
laden.buch_hinzufuegen(Buch("Der unendliche Augenblick", "Natalie Napp", "Sachbuch", 13.95))
laden.buch_hinzufuegen(Buch("Der Quantensprung des Denkens", "Unbekannt", "Sachbuch", 14.90))
# Ratgeber
laden.buch_hinzufuegen(Buch("Handbuch des Kriegers des Lichts", "Paulo Coelho", "Ratgeber", 10.99))
# Wissenschaft
laden.buch_hinzufuegen(Buch("Das Universum in der Nussschale", "Stephen Hawking", "Wissenschaft", 19.95))

# Alle Bücher anzeigen
laden.zeige_buecher()