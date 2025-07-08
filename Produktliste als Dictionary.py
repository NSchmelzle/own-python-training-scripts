# Produktliste als Dictionary
produktliste = {
    "Laptop": 999.00,
    "Smartphone": 599.00,
    "Kopfhörer": 149.00,
    "Smartwatch": 249.00,
    "Tablet": 399.00,
    "E-Book-Reader": 129.00,
    "Fitness-Tracker": 79.00,
    "Bluetoothlautsprecher": 89.00,
    "Powerbank": 39.00,
    "Webcam": 59.00
}

# a) Durchschnittspreis berechnen
def durchschnittspreis(preise):
    if not preise:
        return None
    return round(sum(preise) / len(preise), 2)

# b) Produkt-Filter mit filter() und startswith()
def produkt_filter(produktliste, buchstabe):
    gefilterte_produkte = list(filter(
        lambda produkt: produkt.lower().startswith(buchstabe.lower()),
        produktliste.keys()
    ))
    return gefilterte_produkte

# c) Rekursive Maximalpreis-Funktion
def max_preis(preise):
    if not preise:
        return None
    if len(preise) == 1:
        return preise[0]
    else:
        max_rest = max_preis(preise[1:])
        return preise[0] if preise[0] > max_rest else max_rest

# d) Preis mit Steuer berechnen (Default: 19%)
def preis_mit_steuer(preis, steuersatz=19):
    return round(preis * (1 + steuersatz / 100), 2)

# e) Lambda + map(), um Preise um Prozentsatz zu erhöhen
def preise_erhoehen(preise, prozentsatz):
    return list(map(lambda p: round(p * (1 + prozentsatz / 100), 2), preise))

# f) Produkte schön formatiert ausgeben
def drucke_produktliste(produkte):
    print("Produktliste:")
    for produkt in produkte:
        print(f"- {produkt}")

# ------------------------------------------------------
# Test / Beispielaufrufe

# Liste der Preise aus dem Dictionary holen
preise = list(produktliste.values())

# a) Durchschnittspreis
print("Durchschnittspreis:", durchschnittspreis(preise), "€")

# b) Produkte mit Buchstabe 'S'
print("Produkte mit 'S':", produkt_filter(produktliste, "S"))

# c) Höchster Preis
print("Höchster Preis:", max_preis(preise), "€")

# d) Preis mit Steuer für ein Produkt
print("Laptop-Preis mit Steuer:", preis_mit_steuer(produktliste["Laptop"]), "€")

# e) Preise um 10 % erhöhen
neue_preise = preise_erhoehen(preise, 10)
print("Preise nach 10 % Erhöhung:", neue_preise)

# f) Produktliste ausgeben
drucke_produktliste(produktliste.keys())