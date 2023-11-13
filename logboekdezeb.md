## Les 1: Python en security - intro

**Wat is ethical / white-hat hacking?**

Ethical hacking a.k.a white-hat hacking, is als het spelen van de rol van een goede detective in de digitale wereld. In plaats van je vaardigheden te gebruiken om anderen schade toe te brengen of te stelen, zet je ze in om te helpen beschermen en verbeteren. Het belangrijkste om te onthouden is dat je altijd toestemming moet hebben voordat je begint met hacken.

**In welke context gebeurt dit?**

Ethisch hacken of white-hat hacken gebeurt in de context van cybersecurity, wat draait om het beschermen van computers, netwerken, websites en digitale systemen tegen kwaadaardige aanvallen en inbraken. Enkele voorbeelden:

- Softwareontwikkeling: Softwarebedrijven huren ethische hackers in om hun apps en programma's te onderzoeken op beveiligingslekken voordat ze worden uitgebracht.
- Overheidsinstellingen: Overheidsorganisaties kunnen ethische hackers inschakelen om de beveiliging van kritieke infrastructuur te testen

**Wat zijn de basis-voorwaarden om aan ethical hacking te doen?**

Er zijn een aantal voorwaarden waar men zich aan moet houden als je aan ethical hacking wilt doen.

- Toestemming: Je moet altijd schriftelijke toestemming hebben van de eigenaar van het systeem of de organisatie voordat je ethisch hacken uitvoert. Vermeldt altijd wat je gaan hacken, hoe, wanneer en wat de impact gaat zijn van uw acties.
- Naleving van ethische richtlijnen: Handel altijd met integriteit en professionaliteit, respecteer de vertrouwelijkheid en privacy van gegevens.
- Geheimhouding: Vulnerabilities die je vindt tijdens je hacking hebt verkregen strikt vertrouwelijk houden en niet delen zonder de toestemming.

**Wat is pentesting?**

Een pentest a.k.a penetratietest of binnendringingstest, controleert computersystemen en software op kwetsbaarheden die hackers in staat kunnen stellen om binnen te dringen. Enkele voorbeelden van pentesting zijn:

- Scannen van netwerken (nmap)
- Social Engineering
- Phishing
- Privilege Escalation en nog meer...

**Wat zijn de verschillende fasen die in de literatuur worden beschreven? Meer**

**bepaald: wat wordt begrepen onder “reconaissance”. Beschrijf!**

Onder reconnaissance verstaan we de praktijk van heimelijk informatie ontdekken en verzamelen over een systeem. Deze methode wordt vaak gebruikt bij ethical hacking of pentesting.

We kunnen onderscheid maken tussen 2 types reconnaissance:

*Active reconnaissance:*

Houdt in dat hackers rechtstreeks met het computersysteem communiceren en proberen informatie te verkrijgen. Het is in het algemeen sneller en preciezer, maar riskanter omdat het meer storing veroorzaakt binnen een systeem en een grotere kans heeft om te worden gedetecteerd.

*Passive reconnaissance:*

Verzamelt informatie zonder rechtstreeks met systemen te communiceren, met behulp van hulpmiddelen zoals Wireshark en Shodan.

**Wat is bug bounty? Welke zijn de mogelijkheden om aan bug bounty te doen?**

Een bug bounty is een programma dat wordt aangeboden door bedrijven, waarbij individuen of groepen worden aangemoedigd om bugs in hun software, websites, of systemen te vinden en te rapporteren. Vaak heeft deze ook een geldprijs.

**Hoe verhoudt het Belgische Intigriti (intigriti.com) platform zich hiertoe?**

Intigriti is een bedrijf dat een platform aanbiedt voor ethical hackers om deel te nemen aan bug bounty-programma's. Het platform van Intigriti fungeert als een bemiddelaar tussen organisaties die hun systemen willen laten testen op bugs en degenen die bereid zijn deze tests uit te voeren.

**Hoe ga je te werk bij bug bounty? Wat is de beste aanpak voor een beginnend bounty hunter?**

