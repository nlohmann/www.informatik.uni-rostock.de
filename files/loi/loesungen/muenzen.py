betrag = float(input("Bitte einen Euro-Betrag eingeben! "))

liste = list()

while betrag >= 2.00:
    betrag = betrag - 2.00
    liste.append("2€")

while betrag >= 1.00:
    betrag = betrag - 1.00
    liste.append("1€")

while betrag >= 0.50:
    betrag = betrag - 0.50
    liste.append("50c")

while betrag >= 0.20:
    betrag = betrag - 0.20
    liste.append("20c")

while betrag >= 0.10:
    betrag = betrag - 0.10
    liste.append("10c")

while betrag >= 0.05:
    betrag = betrag - 0.05
    liste.append("5c")

while betrag >= 0.02:
    betrag = betrag - 0.02
    liste.append("2c")

while betrag > 0:
    betrag = betrag - 0.01
    liste.append("1c")


print("Man braucht mindestens", len(liste), "Münzen:", liste)    
