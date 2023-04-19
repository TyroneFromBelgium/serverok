import sys
import time
from functions import *
from Cheetah.Template import Template

def check(bestand):
    while True:
        # Lees gegevens uit het opgegeven bestand in een dictionary
        gegevens = json_inlezen(bestand)
        
        # Voor elke server in de lijst met hosts, voer de volgende acties uit:
        for i, server in enumerate(gegevens["hosts"]):
            # Ping de website van de server en krijg de beschikbaarheid
            beschikbaarheid = ping_website(server["website"], server["ip"])
            # Wijzig de beschikbaarheidsstatus van de server in het dictionary-object
            # dat is opgeslagen in het opgegeven bestand, met behulp van de huidige iteratie-index
            json_wijzigen(bestand, beschikbaarheid, i)

        # Load the HTML template from a file
        with open('index.html') as f:
            template = Template(file=f)

        # Get the data to display in the report
        gegevens = json_inlezen(bestand)
        servers = gegevens['hosts']

        # Fill in the placeholders in the template with the data
        template.servers = servers
        output = str(template)

        # Write the generated HTML to a file
        with open('report.html', 'w') as f:
            f.write(output)


        # Wacht 120 seconden voordat u de lus opnieuw uitvoert
        time.sleep(120)


def main():
    if len(sys.argv) <= 1:
        mode = input("Choose a mode:\n1. Management mode\n2. Check mode\n")
        if mode == "1":
            management_mode()
        elif mode == "2":
            check_mode()
        else:
            print("Invalid mode. Choose 1 or 2.")
    else:
        mode = sys.argv[1]
        if mode == "management":
            management_action()
        elif mode == "check":
            check("hosts.json")
        else:
            print("Invalid mode.")
            sys.exit(1)


def management_mode():
    action = input("Choose an action:\n1. Show servers\n2. Add server\n3. Remove server\n")
    if action == "1":
        server_tonen("hosts.json")
    elif action == "2":
        website = input("Enter website name: ")
        ip = input("Enter IP address: ")
        server_toevoegen(website, ip, "hosts.json")
        print("Server added!")
    elif action == "3":
        website = input("Enter website name: ")
        server_verwijderen(website, "hosts.json")
        print("Server removed!")
    else:
        print("Invalid action. Choose 1, 2, or 3.")
        sys.exit(1)


def management_action():
    if len(sys.argv) < 3:
        print("Usage: python program.py management [show|add|remove]")
        sys.exit(1)

    action = sys.argv[2]

    if action == "show":
        server_toevoegen("hosts.json")
    elif action == "add":
        if len(sys.argv) != 5:
            print("Usage: python program.py management add [website] [ip]")
            sys.exit(1)

        website = sys.argv[3]
        ip = sys.argv[4]
        server_toevoegen(website, ip, "hosts.json")
        print("Server added!")
    elif action == "remove":
        if len(sys.argv) != 4:
            print("Usage: python program.py management remove [website]")
            sys.exit(1)

        website = sys.argv[3]
        server_verwijderen(website, "hosts.json")
        print("Server removed!")
    else:
        print("Invalid action. Choose show, add, or remove.")
        sys.exit(1)


def check_mode():
    print("Checking all servers every 2 minutes...")
    check("hosts.json")


if __name__ == "__main__":
    main()

