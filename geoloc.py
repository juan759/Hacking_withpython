
"""
Programa para geolocalizar el server.
Con la página ipinfo.io podemos obtener mucha información conociendo una dirección IP.

Author:Drxl
"""

import urllib.request
import json

def main():
    objetivo = "https://ipinfo.io/ip/json"
    urlliv = urllib.request.urlopen(open)
    cargajson = json.loads(urlliv.read())
    for dato in cargajson:
        print(dato+' : '+cargajson[dato])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
