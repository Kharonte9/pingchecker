#Autor: eduar766
#Modificaciones basicas por Kharonte

from requests import get, exceptions   
from colorama import Fore, init    
init()   
print(Fore.GREEN +"-------------------------------------------------------------")
print("""

   _____ _               _      _____ _____ _   _  _____ 
  / ____| |             | |    |  __ \_   _| \ | |/ ____|
 | |    | |__   ___  ___| | __ | |__) || | |  \| | |  __ 
 | |    | '_ \ / _ \/ __| |/ / |  ___/ | | | . ` | | |_ |
 | |____| | | |  __/ (__|   <  | |    _| |_| |\  | |__| |
  \_____|_| |_|\___|\___|_|\_\ |_|   |_____|_| \_|\_____|
  
""")

print("--------------------------------------------------------------")


print("¿Que URL quieres comprobar?")
url = input()

def check_internet_connection():
    try:
        get(url , timeout = 3)
        print('Hay conexion')
    except exceptions.ConnectionError:
        print('No hay conexion')

check_internet_connection()
