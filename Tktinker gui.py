import tkinter as tk
from tkinter import font

# -----------------------------
# Hauptanwendung (Tkinter-Root)
# -----------------------------
root = tk.Tk()
root.title("Hallo Welt GUI")  # Titel des Fensters setzen
root.geometry("300x200")      # Fenstergröße festlegen

# -----------------------------
# Label hinzufügen (Aufgabe a)
# -----------------------------
# Wir erstellen eine Schriftart für das Label: Arial, 14pt
label_font = font.Font(family="Arial", size=14)

# Label mit Text "Hallo Welt!"
label = tk.Label(root, text="Hallo Welt!", font=label_font)
label.pack(pady=10)  # pack() positioniert das Label oben, pady = Abstand oben/unten

# -----------------------------
# Entry-Widget (Aufgabe b)
# -----------------------------
# Das Entry-Widget erlaubt die Eingabe von Text
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# -----------------------------
# Funktionen für Buttons (Aufgabe c)
# -----------------------------
def clear_entry():
    """Löscht den Text im Entry-Widget."""
    entry.delete(0, tk.END)

def close_window():
    """Schließt das Anwendungsfenster."""
    root.destroy()

# -----------------------------
# Button-Liste mit Funktionen (Aufgabe d)
# -----------------------------
# Wir nutzen eine Liste von Tupeln: (Button-Text, zugehörige Funktion)
buttons_data = [
    ("Text löschen", clear_entry),
    ("Fenster schließen", close_window)
]

# Schleife zum Erstellen und Platzieren der Buttons
for text, command in buttons_data:
    button = tk.Button(root, text=text, command=command)
    button.pack(side=tk.BOTTOM, pady=5)  # Buttons am unteren Rand

# -----------------------------
# Hauptschleife starten (Aufgabe h)
# -----------------------------
root.mainloop()
