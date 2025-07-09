#--------------------------------------------
# filename: mini_snipit.py
# autor: Nikhil Schmelzle
# last edit: 09.07.2025 (DDMMYYYY)
#--------------------------------------------

# JSON speichern
import json
with open("data.json", "w") as f:
    json.dump(daten, f)

# Fehlerbehandlung allgemein
try:
    ...
except Exception as e:
    print(e)

# Mit Schleife durch Liste
for item in my_list:
    print(item)
