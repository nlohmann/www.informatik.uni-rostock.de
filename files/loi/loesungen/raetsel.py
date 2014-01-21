#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Stefanie on 2011-01-21.
Copyright (c) 2011 . All rights reserved.
"""

def wortfinden(liste, suchwort, richtung):
	
	for i in range(len(liste)):
		wort = liste[i].find(suchwort)
		if wort != -1:
			for  j in range(len(suchwort)):	
				if richtung == 'quer':
					print(i, wort + j, ' ' , end = '')
				elif richtung == 'laengs':
					print(wort + j, i, ' ', end = '')
	print()
				


suchwort = 'COOL'
#suchwortOhne = suchwort.replace(' ','')

dateiname = 'Raetsel.txt'
datei = open(dateiname, 'r')

zeilen = datei.readlines()
lz = len(zeilen)
print(lz)
datei.close()

print(zeilen)


# Spalten voreinstellen
# spalten = [['*'] * lz for i in range(lz)] # zweidimensionale Liste mit lz Elementen
spalten = ['' for i in range(lz)]

for  i in range(lz):
	for j in range(lz):
		spalten[i] += zeilen[j][i]
		
print (spalten)

wortfinden(zeilen, suchwort, 'quer')
wortfinden(spalten, suchwort, 'laengs')
wortfinden(zeilen, suchwort[::-1], 'quer')	# [::-1] dreht den String um
wortfinden(spalten, suchwort[::-1], 'laengs')


			