- Leer de basisprincipes van cybersecurity: Leer over netwerken, webapplicaties, besturingssystemen enz...
- Kies een platform (Intigriti, HackerOne, Bugcrowd...)
- Voer een passieve reconnaissance (of actief indien toegelaten).
- Begin met testen
- Rapporteer je bevindingen

**Demo 1: Informatie inwinnen via request en socket**

>**In welke context kan dit nuttig zijn?**

>>- Website-analyse
>>- IP-lookup
>>- Locatiegegevens

>**Kan je dit algemener uitbreiden naar een pure ip-context?**
**
>>Het script kan zeker worden uitgebreid naar een meer algemene IP-context door bijvoorbeeld te zoeken naar open poorten, traceroutes uit te voeren, of andere netwerkgerelateerde informatie te verzamelen.

>**Kan je specifieke informatie verkrijgen naargelang de context?**
**
>>Afhankelijk van de context kun je aanvullende informatie verkrijgen door het script uit te breiden. Bijvoorbeeld, als je een beveiligingsonderzoek uitvoert, kun je proberen om informatie over de beveiligingsconfiguratie van de website te verzamelen, zoals SSL-certificaten en ciphersuites.

>**Ervaring met het testen van deze script:**

>>`Ik heb het script uitgevoerd en heb bijvoorbeeld de website van de AP Hogeschool gecontroleerd. Het script vereist een URL als argument en haalt vervolgens de websiteheaders op, inclusief serverinformatie. Met behulp van 'socket.gethostbyname' heeft het script het IP-adres van de AP Hogeschool-website achterhaald en weergegeven. Daarna heb ik extra IP-informatie opgehaald van "ipinfo.io", zoals de locatie, regio, stad en land waar de server zich bevindt

**Demo 2: Poort scannen met Nmap in Python**

>**Welke poort(en) staan open?**
**
>>tcp': {80: {'state': 'open', 'reason': 'syn-ack', 'name': 'http',

>>'product': '', 'version': '', 'extrainfo': '', 'conf': '3', 'cpe': ''}

>>De enige openstaande poort in de 'tcp'-sectie is poort 80, die wordt gebruikt voor HTTP.

>**Wat doet deze script?**

>>Het script maakt gebruik van de Nmap-module om poortscans uit te voeren op een opgegeven target. Het target wordt als een argument aan het script doorgegeven. Vervolgens worden de opgegeven poorten (21, 22, 80, 139, 443 en 8080) gescand.

>>Tijdens de scan wordt de status van elke poort gecontroleerd en weergegeven,samen met de status van het target. De resultaten worden afgedrukt met informatie over de staat van elke poort en of het target online is.

**Demo 4: Screenshots nemen**

>**Bedenk zelf enkele mogelijke use cases voor het maken van screenshots.**
**
>>Foutenrapportage: Stel dat een gebruiker een foutmelding op hun computer ziet,zoals een softwarecrash. Ze kunnen een screenshot maken van de foutmelding en deze naar de klantenondersteuning sturen voor diagnose en oplossing.

>**Een ftp-oppik en afzetplek voor informatie gebruiken heeft voor en nadelen. Wat zijn alternatieven?**

>>Social media, email, WeTransfer (Wat wij studenten vaak gebruiken om grote files te sharen).

>**Wat doet deze script?**

>>In essentie neemt dit script een screenshot van het huidige scherm, slaat deze op als "grabbed.png", en stuurt het vervolgens via FTP naar een specifieke server met de opgegeven inloggegevens (test, test).

## Les 3: Python - werken met Socket en Scapy
Voor week 3 heb ik de experimenten gemaakt dat werden gevraagd. Dit houdt in:

- **Host Discovery**
  - Gegeven een bepaalde IP-range het netwerk doorzoeken naar beschikbare hosts (bijv via ARP)

- **Service Discovery**
  - Gegeven het IP-adres van één of meerdere hosts (bijv als resultaat van de hierboven beschreven sweep) voer je een poort scan uit (voor alle poorten onder 1024)

- **Remote OS Detectie**
  - Je voert een actieve fingerprinting uit op één of meerdere hosts (bijv als resultaat van de hierboven beschreven sweep) en detecteert op basis hiervan het OS van de host

- **Pcap Analyse**
  - Je analyseert één of meerdere hosts op de aanwezigheid van HTTP-verkeer (één of meerdere andere soorten verkeer mogen uiteraard ook: SMTP, POP3, IMAP)

## Les 5: Python Web hacking / Scapy / Cryptografie

Ik koos ervoor om cryptografische oefeningen te doen in plaats van web hacking oefeningen of werken met het Django-framework omdat ik een sterke interesse heb in de fundamenten van cybersecurity en informatiebeveiliging. Cryptografie vormt de basis van beveiligingsmaatregelen en helpt gegevens te beschermen tegen ongeautoriseerde toegang en manipulatie. Ik wilde een diepgaand begrip ontwikkelen van hoe versleutelingssystemen werken, hoe ze kunnen worden gebruikt om gegevens te beschermen en welke zwakke punten ze kunnen hebben.

**Stap 1: Kennisverwerving**

Ik begon met het verwerven van basiskennis over cryptografie, encryptie en decryptie. Dit omvatte het begrijpen van verschillende encryptie-algoritmen. Caesar versleuteling, kolomtranspositie versleuteling enz.

**Stap 2: Eencryptie-oefeningen**

Ik begon met eenvoudige oefeningen waarbij ik tekstberichten of bestanden versleutelde met verschillende encryptie-algoritmen. Dit hielp me om vertrouwd te raken met de encryptieprocessen. Ik had bijvoorbeeld nooit gehoord van kolomtranspositie versleuteling en dus bij deze ben ik dan geinformeerd.

**Stap 3: Decryptie-oefeningen**

Nu ging ik verder met het ontcijferen van versleutelde berichten of bestanden. Het was leuk bedacht om eerst een script te schrijven waarin je een boodschap moest encrypteren en kort later het weer moest gaan decrypteren met een script. 

## Les 7: Python: Wi-Fi reconnaissance

**Ik koos ervoor om een WiFi scanner te schrijven met Scapy.**

Uitleg script:

Dit Python-script maakt gebruik van de Scapy-bibliotheek om Wi-Fi-pakketten te onderscheppen en informatie over draadloze toegangspunten (Access Points, APs) vast te leggen. Het script begint met het importeren van de nodige modules van Scapy, namelijk Dot11, sniff, en Dot11Elt.

Vervolgens wordt een lege lijst genaamd AccessPointsList geïnitialiseerd. Deze lijst zal worden gebruikt om bij te houden welke APs zijn gedetecteerd tijdens het uitvoeren van het script.

Het script definieert een functie genaamd HandleWiFiPackets(pkt) die wordt aangeroepen telkens wanneer een Wi-Fi-pakket wordt onderschept door sniff. Binnen deze functie wordt gecontroleerd of het onderschepte pakket een Wi-Fi-pakket is, wat wordt gedaan door te kijken of het een Dot11-laag heeft.

Vervolgens controleert het script of het onderschepte pakket een probe request-pakket is (subtype 8) van een Wi-Fi-client naar een AP (type 0 en subtype 8). Als dit het geval is, gaat het verder met de verwerking.

Het script kijkt dan of het MAC-adres van het AP (pkt.addr2) al in de lijst AccessPointsList staat. Als het MAC-adres nog niet in de lijst staat, wordt het toegevoegd aan de lijst.

Verder haalt het script informatie op over het AP, zoals de SSID van het AP, de signaalsterkte (uitgedrukt in dBm), en het kanaal waarop het AP actief is.

Ten slotte drukt het script de verzamelde informatie af in de console. Deze informatie omvat het MAC-adres van het AP, de SSID, de signaalsterkte en het kanaal waarop het AP zich bevindt.

Het script maakt gebruik van de sniff-functie om pakketten te onderscheppen op de draadloze netwerkinterface "wlan0". Telkens wanneer er een pakket wordt onderschept, roept het de HandleWiFiPackets-functie aan om de relevante informatie vast te leggen en weer te geven. Hierdoor kan het script continu draaien en nieuwe pakketten blijven onderscheppen en verwerken terwijl het actief is. Dit is handig om een overzicht te krijgen van draadloze APs in de buurt en informatie over hun signaalsterkte en kanaal.
