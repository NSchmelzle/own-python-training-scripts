#----------------------------------------------------------------
# Dateiname: Projektarbeit_Schmelzle_extraktive_Textzusammenfassung.py
# Textzusammenfassung eines climate science textes mit NLTK
# Autor: Nikhil Schmelzle
# Letzte Änderung: 06.08.2025
#--------------------------------------------------------------


# 📦 === [1] Imports & NLTK-Ressourcen vorbereiten ===========================
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import re

nltk.download("punkt")
nltk.download("stopwords")

# 📄 === [2] Text einlesen ====================================================
def load_text(filepath):
    """
    Liest einen Text aus einer Datei ein.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

# Beispielverwendung
text = load_text("velpTEC_K4.0070_3.0_Projektarbeit_Python_ClimateScienceText.txt")

# 🧹 === [3] Vorverarbeitung: Tokenisierung & Bereinigung =====================
def preprocess_text(text):
    """
    Tokenisiert den Text, entfernt Stopwords und Satzzeichen.
    Gibt Liste wichtiger Wörter zurück.
    """
    text = text.lower()
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))  # oder "german"
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return tokens

filtered_tokens = preprocess_text(text)

# 📊 === [4] Word Count berechnen ============================================
def compute_word_frequencies(tokens):
    """
    Zählt, wie oft jedes Wort vorkommt, und normiert die Werte.
    """
    freq_dict = {}
    for word in tokens:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    max_freq = max(freq_dict.values())

    for word in freq_dict:
        freq_dict[word] /= max_freq

    return freq_dict

word_freqs = compute_word_frequencies(filtered_tokens)

# 🧠 === [5] Sentence Scoring ================================================
def score_sentences(text, freq_dict):
    """
    Berechnet für jeden Satz einen Score basierend auf Wortfrequenzen.
    """
    sentence_scores = {}
    sentences = sent_tokenize(text)
    for sent in sentences:
        words = word_tokenize(sent.lower())
        sentence_score = sum(freq_dict.get(word, 0) for word in words)
        sentence_scores[sent] = sentence_score
    return sentence_scores

sentence_scores = score_sentences(text, word_freqs)

# 🧾 === [6] Top-Sätze extrahieren (Zusammenfassung) =========================
def get_summary(sentence_scores, percent=0.2):
    """
    Gibt die obersten x% Sätze als Zusammenfassung zurück.
    """
    import math
    n = math.ceil(len(sentence_scores) * percent)
    sorted_sents = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    summary = [sent for sent, score in sorted_sents[:n]]
    return "\n".join(summary)

summary = get_summary(sentence_scores)

# 📤 === [7] Ausgabe der Zusammenfassung ======================================
print("\n🔎 ZUSAMMENFASSUNG:\n")
print(summary)
