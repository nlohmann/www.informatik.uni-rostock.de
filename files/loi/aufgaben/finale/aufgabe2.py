################################################################
#  _     ___ ___   ____   ___  _ _                             #
# | |   / _ \_ _| |___ \ / _ \/ / |                            #
# | |  | | | | |    __) | | | | | | LANDESOLYMPIADE INFORMATIK #
# | |__| |_| | |   / __/| |_| | | | 18./19. MÄRZ 2011, GÜSTROW #
# |_____\___/___| |_____|\___/|_|_|                            #
#                                                              #
# Aufgabe 2: Game of Life                                      #
################################################################


#--------------------------------------------------------------#
# dieser Code is vorgegeben - bitte nicht ändern

import random
random.seed()

# die Beispielwelt
example = [[0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 1]]

# generiere quadratische Welt (Kantenlänge size) mit
# zufälliger Generation
def generateWorld(size):
    result = []
    
    for i in range(0, size):
        line = []
        for j in range(0, size):
            line.append(random.randint(0,1))
        result.append(line)

    return result


# graphische Ausgabe eine Welt
def printWorld(world):
    size = len(world)
    
    print('+' + ('-' * size) + '+')
    for i in range(0, size):
        line = '|'
        for j in range(0, size):
            if (world[i][j] == 0):
                line += ' '
            else:
                line += 'o'
        print(line + '|')

    print('+' + ('-' * size) + '+')

#--------------------------------------------------------------#

# Diese Funktionen müssen von Dir geschrieben werden.

def neighbors(world, z, s):
    return 0


def evolve(world):
    return 0
