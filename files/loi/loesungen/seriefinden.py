liste = [1,2,1,1,8,4,5,5,6,5,4,2,2,2,2,3,1,5,6,4]
    
position = 0
laenge = 1
wert = liste[0]
    
lliste = len(liste)

templength = 1

for i in range (1,lliste):
    if (liste[i]==liste[i-1]):
        templength +=1
        if (templength > laenge):
            wert = liste[i]
            laenge += 1
            position = i - laenge + 1
    else:
        templength = 1


print("Position: ",position)
print("Laenge:   ",laenge)
print("Wert:     ",wert)
    
