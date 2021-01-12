# Persoonlijk portfolio
Minor Applied data science
door Niels van Schaik 18150845

## Index
1) Globale toevoeging
2) Korte introductie project
3) Scrum
4) Procentuele toeviging team
5) Team communicatie
6) Modellen en mijn toevoeging
7) Load_Data.py
8) Peak detection code
9) Mean day/week code
10) Toevoeging Paper
11) Afsluiting

## 1. Globale toevoeging
1) Verschijdene Trello kaartje opgenomen en afgerond.
2) Univerzele code geschreven om data van specifieke huizen en tebellen in te laden zodat dit bruikbaar is voor de modellen.
3) De Is_Peak functie geschreven dat een formule toepast op energy verbruik toepast om pieken te detecteren.
4) Code om het gemiddelde dag en week verbruik te berekenen in een moving window.
5) Ik was backup scrum master en omdat ik al ervaring had met scrum zorgde ik voor hulp tijdens de meetings en feedback voor de huidige scrum master, Jefry el Bhwash 16095065
6) Heb deel genomen aan verschillende modellen als driver en navigator rol.

### Datacamp
Datacamp Courses ![Minor_DataCamp_Courses](Minor_DataCamp_Courses.png)

## 2. Korte introductie Project
Het doel van dit onderzoek is om voor factory zero uit te zoeken welke prediction models het beste werken om energy verbruik en opbrengst een dag vooruit te voorspellen
met een resolutie van een uur.
Voor ons waren er ook projecten geweest deze zijn te vinden in de reports in de repository:

![Report_Jan](Factory_Zero_January_2020_Report.pdf) and ![Report_Juni](Factory_Zero_June_2020_Report.pdf)

onze onderzoeks vraag was:
*What is a suitable machine learning model to predict energy use & production of a “zero at the meter” residential house, one day in advance with (if possible) hourly resolution?*

## 3. Scrum
Onze scrum master was Jefry el Bhwash 16095065 en ik was de backup scrum master als Jefry afwezig was
We hebben trello gebruikt als scrum board en dit zijn de kaartjes waar ik aan heb gewerkt. ![Trello kaartjes](Trello kaartjes.zip)
Deze screenshots waren genomen voor de deadline van de paper voor het actuele trello bord is hier een link: https://trello.com/b/kDceuyG7
Alleen week 16 word nog geupdate op he moment dat ik dit schrijf.

## 4. Procentuele toevoeging van het team
Ik heb mijn collegas onder verdeeld in delen dat zij hebben geleverd aan dit project in %
Niels van Drunen (18062814): 24%

Levi Duivenvoorden (18005152): 24%

Jefry el Bhwash (16095065): 24%

Niels van Schaik (18150845) :23%

Amin Mansouri (18097367): 5%


Voor uitleg zie volgend hoofdstuk

## 5. Team communicatie
Ondanks dat ik een week later begon met deze minor werd ik goed ontvangen door iedereen in het team en werd het al snel duidelijk dat het een prettig project zou gaan worden.
Tussen mij Jefry, Niels en Levi was de communicatie open eerlijk en concreet. Feedback werd seerieus genomen en het was prettig werken tussen ons 4.
Echter kan ik niet hetzelfde zeggen over Amin, hij was vaak afwezig en als hij aanwezig was zat hij gedempt in de meeting en voegde weinig toe aan het gesprek.
Ook was hij niet open en duidelijk over de taken die hij op zich nam of werden aangewezen. Deze taken waren vaak niet optijd af en vroeg hij niet of te laat om hulp.
Dit leide tot wat gesprekenne met Mevrouw G.E. in 't Veld waarna hij zij dat ie meer open zou communiceren en zijn taken optijd zou volbrengen of anders optijd om hulp vragen.
Hier heb ik persoonlijk weinig verbetering in gezien.
De rest van de groep hebben hier omheen gewerkt en hebben we met hem de afspraak gemaakt dat als we merken dat het niet af kwam wij de taak over nemen.
Dit hebben we gedaan zodat we hem de kans konden geven om mee toe doen met het onderzoek en dat hij de kans heeft om dingen te doen zodat hij belangrijke dingen in zijn portfolio kon stoppen zonder dat wij hem in de weg stonden.

