
"""
Este es un programa para obtener información sobre los headers de una pagina web

argparse es un modulo para poder poner opciones en la linea de comandos,argumentos y
sub-comandos.Esto se ve reflejado ya que para compilar el archivo debemos usar :
>python headerweb.py
Si le damos enter nos arroja un error ya que no le hemos pasado el bojetivo, para
solucionarlo solo debemos escribir:
>python headerweb.py -t/--target https://elobjetivo

Author:Drxl
"""

import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="Objetivo")
parser = parser.parse_args()

def main():
    if parser.target:
        try:
            objetivo = requests.get(url=parser.target)
            header = dict(objetivo.headers)
            for x in header:
                print(x +" : "+header[x])
        except:
            print("No se pudo obtener la conexión.")
    else:
        print("Hubo algun error en el objetivo..")

if __name__ == "__main__":
    main()
