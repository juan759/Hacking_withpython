
"""
Programa para poder escanear los usuarios de una página de wordpress utilizando json(JavaScript
Object Notation) y urllib.request.

Puede haber errores de http ya que el codigo de la conexión puede ser 403,404,etc.
Donde el programa funciona pero el objetivo no esta activo o está protegido.

Author:Drxl
"""

import json
import urllib.request

def main():
    objetivo = urllib.request.urlopen("https://achirou.com/wp-json/wp/users")
    for x in json.loads(objetivo.read()):
        usuario = x['slug']
    print(usuario)

main()
