#!/usr/bin/python 3
# COADER : AKASH BLACK HAT
# TRADUCTEUR : LUXUSE
import os

try:
    import requests
except:
    os.system("pip install requests")
try:
    import colorama
except:
    os.system("pip install colorama")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
from colorama import *

auth = '1840e53e-0a8b-4d4d-b4e6-4d34d1033d91';
import time as t

t.sleep(2)
os.system("clear")



def loop():
    head = pyfiglet.figlet_format("__")
    os.system("clear")
    print(Fore.GREEN + head)
    print(Fore.GREEN + """    
██╗     ██╗██╗   ██╗███████╗
██║     ██║██║   ██║██╔════╝
██║     ██║██║   ██║█████╗  
██║     ██║╚██╗ ██╔╝██╔══╝  
███████╗██║ ╚████╔╝ ███████╗
╚══════╝╚═╝  ╚═══╝  ╚══════╝ V1.1 trad luxuse                                                                                                                                              
   ┌┬┐┬─┐┌─┐┌─┐┬┌─┌─┐┬─┐
    │ ├┬┘├─┤│  ├┴┐├┤ ├┬┘
    ┴ ┴└─┴ ┴└─┘┴ ┴└─┘┴└─                                                                                                                                                       
 ==============================================
[+]Author  : Akash Black Hat                 [+]
= traducteur luxuse : https://github.com/Luxuse 
[+]GitHub  : https://github.com/akashblackhat[+]""")
    print(Fore.GREEN + """ ==============================================""")
    # print("Usage:Iptracker [Ip address]\n\nExample:Iptracker our prsnal ip")
    print(Fore.GREEN + """
    Type \"show\" pour afficher toutes les commandes """)

    def track():
        tip = input(Fore.MAGENTA + "Iptracker > " + Style.RESET_ALL)
        if tip == "help":
            print(Fore.BLUE + """
           show : Affiche toutes les commandes
            iptracker : Il est utilisé pour suivre une adresse Ip
            help : Affiche comment utiliser cet outil
            exit : Pour quitter ip tracker

            update : Pour mettre à jour Ip-Tracker automatiquement
            """)
            track()
        elif tip == "show":
            print(Fore.BLUE + """


           Voici les commandes disponibles
            help
            show
            exit
            iptracker
            update
            """)
            track()
        elif tip == "exit":
            print(
                Fore.YELLOW + "Merci d'avoir utilisé mon outil. Si vous trouvez une erreur, n'hésitez pas à m'envoyer un message sur whatsapp.")
            exit()
        elif tip == "iptracker":
            print(Fore.GREEN + """________________________________Track Ip____luxuse-trad________________________""")
            print("""
            """)

            ip = (input(Fore.YELLOW + Back.RED + "Saisir l'adresse IP : " + Style.RESET_ALL + ""))
            print(Fore.CYAN + " Récupération de données à partir de " + ip)

            def get_location():
                ip_address = ip
                response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()

                location_data = {
                    "Ip Address": ip_address,
                    "city": response.get("city"),
                    "region": response.get("region"),
                    "country": response.get("country_name"),
                    "Ip Address Type": response.get("version"),
                    "Region Code": response.get("region_code"),
                    "Postal Code": response.get("postal"),
                    "Latitude": response.get(str("latitude")),
                    "Longitude": response.get(str("longitude")),
                    "TimeZone": response.get("timezone"),
                    "Country code": response.get("country_calling_code"),
                    "Currency": response.get("currency"),
                    "Currency Name": response.get("currency_name"),
                    "Languages": response.get("languages"),
                    "Country Area": response.get("country_area"),
                    "Population": response.get("country_population"),
                    "ASN": response.get("asn"),
                    "Organization": response.get("org")

                }
                latitude = response.get("latitude")
                global lat
                lat = str(latitude)
                longitude = response.get("longitude")
                global long
                long = str(longitude)

                global url
                url = "https://google.com/maps/place/" + lat + "," + long + "/@" + lat + "," + long + ",16z"

                return location_data

            print(Fore.YELLOW, get_location())
            print(Fore.YELLOW + "\nGoogle Maps: " + Fore.GREEN + url)
            opn = "xdg-open " + url
            map = input(Fore.CYAN + "\n\nVoulez-vous ouvrir la localisation sur google map ? [yes/no]: " + Style.RESET_ALL)
            if map == "yes" or map == "Oui":
                os.system(opn)

        elif tip == "update":
            print(Fore.GREEN + "Mise à jour de l'Ip Tracker")
            os.system("""
            cd
            rm -f -r Ip-Tracker
            https://github.com/akashblackhat

            """)

            print(Fore.BLUE + """Tapez maintenant la commande suivante
            cd $HOME
            cd Ip-Tracker
            python3 tracker.py
            """)
            exit()
        else:
            print(Fore.RED + "Commande non valide !")
            t.sleep(3)
            track()

    track()

    cont = input(
        "\n\n" + Fore.YELLOW + Back.RED + "Souhaitez-vous suivre une autre adresse IP ?[y/n] " + Style.RESET_ALL + " ")
    if cont == "y" or cont == "Y":
        loop()
    else:
        exit()


loop()
# HAPPY HACKING
