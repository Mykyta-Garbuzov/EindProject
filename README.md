# Inleiding 
Voor het eind project heb ik API opgebouwd vanuit FastAPI en uvicorn.SQLite wordt gebruikt voor beheren van database en gegevens. Hashing en OAuth waren voor veiligheidsreden op sommige eindpoints om te tonen dat andere mensen die account hebben, kunnen we geen eindpoint gebruiken. Zoals voor basische project worden containers automatisch opgebouwd via GitHub Action en deployed op Okteto Cloud. Vanuit alle aanvullingen heb ik Front-End aanvulling gekozen. 
Hieronder kunt u alle links naar repositories en websites terugvinden :
*	GitHub : https://github.com/Mykyta-Garbuzov/EindProject
*	Grafana : https://grafana-mykyta-garbuzov.cloud.okteto.net/?orgId=1
*	Prometheus : https://prometheus-mykyta-garbuzov.cloud.okteto.net/graph?g0.expr=&g0.tab=1&g0.stacked=0&g0.show_exemplars=0&g0.range_input=1h
* Netlify : https://eindproject-mykyta-garbuzov.netlify.app/
*	OpenAPI : https://app-mykyta-garbuzov.cloud.okteto.net/docs
# Algemene Eisen
## Main.py
In main.py import we alle libs dat we nodig zullen hebben en daarnaast verwijzen  we ook naar andere files voor het project. 
Na import creëren we een FastApi app instance met korte beschrijving, titel en versie. Verder voegen we “security” en “app.add_middleware” voor CORS zodat front-end met backend kan communiceren. Lijn 33 zal alle database maken als die nog niet bestaan. Lijn 34 wordt gebruikt voor Grafana en Prometheus. De bedoeling is dat die Prometheus alle activiteiten van onze API zouden kunnen aflezen en naar dashboard in Grafana doorsturen. Van de lijn 38 tot en met 42 implementeren we hashing met OAuth protocol zodat mensen die account hebben, kunnen de endpoints gebruiken. 
De volgende lijnen worden niet volledig geopend omdat zij ongeveer gelijkaardig zijn. In het algemeen creëren we functies voor GET, PUT,POST,UPDATE endpoinst bij onze database. Enige waarop we moeten opletten dat sommige functies token hebben die verwijst naar onze OAuth. Deze functies kunnen alleen gebruikt worden als een persoon een account heeft en heeft ingelogd, zal anders persoon geweigerd worden. 
Op het eind run we een developer server op poort 8000 .
![image](https://user-images.githubusercontent.com/71609618/211378447-2842925d-d7ab-47c3-9b92-d6d908a5661e.png)
![image](https://user-images.githubusercontent.com/71609618/211378492-7dc1766d-e357-48b4-8b34-26aa5f173b0c.png)
![image](https://user-images.githubusercontent.com/71609618/211378500-48658c1b-572c-44d1-9427-7c35d12dd790.png)

 
 
 
## Db.py
Bij db.py importeren we benodigde libs. We maken gebruik van SQLite en dat vermelden we na alle imports. Volgende stap is creatie van engine met SessionLocal voor database. declarative_base() zal een klasse retourneren om de Base class te maken en get_db() functie zal gebruikt worden om voor elk verzoek een onafhankelijke database sessie te maken.
 ![image](https://user-images.githubusercontent.com/71609618/211378520-e88ce257-ebf1-4fe8-80b4-6f520524907f.png)

## Auth.py & 
Hier wordt een authenticatie van de gebruiker en control van authenticatie header met juiste token. Auth.py file wordt gebruik voor OAuth en hashing. Het is gelijkaardig aan wat we in de cursus hebben gezien maar het lijkt op de voorbeelden van andere sources hoe basische OAuth en hashing te maken. Enige wat we hebben aangepast, is onze access token en naar welke files het moet verwijzen. 
 ![image](https://user-images.githubusercontent.com/71609618/211378540-9bb9ff7b-ed6a-47b4-9dec-70b6abf27f15.png)

# Docker
## Dockerfile
Deze file blijft ongeveer dezelfde met Dockerfile van Basischeproject . In de file zeggen we dat python moet gebruiken als een base. Op welke port het moet werken, dat alle eisen moet geïnstalleerd worden, welke directories moet gemaakt worden en op het eind CMD zodat developer server zal opgestart worden. 

![image](https://user-images.githubusercontent.com/71609618/211378571-a7fcf447-16a2-4f7b-993c-b92c30628729.png)


## Docker-compose 
Binnen deze file creëren we App, Front-end, Grafana en Prometheus. Extra volumes worden aangemaakt voor database en voor logsgegevens die worden verzameld door Prometheus. We hebben ook netwerk toegevoegd voor meer flexibele en complexe topologie. De hoofdreden ervan zodat App, Grafana en Prometheus elkaar kunnen vinden, anders krijgen we gewoon foutmeldingen tijdens opbouwen van containers.

![image](https://user-images.githubusercontent.com/71609618/211378594-7eb0620d-c099-420c-9fc9-4eee95550e70.png)


![image](https://user-images.githubusercontent.com/71609618/211378607-27e32457-02f4-4580-be18-cb91a62cae67.png)
![image](https://user-images.githubusercontent.com/71609618/211378631-c625b78b-e6bb-40b7-9653-f743175e832d.png)

 
 
## Docker (Vue)
Het is nog een andere Dockerfile dat wordt aangemaakt voor front-end. Het installeert alle benodigde programma’s en files voor vue.js te werken. Apart op de computer moest ik ook node.js installeren. Wanneer we onze hoofd Dockerfile runnen, wordt deze Dockerfile (vue) ook geactiveerd.
 ![image](https://user-images.githubusercontent.com/71609618/211378637-2fe7afca-418c-4757-8fb2-53873ece165b.png)

# Sqlapp
## Models
Binnen deze file gaan we models voor de database tables met de inhoud. We kunnen hier zien dat er drie tables (User,Dogs en Stores) zijn. Zij zijn met elkaar verbonden door Foreign Key en Primary Key.
__repr__ is een hulpmethode om het objecten tijdens runtimes af te drukken. 
 ![image](https://user-images.githubusercontent.com/71609618/211378705-a2102aeb-2e30-4128-b00d-8d9287d502d1.png)

## Repositories
Hier hebben we verschillende functies voor owners, dogs en stores. In plaats van het opnieuw en opnieuw schrijven, maken we gewoon een file waarnaar we elke keer zullen verwijzen om functie op te roepen en gebruiken. 
 ![image](https://user-images.githubusercontent.com/71609618/211378723-101b1286-8175-4dc9-a981-761baf8c918e.png)

## Schemas 
Bij Schemas maken we ItemBase, UserBase en StoreBase models om de gemeenschappelijke kenmerken vast te houden tijdens het lezen of maken van de gegevens. 
 ![image](https://user-images.githubusercontent.com/71609618/211378739-a9982d54-c243-403b-9471-94bbbd6c758f.png)

# Postman
Bij de PostMan kunnen we zien dat we de gegevens van Okteto Cloud afhalen en Posten.
![image](https://user-images.githubusercontent.com/71609618/211378853-f377d2b3-03df-4218-ac0d-bdfd36886385.png)

 ![image](https://user-images.githubusercontent.com/71609618/211378754-6aea35cc-10e2-406e-a9c4-be2c3a16e4d8.png)

Via Get endpoint krijgen we info over dogs en veranderen “Happy” naar “SlaapMode”
 ![image](https://user-images.githubusercontent.com/71609618/211378780-54a6480a-5d2e-4b28-a7f4-70723a9ca822.png)
![image](https://user-images.githubusercontent.com/71609618/211378792-1ab50d1b-0cf4-43c7-b546-2c2f07e21b91.png)

 
En op het eind verwijderen we “Toby” van onze database.
 
 ![image](https://user-images.githubusercontent.com/71609618/211378809-9cf1e6fd-f00c-481c-b4db-19988376549d.png)

# Aanvulling: Front-end
## Endpoints
## Netflify
Mijn front-end wordt gehost op netlify. Er zijn alleen pare files dat ik moet toevoegen aan vue.js zodat het zal werken met netlify. Zij worden gebruikt zodat er geen probleem met CORS zal zijn en zodat index.html echt vue.js zou gebruiken.
  ![image](https://user-images.githubusercontent.com/71609618/211378906-6db0a19b-e9e4-4e78-961b-5a03e8203cf5.png)
![image](https://user-images.githubusercontent.com/71609618/211378916-406253a2-8ab4-4f84-bd28-47366e343f81.png)

 ![image](https://user-images.githubusercontent.com/71609618/211378945-29ad72db-2b98-49ad-acc4-4677dbaafaa2.png)

## Vue
Voor vue.js moeten we node.js installeren en het is eerste ding dat ik moest doen. Na installatie van vue.js zullen we zien dat er veel nieuwe files zijn verschenen maar in de werkelijkheid zullen we alleen werken met index.html en App. Vue

![image](https://user-images.githubusercontent.com/71609618/211378955-5d96d4e3-fb57-44b4-947f-fd519e6057b7.png)

 
### Index.html
In index.html gebruiken we basis html en bootstraap voor de stijl.  Het betekent dat we geen fetch api daar zullen gebruiken. Er is alleen een div met id=”app” die template van App. Vue zal nemen en voor ons op html zal plakken.
![image](https://user-images.githubusercontent.com/71609618/211378992-23678a96-bcc8-477f-a995-1014c0c856ad.png)

 
### App.vue
Binnen template kunnen we zien hoe de aangevraagde gegevens zullen verwerkt worden en getoond op de pagina
  ![image](https://user-images.githubusercontent.com/71609618/211379008-d1518bce-ce99-45e2-baa6-b63ce5874c17.png)

Verder kunnen we zien hoe de gegevens worden aangevraagd via Post en Get . Helaas is het totaal niet gelukt bij om Post te doen met behulp van fetch in vue. Daar heb ik 3-4 dagen gespendeerd en geen echte antwoord gevonden. 
   ![image](https://user-images.githubusercontent.com/71609618/211379040-062d41ad-e742-4c6a-b337-d6c7c4533ae3.png)


# Grafan&Prometheus
Ik heb gewone Grafana gebruikt vanuit het internet omdat Grafana Cloud free trail zou vervallen na 14 dagen en dan zou ik 8 euro per maand moeten betalen. Als een alternatief besloot ik Grafana installeren met Prometheus want ik heb er meer van geleerd hoe zij allebei werken en hoe zij moeten aangepast worden voor mijn eigen eisen.
Voor Grafana heb ik extra Prometheus geïnstalleerd. Prometheus verzamelt de gegevens vanuit onze API en Grafana maakt een dashboards ervan. We hebben al in docker-compose gezien hoe zij met elkaar zijn verbonden maar er zijn nog pare files die we moesten toevoegen zodat het zou werken. 
Prometheus.yml
### Hier vermelden we van welke plaatsen we de logsgegevens willen verzamelen en we kunnen zien dat we de gegevens nemen van onze app en Prometheus zelf.
  ![image](https://user-images.githubusercontent.com/71609618/211379071-56d3e7f9-ee6e-4209-af50-f4282d968377.png)
![image](https://user-images.githubusercontent.com/71609618/211379102-c1b59264-21c4-44f0-8bc1-03e7a6204e45.png)

### Grafana
Om toegang te krijgen tot Grafana moeten we inloggen met “Admin” username en “pass@123” wachtwoord.
  ![image](https://user-images.githubusercontent.com/71609618/211379136-d0e43201-9bd3-45c8-b478-d50273d8b8b0.png)
![image](https://user-images.githubusercontent.com/71609618/211379146-27051837-141d-4c58-abc6-3dcfda38993c.png)


