person = []
al = []
min_list=[]
#print(person)
#print(al)
'''
try:
    g = float(input("Eingabe der Größe in m: "))
except:
    g = 0
else:
    while (g>0):
        try:
            m = float(input("Eingabe der Masse in kg: "))
        except:
            g = 0
        else:
            person = [g,m]
            al.append(person)
            try:
                g = float(input("Eingabe der Größe in m: "))
            except:
                g = 0


print(al)
'''

al = [[1.70, 56],
[1.64, 67],
[1.98, 89],
[1.98, 120],
[1.62, 45],
[1.78, 70],
[1.82, 82],
[2.03, 110],
[1.85, 88],
[1.82, 83]]
mGroesse = 0
mMasse = 0

l = len(al)
if l>0:
    for i in range(l):
        mGroesse += al[i][0]
        mMasse += al[i][1]

    mGroesse /= l
    mMasse /= l
else:
    mMasse = None
    mGroesse = None

print(mGroesse, mMasse)

for i in range(l):
    dqg = 1-al[i][0]/mGroesse
    dqg *= dqg
    al[i].append(dqg)
    
    dqm = 1-al[i][1]/mMasse
    dqm *= dqm
    al[i].append(dqm)

print(al)

for i in range(len(al)):
	x = al[i][2]*al[i][3]
	min_list.append(x)

print(min_list)

min_index = min_list.index(min(min_list))

print("Nr.:",min_index,"Größe",al[min_index][0],"Masse",al[min_index][1])
