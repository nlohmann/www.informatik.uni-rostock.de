import random
random.seed()

def wuerfeln(anzahl):
    ergebnisse = [0,0,0,0,0,0,0,0,0,0,0,0,0]

    for i in range(0, anzahl):
        augen = random.randint(1,6) + random.randint(1,6)
        ergebnisse[augen] = ergebnisse[augen] + 1

    return ergebnisse


ergebnisse = wuerfeln(100)
print(ergebnisse)

maximum = 0
for i in range(0, len(ergebnisse)):
    if ergebnisse[i] > maximum:
        maximum = ergebnisse[i]

for i in range(0, len(ergebnisse)):
    if ergebnisse[i] == maximum:
        print(i, "wurde (mit) am häufigsten gewürfelt:", maximum, "mal")
