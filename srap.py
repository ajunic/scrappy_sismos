import requests
from bs4 import BeautifulSoup
import pandas as pd

#Acceder a servidor
paginaScrap = 'http://www.iris.washington.edu/latin_am/evlist.phtml?region=mundo'
page = requests.get(paginaScrap)

#imprimir datos requeridos para graficar
soup = BeautifulSoup(page.text ,'lxml')
sismo_mag= float(soup.find('td' ,class_= 'mag').text)
sismo_latlon= soup.find('td' ,class_= 'latlon').text
sismo_dep= soup.find('td' ,class_= 'dep').text

#imprimir los valores de magnitud y long
if sismo_mag>4:
    for mag in soup:
        print(sismo_mag)
        for latlon in soup:
            print(sismo_latlon)


""" 
print(sismo_mag)
print(sismo_latlon)
print(sismo_dep)
 """

