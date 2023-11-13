Berat Aksoy / Ethical Hacking
**Les 1: Python en security - intro**

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
