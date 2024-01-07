## Les 1: Python en security - intro

**portscanner.py**

- Beschrijving: Zoals de naam suggereert, wordt het gebruikt voor het scannen van netwerkpoorten op een doelhost. Het identificeert open poorten en mogelijk actieve diensten.
- Belang: Een basale maar essentiële tool voor netwerkbeveiligingsbeoordelingen, helpt bij het identificeren van potentiële toegangspunten voor aanvallen.

**certretriever.py**

- Beschrijving: Dit script is ontworpen om SSL/TLS-certificaten van servers op te halen. Het is cruciaal in een pentesting toolkit voor het beoordelen van de veiligheid van deze certificaten, het identificeren van verouderde of kwetsbare configuraties, en het garanderen dat communicatiekanalen veilig versleuteld zijn.
- Belang: Essentieel voor het evalueren van de veiligheidspositie van webservers en het verzekeren van naleving van de beste praktijken in SSL/TLS-configuraties.

**domainscanner.py**

- Beschrijving: Deze script wordt gebruikt voor het scannen en verzamelen van informatie over domeinen. Dit kan functies omvatten zoals WHOIS-opzoekingen, subdomein opsomming en DNS-recordanalyse.
- Belang: Belangrijk voor verkenning en informatieverzameling, die inzichten biedt in mogelijke aanvalsvectoren en de veiligheidspositie van een domein.

**dnssec.py**

- Beschrijving: Richt zich op DNS Security Extensions (DNSSEC). Het kan worden gebruikt voor het analyseren van de DNSSEC-implementatie van domeinen, op zoek naar configuratiefouten of zwakheden
- Belang:  Cruciaal voor het waarborgen van de integriteit en authenticiteit van DNS-gegevens, wat een veelvoorkomende aanvalsvector is in cybersecurity.

**os_detection.py**

- Beschrijving: Dit script houdt zich bezig met het detecteren van het besturingssysteem van een doelhost. Het kan technieken gebruiken zoals TCP/IP-stack-fingerprinting.
- Belang: Fundamenteel in de initiële fase van pentesting om latere aanvallen of tests af te stemmen op het specifieke besturingssysteem.

**webscraper.py**

- Beschrijving: Deze klasse is ontworpen voor web scraping. In de context van pentesting kan het worden gebruikt om informatie van webpagina's te verzamelen, wat kan helpen bij verdere aanvallen of het identificeren van kwetsbaarheden.
- Belang: Nuttig in de verkenningfase, waardoor waardevolle gegevens uit webbronnen kunnen worden verzameld.

**http_headers.py**

- Beschrijving: Deze klasse analyseert HTTP-headers van webtoepassingen. Het kan beveiligingsheaders identificeren, configuratiefouten of ontbrekende beveiligingen zoals CSP, X-Frame-Options, enz.
- Belang: Kritisch voor beveiligingsbeoordelingen van webapplicaties, om robuustheid te garanderen tegen verschillende webgebaseerde aanvallen.

**cve.py**

- Beschrijving: Deze klasse behandelt het Common Vulnerabilities and Exposures (CVE) systeem. Het kan worden gebruikt voor het scannen van systemen of applicaties op bekende kwetsbaarheden, met referentie naar de CVE-database.
- Belang: Onmisbaar voor kwetsbaarheidsbeoordeling en -beheer, waardoor pentesters bekende beveiligingszwakheden in doelsystemen kunnen identificeren.
