'''Das Programm spielt Mastermind mit dem Benutzer'''
import random
random.seed()

farben = ['blau','gelb','rot','gruen']
code = []
auswertung = ['x','x','x','x']
eingegeben = ['x','x','x','x']


def codeErstellen ():
    liste = ['x','x','x','x']
    for i in range(0,4):
        zufall = random.randint(0,3)
        while farben[zufall] in liste:
            zufall = random.randint(0,3)
        liste[i] = farben[zufall]
    return liste


def eingabe ():
    for i in range(0,4):
        print ()
        print (i+1,'te Farbe: ')
        eingegeben[i] = str(input())
    return eingegeben


def pruefen (liste):
    platz = 0
    farbe = 0
    for i in range(0,4):
        if code[i] == liste[i]:
            platz += 1
        elif liste[i] in code:
            farbe += 1
    print ('','O'*platz,'\n','X'*farbe)
    

    
while (True):
    pruefe = []
    code = codeErstellen()
    # print (code)
    print ('Hallo lieber Nutzer, ich spiele Mastermind mit dir.')
    print ('Der Code ist vierstellig und es gibt die Farben:\nlila, blau, gelb, rot und gruen.')
    print ('Ein X sagt dir, dass eine Farbe stimmt.\nEin O sagt dir, dass eine richtige Farbe am richtigen Platz ist.')


    while (pruefe != code):
        pruefe = eingabe()
        print ('-----------------------------------')
        print ('Deine Eingabe:\n',pruefe,'\n')
        pruefen (pruefe)
        print ('-----------------------------------')

    print ('Super, du hast es erraten.')
    print ('Zum Vergleich mein Code: ',code) 
    antwort = input('Nochmal? N/J: ')
    if antwort == 'N':
        break

print ('Tschüß')
