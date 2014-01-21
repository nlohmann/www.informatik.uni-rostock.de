import random,tkinter
from tkinter import *

#      einmaliges Starten des Zufallszahlengenerators 'zufall'
#      Random zufall = new Random();

def dice():
    wliste = []  
    # Schleifenbeginn: 3*würfeln
    for i in range(1,4):

        # Erzeugen einer Zufallszahl von 1..6
        augenzahl = random.randint(1,6)
        wliste.append(augenzahl)
        # Falls erste 6 gewürfelt wird ...
        sechs = 0
        if (augenzahl==6):
            # Solange 6en gewürfelt werden, wiederhole

            while (augenzahl==6):
                # Würfeln

                augenzahl = random.randint(1,6)
                wliste.append(augenzahl)
                # Ende der Wiederholungen nach 6er-Serie
                 
            # Abbruch des Durchlaufs der for-Schleife
            break

        # Ende if-Verzweigung
              
    # Schleifenende for
    return wliste

def drucke(liste):
    liste = str(dice())
    text1=str(liste)
    label.config(text=text1)
    

def speichere(liste):
    datei=open('./hurz.txt','w')
    datei.write(liste)
    datei.close()














liste = dice()
print(liste)
speichere(str(liste))












