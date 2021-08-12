
"""
Este es un programa para poder obtener información conocienco unicamente el
dns(Domain Name System) de nuestro Objetivo.

https://www.ibm.com/docs/es/itcam-transactions/7.4.0.1?topic=monitor-dns-query-types
La pagina anterior es para saber qué tipo de información queremos obtener, es decir a usar con
el módulo dns.resolver.query("objetivo","algunadelasopcionesenlapagina")

Author:Drxl
"""

import dns.resolver

def main():
    try:
        objetivo = dns.resolver.resolve("achirou.com","A")
        for x in objetivo:
            print(x)
    except:
        print("No se obtuvo información")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
