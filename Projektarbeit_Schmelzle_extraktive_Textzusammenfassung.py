#----------------------------------------------------------------
# Dateiname: Projektarbeit_Schmelzle_extraktive_Textzusammenfassung.py
# Textzusammenfassung eines Climate-Science-Textes mit NLTK
# Autor: Nikhil Schmelzle
# Letzte Änderung: 08.08.2025
#----------------------------------------------------------------
#1 Imports & NLTK-Ressourcen vorbereiten
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
import string
import math
import re
nltk.download("stopwords")  # Punkt nicht nötig, hat lokal bei mir Probleme gemacht, musste ich rausnehmen

#2 Text einlesen
def load_text(filepath):
    """Liest den Inhalt einer Datei ein"""
    with open(filepath,"r",encoding="utf-8") as file:
        return file.read()
text =load_text("velpTEC_K4.0070_3.0_Projektarbeit_Python_ClimateScienceText.txt")

#3 Vorverarbeitung des Textes: Wörter bereinigen
def preprocess_text(text):
    """Tokenisiert den Text, entfernt Stopwords und Satzzeichen"""
    text= text.lower() #kleinschreibung für Gleichbehandlung aller Wörter
    tokens =wordpunct_tokenize(text)
    stop_words =set(stopwords.words("english"))
    tokens= [word for word in tokens if word not in stop_words and word not in string.punctuation]
    return tokens
filtered_tokens = preprocess_text(text)

#4 Word Counts berechnen
def compute_word_frequencies(tokens):
    """Berechnet normalisierte Häufigkeiten der Wörter"""
    freq_dict = {}
    for word in tokens:
        freq_dict[word] = freq_dict.get(word,0)+1
    max_freq = max(freq_dict.values())
    for word in freq_dict:
        freq_dict[word] /=max_freq
    return freq_dict
word_freqs=compute_word_frequencies(filtered_tokens)

#5 Sentence Scoring
def score_sentences(text, freq_dict):
    """Bewertet Sätze basierend auf den Wortfrequenzen"""
    sentence_scores = {}
    sentences = re.split(r'(?<=[.!?]) +',text)  # einfache Satztrennung
    for sent in sentences:
        words = wordpunct_tokenize(sent.lower())
        score = sum(freq_dict.get(word,0) for word in words)
        if len(words) > 3:  # Filter: keine sehr kurzen Sätze bewerten
            sentence_scores[sent]=score
    return sentence_scores
sentence_scores=score_sentences(text, word_freqs)

# 6 Zusammenfassung erzeugen
def get_summary(sentence_scores, percent=0.2):
    """Gibt die obersten (x)% Sätze als Zusammenfassung zurück"""
    n = math.ceil(len(sentence_scores)*percent)
    sorted_sents = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
    top_sents =[sent for sent, score in sorted_sents[:n]]
    top_sents.sort(key=lambda s: text.find(s))  # Originalreihenfolge
    return "\n".join(top_sents)

summary = get_summary(sentence_scores)

# 7 Ausgabe der Zusammenfassung
print("\n ZUSAMMENFASSUNG:\n")
print(summary)