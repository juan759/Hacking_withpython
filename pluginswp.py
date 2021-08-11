
"""
Este es un programa para obtener los pluggins de una pagina hecha con wordpress.
Utilizando el modulo requests.Y del modulo os la clase path, para leer archivos o listados
de pluggins para hacer bypass de los pluggins.Y del modulo progress.bar la clase Bar para una
barra de avance.

akismet es un pluggin muuy común

Author:Drxl
"""
import requests as rq
from os import path
from progress.bar import Bar

def main():
    if path.exists("wp_plugins.txt"):
        pluggins = open("wp_plugins.txt","r")
        pluggins = pluggins.read().split("\n")
        list = []
        objetivo = "https://achirou.com"
        barra = Bar("Procesando ...",max=len(pluggins))

        for pluggin in pluggins:
            barra.next()
            try:
                plu=rq.get(url=objetivo+"/"+pluggin)
                if plu.status_code == 200:
                    resultado = objetivo+""+pluggin
                    lista.append(resultado.split("")[-2])
            except:
                pass
        barra.finish()
        for pluggin in lista:
            print("Plugins:{}".format(pluggin))

    else:
        print("No se encontró la lista o el archivo 'wp_pluggins.txt'.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
