# Vraag 1
Een pentest, beter genoemd penetratietest, is een test waarbij ethical hackers systemen onderzoeken op kwetsbaarheden om deze dan uiteindelijk aan het licht te brengen.

De fases gaan als volgt:
- **Fase 1 – Intelligence Gathering ( reconnaissance )**
  - Deze fase bestaat uit het verzamelen van zoveel mogelijk informatie uit beschikbare bronnen. ( OSINT ).
 
- **Fase 2 – Intelligence Analysis**
  - Gedurende deze fase wordt de informatie georganiseerd en vastgesteld welke informatie relevant is voor de penetratietest.

- **Fase 3 – Vulnerability Analysis**
  - Nadat alle informatie is verzameld wordt in deze fase gezocht naar kwetsbaarheden in systemen en applicaties.
 
- **Fase 4 – Exploitation**
  - Tijdens de exploitation fase is het doel toegang verkrijgen tot het systeem. De reeds verzamelde informatie wordt gebruikt om op een zorgvuldige wijze aanvallen uit te voeren.
 
- **Fase 5 – Post-Exploitation**
  - In deze fase wordt er vastgesteld wat de waarde is van het gecompromitteerde systeem. Dit is afhankelijk van welke data is gevonden en of deze bruikbaar is om het netwerk verder te compromitteren.

- **Fase 6 – Reporting**
  - Alle bevindingen zullen worden samengebracht in een compleet en helder uitgewerkt rapport.

- **Fase 7 – Re-audit**
  - Op basis van de aanbevelingen kunnen de gevonden kwetsbaarheden door uw eigen organisatie (of externe partij) worden opgelost.
 
# Vraag 2
Ik heb een pentesting toolkit gemaakt met 8 scans dat zowat op alles scant, van portscanners tot CVE scans. Ze hebben allemaal een belang als we over pentesting spreken. (Ik heb dit meer uitgebreid beschreven in mijn READme file van mijn project.)

Mijn pentestingtoolkit richt zich vooral op de "Intelligence Gathering ( reconnaissance )" fase.

Dit omdat Ik scripts heb zoals poortscans, SSL certificaten oplijsten, OS detection, webscraper, http_headers... Deze zijn allemaal scripts om informatie over te winnen van systemen en/of websites om dan te gaan vaststellen of we hiermee onze attackplan kunnen baseren. Bv: Dus ik kan beoordelen over de veiligheid en geldigheid van gevonden certificaten, identificeren van verouderde of kwetsbare configuraties. Bij een webscaper is het dan handig dat er waardevolle gegevens uit webbronnen kunnen worden verzameld, wat kan helpen bij verdere aanvallen of het identificeren van kwetsbaarheden. Bij HTTP headers beveiligingsheaders, configuratiefouten of ontbrekende beveiligingen identificeren. Dus dit sluit goed aan bij de reconnaissance fase.

# Vraag 3

Scapy doet hoofdzakelijk twee dingen: pakketten verzenden en antwoorden ontvangen. Je definieert een set pakketten, verzendt ze, ontvangt antwoorden, vergelijkt verzoeken met antwoorden en retourneert een lijst met pakketkoppelingen (verzoek, antwoord) en een lijst met niet-overeenkomende pakketten. Dit heeft een groot voordeel ten opzichte van tools zoals Nmap of hping. Het antwoord wordt niet beperkt tot “open / gesloten / gefilterd” maar het hele pakket.

**Wanneer je met scapy pakketjes wilt creeren:**

Het mooie van Scapy is de mogelijkheid om elk pakket dat je maar kunt bedenken te creeren. Over het algemeen zal de TCP/IP-stack van uw besturingssysteem een RFC-compatibel pakket maken naar als hacker zouden we vaak een uniek pakket maken dat niet RFC-compatibel is om informatie over een doel te verzamelen. Dus we kunnen daan gewoon een IP-pakket bouwen. Je zoekt dan het pakketattribuut op en kent dit toe bij een variabel bv: x = IP(ttl=64)

**Wanneer je met scapy pakketjes wilt verzenden kan dat aan de hand van deze 2 methodes:**

