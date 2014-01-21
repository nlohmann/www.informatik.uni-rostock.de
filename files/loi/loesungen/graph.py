kanten = {('a','b'), ('b','c'), ('b','d'), ('d','b'), ('c','a')}


def erreichbar(a,b, seen=[]):
    '''gibt zurück, ob von Knoten a aus Knoten b erreichbar ist'''

    # wir merken uns, wo wir bereits waren
    seen = seen + [a]

    # nehme die globale Variable 'kanten' für den Graphen
    global kanten

    # Fall 1: wir finden die Kante, mit der wir das Ziel erreichen
    if (a,b) in kanten:
        return True

    # Fall 2: wir sind bereits am Ziel angekommen
    if a == b:
        return True

    # Fall 3: wir suchen eine Kante, die uns näher ans Ziel bringt
    for (x,y) in kanten:
        # Kante beginnt hier und Ziel wurde noch nicht besucht
        if x == a and y not in seen:
            return erreichbar(y,b,seen)

    # Ziel ist nicht erreichbar
    return False




def pfad(a,b, seen=[]):
    '''gibt den Pfad von Knoten a nach Knoten b'''

    # wir merken uns, wo wir bereits waren
    seen = seen + [a]

    # nehme die globale Variable 'kanten' für den Graphen
    global kanten

    # Fall 1: wir finden die Kante, mit der wir das Ziel erreichen
    if (a,b) in kanten:
        # gib bisher gesehene Kanten und Ziel aus
        return seen+[b]

    # Fall 2: wir sind bereits am Ziel angekommen
    if a == b:
        # gib bisher gesehene Kanten aus
        return seen

    # Fall 3: wir suchen eine Kante, die uns näher ans Ziel bringt
    for (x,y) in kanten:
        # Kante beginnt hier und Ziel wurde noch nicht besucht
        if x == a and y not in seen:
            return pfad(y,b,seen)

    # es wurde kein Weg gefunden
    return []
