# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 09:30:26 2017

@author: 1537259
"""

a = 'Acapulco de Ju\u00e1rez, Guerrero, Mexico'

from unidecode import unidecode

a = 'Nova Igua\u00e7u, Rio de Janeiro, Brazil'
val=unicode(a)
b = val.decode('unicode_escape')
print(b)

val=unicode(a)
my_str = u"{}".format(val)
print(my_str)

##Write to csv file

## Open the file with read only permit
f = open('C:/Users/1537259/Documents/TimeSheets/scraping/GeoCode_utf_to_chr.csv', "r")
lines = f.readlines()
f.close()

wf = open('C:/Users/1537259/Documents/TimeSheets/scraping/GeoCode_utf_to_chr_all.txt', 'w')

for chr_str in lines[1:1600]:
   try:    
     val=unicode(chr_str)
     b = val.decode('unicode_escape')  
     print chr_str,b    
     wf.write((chr_str)+';'+str(b)+'\n')
   except:
       pass

wf.close()
    