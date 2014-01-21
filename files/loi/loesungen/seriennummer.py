def eingabe():
    liste = list()
    
    while True:
        eintrag = int(input("Bitte Seriennummer eingeben (0 für Ende): "))
        if eintrag == 0:
            print("Eingegebene Liste:", liste)
            return liste
        else:
            liste.append(eintrag)


def rechnen(liste):
    anzahl = len(liste)
    maximum = max(liste)
    return (maximum + (maximum/anzahl) - 1)

liste = eingabe()
anzahl = rechnen(liste)
print("Es gibt ungefähr", anzahl, "Geräte")
