def schaltjahr(jahreszahl):
    if jahreszahl % 4 == 0:
        if jahreszahl % 100 == 0:
            if jahreszahl % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

jahreszahl = int(input("Bitte ein Jahr eingeben! "))
if schaltjahr(jahreszahl):
    print(jahreszahl, "ist ein Schaltjahr")
else:
    print(jahreszahl, "ist kein Schaltjahr")
