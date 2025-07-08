# Eingabe einer Zahl, die eine Primzahl sein könnte.
input1 = int(input("Gebe eine Zahl ein, von der du denkst, sie wäre eine Primzahl, Alter: "))

# Bekannte Primzahlen innerhalb der Zahlen 1-100, um viel Rechenarbeit zu sparen.
# Erklärung: Wenn eine Zahl durch 6 teilbar ist, ist sie auch durch 3 und 2 teilbar
# Die Überprüfung von reinen prim-teilern reicht daher aus.
bekannte_primzahlen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

# Vorüberprüfung durch bekannte Primzahlen
is_primzahl = True
for primzahl in bekannte_primzahlen:
    if input1 % primzahl == 0 and input1 != primzahl:
        is_primzahl = False
        break

# Wenn die Zahl größer als die größte bekannte Primzahl ist,
# überprüfen wir weitere mögliche ungerade Teiler
# Wir brauchen nur Teiler, bis maximal zu der Wurzel, da x^2=x*x
# Das heißt, wenn ein Teiler größer wird als x, wird der andere kleiner als x
# Das heißt wir müssen maximal bis x überprüfen, also die Wurzel der Zahl
if is_primzahl and input1 > bekannte_primzahlen[-1]:
    root1 = round(input1 ** 0.5)
    ungeradeTeilermenge1 = set(range(max(bekannte_primzahlen[-1] + 1, 3), round(root1) + 1, 2))
    for i in ungeradeTeilermenge1:
        if input1 % i == 0:
            is_primzahl = False
            break

# Ausgabe des Ergebnisses
if is_primzahl and input1 > 1:
    print(input1, "ist eine Primzahl Alter! Super!")
else:
    print(input1, "ist keine Primzahl Alter!")
