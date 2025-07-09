#----------------------------------------------------------------
# Dateiname: save_data_test.py
# writing data on file
# Autor: Nikhil Schmelzle
# Letzte Änderung: 08.07.2025
#----------------------------------------------------------------

# Eigene funktion zum speichern von Daten
def save_data(list):
    try:
        with open("person.txt", "w") as file:
            for name, age in list:
                file.write(f"{name}: {age}\n")  # age statt alter, da Variable so heißt
    except Exception as e:
        print("Fehler beim Speichern der Datei:", e)  # bessere Fehlerausgabe

# Funktion zum Laden der Daten
def load_data():
    try:
        personen = []
        with open("person.txt", "r") as file:
            for row in file:
                name, age = row.strip().split(": ")  # ": " statt '": "' → richtige Trennung
                personen.append({"Name": name, "age": int(age)})
        return personen  # return gehört außerhalb der Schleife, aber innerhalb try-Blocks
    except Exception as e:
        print("Fehler beim Laden der Datei:", e)
        return []

def main():
    personen = [("Nikhil", 38), ("Anne", 35)]
    save_data(personen)

    loaded_data = load_data()
    if loaded_data:
        for person in loaded_data:  # loaded_data statt falschem Ausdruck
            print(f"name: {person['Name']}, age: {person['age']}")  # richtige Anführungszeichen
    else:
        print("no data")

if __name__ == "__main__":
    main()
