from datetime import datetime
import os
import json

def server_tonen(bestand):
    # Lees de huidige gegevens uit het bestand
    gegevens = json_inlezen(bestand)

    # Loop over de servers in de gegevens en druk de gewenste velden af
    for server in gegevens["hosts"]:
        print(server["website"], server["ip"], server["beschikbaarheid"], server["uitgevoerd_op"])

def server_toevoegen(website, ip, bestand):
    # Lees de huidige gegevens uit het bestand
    gegevens = json_inlezen(bestand)

    # Maak een nieuw dict aan voor de nieuwe server
    nieuwe_data = {
            'ip': ip, 'website': website,'beschikbaarheid': None,'uitgevoerd_op': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    
    # Controleer of de server al bestaat in de gegevens
    if website in str(gegevens):
        print("De website/server die u probeert toe te voegen bestaat al.")
    # Voeg de nieuwe server toe aan de gegevens en schrijf deze weg naar het bestand
    else:
        json_wegschrijven(bestand, nieuwe_data)

def server_verwijderen(website, bestand):
    # Lees de huidige gegevens uit het bestand    
    gegevens = json_inlezen(bestand)

    # Zoek naar de server die overeenkomt met de opgegeven website en verwijder deze
    for server in gegevens["hosts"]:
        if server["website"] == website:
            gegevens["hosts"].remove(server)

            # Schrijf de bijgewerkte gegevens terug naar het bestand
            with open(bestand, 'w') as f:
                json.dump(gegevens, f, indent=4, separators=(',',': '))

def ping_website(website, ip):
     # Een ping-commando uitvoeren voor de opgegeven website
    reply = os.system("ping -c 1 " + website)
    
    return "Website is up and running" if reply == 0 else "Website is down"
        
def json_inlezen(bestand):
    with open(bestand, 'r') as f:
        # JSON-gegevens lezen uit het opgegeven bestand
        gegevens = json.load(f)
        # De gelezen gegevens retourneren als een Python-dictionary
        return gegevens

def json_wegschrijven(bestand, nieuwe_data):
    # De bestaande gegevens uit het JSON-bestand inlezen
    gegevens = json_inlezen(bestand)

    # De nieuwe gegevens toevoegen aan de bestaande gegevens
    gegevens["hosts"].append(nieuwe_data)

    # De bijgewerkte gegevens wegschrijven naar het JSON-bestand
    with open(bestand, 'w') as f:
        json.dump(gegevens, f, indent=4, separators=(',',': '))


def json_wijzigen(bestand, gewijzigde_data, index):
    # JSON bestand inlezen en data ophalen
    gegevens = json_inlezen(bestand)

    # Loop door de lijst van hosts in de JSON data
    for server in gegevens["hosts"]:
            # Update de beschikbaarheid van de host op de opgegeven index
            gegevens["hosts"][index]["beschikbaarheid"] = gewijzigde_data
            # Update de uitvoerdatum en tijd van de laatste wijziging
            gegevens["hosts"][index]["uitgevoerd_op"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Schrijf de aangepaste JSON data terug naar het bestand
    with open(bestand, 'w') as f:
        json.dump(gegevens, f, indent=4, separators=(',',': '))
