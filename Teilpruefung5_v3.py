# --------------------------------------------------------
# Dateiname: Teilpruefung5_v3.py
# Autor: Nikhil Schmelzle
# Letzte Änderung: 25.07.2025
# ---------------------------------------------------
import tkinter as tk
from tkinter import filedialog, messagebox
import threading   # Threads für parallele Aufgaben (z. B. Timer) – GUI bleibt reaktionsfähig
import time
import pickle    # Für Speichern und Laden von Daten (Ergebnisse)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Einfaches Quiz")
        # Fragen und Antworten (eigene Beispiele)
        self.questions = [
            {"Frage": "Was sind die drei Hauptcharacktäre aus Harry Potter?", "antworten": ["Harry, Ron & Hermine", "Tick, Trick & Track", "Die drei Musketiere"], "richtig": "Harry, Ron & Hermine"},
            {"Frage": "Was ist die Resource mit der größten Knappheit der Welt?", "antworten": ["Bitcoin", "USD", "EURO"], "richtig": "Bitcoin"},
            {"Frage": "Was sind Politiker immer?", "antworten": ["korrupt", "gutaussehend", "arm"], "richtig": "korrupt"}
        ]
        self.index = 0   # Aktuelle Frage
        self.score = 0   # Richtige Antworten zählen
        self.remaining_time = 30  # Timer für jede Frage
        self.running = True
        self.selected_answer = tk.StringVar()  # Speichert die aktuell gewählte Antwort (Radiobutton)

        # GUI-Elemente (Labels, Buttons, Radiobuttons)
        self.question_label = tk.Label(root, text="", font=("Comic Sans MS", 14)) # Wahl der unprofessionellen Schriftart Comic Sans um Prüfer zu trollen
        self.question_label.pack(pady=10)
        self.radio_buttons = []
        for i in range(3):    # max. 3 Antworten / Frage
            rb = tk.Radiobutton(root, text="", variable=self.selected_answer, value="")
            rb.pack(anchor="w")
            self.radio_buttons.append(rb)
        self.timer_label = tk.Label(root, text="Zeit: 30", font=("Comic Sans MS", 12))
        self.timer_label.pack(pady=10)

        # Buttons für Steuerung
        self.next_button = tk.Button(root, text="Nächste Frage", command=self.naechste_frage)
        self.next_button.pack(pady=5)
        self.save_button = tk.Button(root, text="Ergebnisse speichern", command=self.ergebnisse_speichern)
        self.save_button.pack(pady=5)
        self.lade_button = tk.Button(root, text="Ergebnisse laden", command=self.ergebnisse_laden)
        self.lade_button.pack(pady=5)
        # Start: erste Frage laden und Timer starten
        self.load_question()
        self.start_timer()

    def load_question(self):
        """Lädt die aktuelle Frage in die GUI."""
        self.selected_answer.set("")  # Radiobutton-Auswahl zurücksetzen
        frage = self.questions[self.index]
        self.question_label.config(text=frage["Frage"])
        for i, text in enumerate(frage["antworten"]):
            self.radio_buttons[i].config(text=text, value=text)

    def start_timer(self):
        """Startet Timer in einem separaten Thread, um die GUI nicht zu blockieren."""
        def countdown():
            self.remaining_time = 30
            while self.remaining_time > 0 and self.running:
                time.sleep(1)  # Blockiert nur den Thread, nicht die GUI
                self.remaining_time -= 1
                self.timer_label.config(text=f"Zeit: {self.remaining_time}")
            if self.remaining_time == 0:
                self.naechste_frage()  # Automatisch nächste Frage, wenn Zeit abgelaufen

        # Thread für den Timer starten
        thread = threading.Thread(target=countdown, daemon=True)
        thread.start()

    def naechste_frage(self):
        """Prüft Antwort und lädt die nächste Frage oder zeigt Endergebnis."""
        self.running = False  # Stoppt Timer-Schleife
        if self.selected_answer.get() == self.questions[self.index]["richtig"]:
            self.score += 1  # Punkt für richtige Antwort

        self.index += 1
        if self.index < len(self.questions):
            self.running = True
            self.load_question()
            self.start_timer()
        else:
            # Quiz beendet → Ergebnis in Messagebox
            messagebox.showinfo("Quiz beendet", f"Dein Ergebnis: {self.score}/{len(self.questions)}")
            self.running = False

    def ergebnisse_speichern(self):
        """Speichert das aktuelle Ergebnis in einer Datei (Pickle)."""
        pfad = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle Dateien", "*.pkl")])
        if pfad:
            with open(pfad, "wb") as f:
                pickle.dump({"score": self.score}, f)
            messagebox.showinfo("Gespeichert", f"Ergebnis wurde gespeichert: {pfad}")

    def ergebnisse_laden(self):
        """Lädt ein vorher gespeichertes Ergebnis aus Datei."""
        pfad = filedialog.askopenfilename(filetypes=[("Pickle Dateien", "*.pkl")])
        if pfad:
            with open(pfad, "rb") as f:
                daten = pickle.load(f)
            messagebox.showinfo("Geladen", f"Früheres Ergebnis: {daten['score']} Punkte")



# Programmstart
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()




