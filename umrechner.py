def umrechner(betrag, waehrung="USD"):
    if waehrung == "USD":
        return betrag * 1.1
    elif waehrung == "GBP":
        return betrag * 0.9
    else:
        return None
while True:
    print("Währungsumrechner: EUR zu USD oder GBP")
    betrag = float(input("Bitte geben Sie den Betrag in EUR ein, den Sie umrechnen möchten: "))
    waehrung = input("Bitte geben Sie die Währung ein, in die Sie umrechnen möchten (USD/GBP). Drücken Sie Enter für USD: ").upper()
    
    if waehrung not in ["USD", "GBP", ""]:
        print("Die angegebene Währung wird nicht unterstützt.")
    else:
        ergebnis = umrechner(betrag, waehrung)
        if ergebnis is not None:
            print(f"Umrechnungsergebnis: {ergebnis:.2f} {waehrung}")
        else:
            print("Es gab ein Problem mit der Währungsumrechnung.")
    
    weiter = input("Möchten Sie eine weitere Umrechnung durchführen? (ja/nein): ").lower()
    if weiter != "ja":
        print("Programm beendet.")
        break