- Send(): Dit stuurt layer3 paketten
- Sendp(): Dit stuurt layer2 paketten

**Wanneer je met scapy pakketjes wilt onderscheppen ( sniffing ):**

Dat kan met het sniff() commando waarbij je de interface specificeert en ernaar luistert.

**Wanneer je met scapy pakkeetjes wilt analyseren:**

Dat kan je doen via de summary() method waarbij het dan een de layers definieerd van elke pakket.

# Vraag 4

Sockets zijn een essentieel onderdeel van effectieve netwerkcommunicatie, omdat ze het onderliggende concept vormen dat wordt gebruikt om berichten tussen apparaten te verzenden via lokale of mondiale netwerken en verschillende processen op dezelfde machine. Ze bieden een interface op laag niveau die nauwkeurige controle mogelijk maakt over het verkeer dat moet worden verzonden of ontvangen.
Dit lage niveau maakt het mogelijk om zeer performante communicatiekanalen (of aangepaste protocollen) te creëren voor specifieke gebruiksscenario's met lage overhead die aanwezig kunnen zijn in traditionele protocollen, die bovenop socketcommunicatie zijn gebouwd.
Dit maakt sockets uitzonderlijk nuttig in real-time client-server-applicaties die afhankelijk zijn van instant message-uitwisseling of die met enorme hoeveelheden data werken.

**Hoe sockets kunnen worden gebruikt voor zowel client- als server side communicatie:**

Wanneer onze connect() method is voltooid. kunnen de sockets worden gebruikt om een verzoek om de tekst van de pagina in te sturen. Diezelfde socket leest het antwoord en wordt vervolgens vernietigd. Clientsockets worden normaal gesproken slechts voor één uitwisseling (of een kleine reeks opeenvolgende uitwisselingen) gebruikt. 
Ten slotte vertelt het listen() argument om te luisteren aan de socketbibliotheek dat we willen. Als we dit allemaal juist hebben gedaan hebben we nu een “server” socket.

**Beveiligingsaspecten die in acht moeten worden genomen:**

Wanneer u hostnamen in uw toepassing gebruikt, kunnen de geretourneerde adressen letterlijk van alles zijn. Maak geen aannames over een naam als u een beveiligingsgevoelige applicatie heeft. Afhankelijk van uw toepassing en omgeving kan dit al dan niet een probleem voor u zijn.

# Vraag 5

Intigriti is een bedrijf dat een platform aanbiedt voor ethical hackers om deel te nemen aan bug bounty-programma's. Het platform van Intigriti fungeert als een bemiddelaar tussen organisaties die hun systemen willen laten testen op bugs en degenen die bereid zijn deze tests uit te voeren.

**De voordelen/uitdagingen voor organisaties die een bug bounty programma willen launchen is het volgende:**

Intigriti biedt een community aan van ethische hackers die kwetsbaarheden ontdekken en de beveiliging verbeteren. Ze zorgen ervoor dat je in contact komt met de juiste hackers die bij uw wensen passen. Alle reports/bevindingen worden gevalideerd door Intigriti’s deskundige triageteam en wordt beheerd op hun eigen platform. Ze ondersteunen compliance eisen en zijn ISO 27001 en SOC 2 gecertificeerd. Een uitdaging is dat bedrijven niet zoveel geld willen besteden of dat ze simpelweg de bounty hunters niet vertrouwen omdat zij niet een background check kunnen doen omdat ze worden aangenomen door intigriti zelf.

**De voordelen/uitdagingen voor individuele onderzoekers die een mee willen deelnemen aan een bug bounty programma het volgende:**

Bedrijven zullen u belonen (met geld) als u hen waarschuwt voor exploiteerbare beveiligingsfouten. Je kan je skills developen door af en toe eens deel te nemen en dit zal ook goed op u CV staan. Je kan netwerken opbouwen en zo nog groter gaan. Een uitdaging kan zijn dat wanneer je niets heb kunnen vinden krijg je geen geldbeloning en “takes a toll on your mental” en kan je demotiveren. 
