## 6. Modellen en mijn toevoegingen
Levi Duivenvoorden was de persoon die vooral de modellen in elkaar heeft gezet en getraind. Hierbij heb ik vaak als navigator rol gespeeld om hem hierbij te ondersteunen(Zie week 14 trello).
Echter waren mijn grootste toevoegingen in het verbeteren van de modellen. De classes en binnen werking waren al voor ons gemaakt en levi heeft deze geimplementeerd.
We hebben vooral gewerkt aan on hot encoden en features toevoegen om het model te verbeteren.
De 3 grootste toevoegingen aan mij zijn te zien in hoofdstuk 7, 8 en 9.
Zoals te zien in trello ben ik ook vaak navigator geweest bij verschillende toevoegingen aan de modellen zodat ik mijn achtergrond als software engeneer breed kon sprijden ipv alle taken op me nemen.

## 7. Load_Data.py
Load_Data.py is code dat ik heb geschreven om data dat in numpy bestanden opgeslagen waren op de serven in te laden en dit om te zetten in bruikbare data voor modellen en andere doel einde zoals plottjes.
Deze code was makkelijk te importeren en begrijpen en heeft ons als groep tijd bespaard omdat we makkelijk specifieke huizen en tabbelen konden inladen zonder opzoek te gaan naar complexe code en het op die manier in te laden.
Ik heb comments gezet in het bestand met uitleg erin over de functies die ik heb gebouwd. ![Load_data](Load_data.py) 

## 8. Peak detection code
Tijdens het maken van de LSTM wouden we proberen of een feature dat aangaf of de data een piek was verbeteringing gaf aan het model. Deze taak heb ik op me genomen.
Om dit voor elkaar te krijgen heb ik een formule geschreven dat gebruik maakt van het gemiddelde en standaart deviatie binnen een moving window.
Deze formule gaf de treshold aan en als de energy daar over heen ging was het een piek.
De notebook met de code: ![Is_peak](Is_peak_code.pdf) 

En een bijbehorend plottje:

![Is_peak plotje](Is_peak.png) 

## 9. Mean day/week code
We hadden een feature toe gevoegd dat binnen de window het gemiddelde van de dag en van de week aangaf
Dit is de code dat daar uit kwam: ![dag en week gemiddelde](day-week-Mean.py) 

## 10. Toevoeging Paper
Ondanks dat het nog niet is afgerond tijdens het schrijven van mijn portfolio zijn dit mijn toevoegingen aan de paper.
Hoofdstuk 2.1.2 en 5
Ook heb ik net zoals de rest van mijn groep het document nagekeken en verbeterd.
Ik heb ook de taak op me genomen om alle tabellen en grafieken te verbeteren waar nodig en ervoor zorgen dat ze alles hebben dat ze moeten hebben zoals een titel.

## 11. Afsluiting
Persoonlijk vond ik dit een heel interesant onderzoek. Ik had voor deze minor veel intresse in wat AI kon doen en had veel plezier in het maken van deze modellen.
Ook met corona had ik een team gevoel en waren de lessen goed opgezet en makkelijk te volgen.
Toch zijn er dingen die ik persoonlijk beter zou willen doen.
Als er meer projecten komen ga ik vaker mijn camera aan zetten om een meer menselijk element toe te voegen en team verband te stimuleren.
Ik moet een proffescionelere houding aan nemen tijdens meetings met leeraren en problem/ project owners. Tijdens dit project heb ik en ons team te weinig aan gedaan en valt er veel in te verbeteren.
Ik vind dat ik meer had kunnen doen tijdens dit project met een meer active houding.

Bedankt voor het lezen van mijn portfolio en veel succes met het beoordelen van mijn en toekomstige portfolios.
Niels van Schaik
18150845
