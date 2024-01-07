## Usage
- python main.py --hostname www.example.be
- python main.py --ip 192.168.0.0

## Eindopdracht Python: Pentesting Toolkit

**portscanner.py**

- Beschrijving: Wordt gebruikt voor het scannen van netwerkpoorten op een doelhost. Het identificeert open poorten en actieve diensten (services).
- Belang: Een essentiële tool voor netwerkbeveiligingsbeoordelingen, helpt bij het identificeren van potentiële toegangspunten voor aanvallen.

**certretriever.py**

- Beschrijving: Wordt gebruikt om SSL/TLS-certificaten van servers op te halen. Het is cruciaal in een pentesting toolkit voor het beoordelen van de veiligheid van deze certificaten, het identificeren van verouderde of kwetsbare configuraties, en het garanderen dat communicatiekanalen veilig versleuteld zijn.
- Belang: Een essentiële tool voor het evalueren van de veiligheidspositie van webservers en het verzekeren van naleving van de beste praktijken in SSL/TLS-configuraties.

**domainscanner.py**

- Beschrijving: Wordt gebruikt voor het scannen en verzamelen van informatie over domeinen, WHOIS-opzoekingen, subdomein opsomming en DNS-recordanalyse.
- Belang: Een essentiële tool voor verkenning en informatieverzameling, die inzichten biedt in mogelijke aanvalsplan en de algemene veiligheid van een domein.

**dnssec.py**

- Beschrijving: Wordt gebruikt voor het analyseren van de DNSSEC-implementatie van domeinen.
- Belang: Een essentiële tool voor het nakijken of DNSSEC is geimplementeerd zodat gebruikers zekerheid hebben dat de DNS-informatie die ze ontvangen afkomstig is van een legitieme bron en niet is gemanipuleerd onderweg.

**os_detection.py**

- Beschrijving: Wordt gebruikt voor het detecteren van het besturingssysteem van een doelhost.
- Belang: Een essentiële tool voor in de initiële fase van pentesting om latere aanvallen of tests af te stemmen op het specifieke besturingssysteem.

**webscraper.py**

- Beschrijving: Wordt gebruikt voor web scraping.
- Belang: Een essentiële tool voor in de verkenningfase, waardoor waardevolle gegevens uit webbronnen kunnen worden verzameld, wat kan helpen bij verdere aanvallen of het identificeren van kwetsbaarheden.

**http_headers.py**

- Beschrijving: Wordt gebruikt om HTTP-headers te analyseren van webtoepassingen.
- Belang: Een essentiële tool om beveiligingsheaders, configuratiefouten of ontbrekende beveiligingen zoals "Referrer-Policy", "X-Content-Type-Options", "X-XSS-Protection", "Referrer-Policy" en "Content-Security-Policy" te identificeren.

**cve.py**

- Beschrijving: Wordt gebruikt voor het scannen van systemen of applicaties op bekende kwetsbaarheden, met referentie naar de CVE-database.
- Belang: Een essentiële tool voor kwetsbaarheidsbeoordeling en -beheer, waardoor pentesters bekende beveiligingszwakheden in doelsystemen kunnen identificeren.

  - Wat ik eigenlijk wilde bereiken: Ik wilde oorspronkelijk een script maken dat eerst een opgegeven domein scant op alle technologieën en daaruit de versies haalt. Vervolgens wilde ik deze versies opzoeken in een CVE-database met behulp van een API, maar helaas zat ik erg lang vast, dus heb ik gewoon mijn voortgang in het script gelaten.
