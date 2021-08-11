
"""
Este es un programa para obtener los temas de una pagina hecha con wordpress.
Utilizando el modulo requests y bs4

Author:Drxl
"""


import requests as rq
from bs4 import BeautifulSoup

"""
r=rq.get("https://achirou.com")
print(r.status_code)
"""


def main():
    agente = {'User-Agent':'Firefox'}
    objetivo = rq.get(url="https://achirou.com",headers=agente)

    #Utilizamos BeautifulSoup para parsear.
    #Almacenar el parseamos con BeautifulSoup.Sobre la libreria html5lib
    parsear = BeautifulSoup(objetivo.text,'html5lib')

    #Href es lo que buscamos dentro de wp-content/themes
    for link in parsear.find_all('link'):
        if 'wp-content/themes' in link.get('href'):
            tema = link.get('href')
            tema = tema.split('/')
            if 'themes' in tema:
                posicion = tema.index('themes')
                temas = tema[posicion+1]
                print("El tema que usa es:"+ temas)

if __name__== '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
