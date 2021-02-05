# Persoonlijk portfolio
Minor Applied data science
door Niels van Schaik 18150845

## Index
1) Globale toevoeging
2) Het Project
3) Scrum
4) Leerdoelen
5) Modellen en mijn toevoeging
6) Load_Data.py
7) Peak detection code
8) Mean day/week code
9) Toevoeging Paper
10) Feedback
11) Presentaties
12) Afsluiting

## 1. Globale toevoeging
1) Verschijdene Trello kaartje opgenomen en afgerond.
2) Univerzele code geschreven om data van specifieke huizen en tebellen in te laden zodat dit bruikbaar is voor de modellen.
3) De Is_Peak functie geschreven dat een formule toepast op energy verbruik toepast om pieken te detecteren.
4) Code om het gemiddelde dag en week verbruik te berekenen in een moving window.
5) Ik was backup scrum master en omdat ik al ervaring had met scrum zorgde ik voor hulp tijdens de meetings en feedback voor de huidige scrum master, Jefry el Bhwash 16095065
6) Heb deel genomen aan verschillende modellen als driver en navigator rol.
7) Verschillende presentaties gehouden.

### 1.1 Datacamp
Datacamp Courses ![Minor_DataCamp_Courses](Minor_DataCamp_Courses.png)

## 2. Het Project
Ons onderzoeks vraag luide als volgt: What is a suitable machine learning model to predict energy use & production of a “zero at the meter” residential house, one day in advance with (if possible) hourly resolution?

Dit houd in dat we op zoek zijn gegaan naar een machine learning model dat het beste energy opbrengst en verbruik 24 uur kan voorspellen voor specifieke "nul op de meter huizen" met een rezolutie van een uur. 
Voor ons waren er ook projecten geweest deze zijn te vinden in de reports in de repository:

![Report_Jan](Factory_Zero_January_2020_Report.pdf) and ![Report_Juni](Factory_Zero_June_2020_Report.pdf)
De belangrijkste informatie die we hieruit hebben gehaald is de formule voor het berekenen van het energy verbruik van een van de huizen van Factory Zero.

Energy Consumption = Smart_in + Solar_out − Smart_out

1) Smart_in: Energie dat het huis binnen komt vanaf het energie netwerk
2) Solar_out: Energie dat is opgewekt door de zonnepanelen van het huis.
3) Smart_out: Energie dat is verkocht aan het energie netwerk.

Factory zero is opzoek naar een model die energy opbrengst en verbruik kan voorspellen voor hun huizen omdat de manier waarop energy word verkocht naar energy maatschappijen gaat veranderen.
Een korte samenvatting van de veranderingen die wellicht komen: Als je energy verkoopt op momenten dat het energy netwerk overbelast raakt moet je betalen voor de terrug gevoerde energy in plaats van dat je er geld voor krijgt. Deze prijzen veranderen per uur.
Om te voorkomen dat de NZEB (Net Zero Emmision Buildings) een energy rekening krijgen door deze veranderingen wilt Factory Zero een model dat voorspelt Wanneer het beste moment is om energy te kopen en verkopen.
De eerste stap om dit te berijken was om een voorspelings model te maken voor energy opbrengst en gebruik. Deze taak is aan Team Zero gegeven.
Om dit te berijken zijn we een onderzoek gestart dat bepaald welk machine learning model het beste was om te gebruiken voor dit doel einde.

Voor dit onderzoek hebben we een ![Literatuur_Onderzoek](literaturePapersWeek5.xlsx) gedaan en een ![Onderzoeksplan](Onderzoeksplan.pdf) opgesteld.
(voor meer informatie over de planning van dit onderzoek wil ik u verweizen naar het onderzoeks plan)
Dit is de lijst aan artiekelen die we uit dit onderzoek hebben gehaald:
1) Predicting energy consumption: A multiple decomposition-ensemble approach
2) Forecasting Energy Consumption of a House using Radial Basis Function Network
3) Predicting Energy Consumption of a House using Neural Network
4) A granular deep learning approach for predicting energy consumption
5) Machine Learning-Based Approach to Predict Energy Consumption of Renewable and Nonrenewable Power Sources

Met de kennis die we hebben vergaard van de literatuur en de reports van Factory Zero hebben we de volgende modellen geimplementeerd:
1) MVLR (Multi Variate Linear Regression)
2) SVR (Support Vector Regression)
3) LSTM (Long Short-Term Memory)
4) MLP (Multi-Layer Perceptron)

De resultaten van deze modellen zijn te vinden op pagina 7 va onze ![paper](Paper_v04.docx) die we hebben ingeleverd.

De conlusie die we uit de resultaten hebben kunnen halen is dat LSTM de beste voorspellingen maakte binnen onze use case voor energy opbrengst en gebruik.
Echter kan er meer geëxperimenteerd worden om een beter resultaat te kunnen behalen.
Zoals 2 simpele modelen maken, 1 om de pieken te voor spellen en 1 om de energy te voorspellen zonder de pieken, en dan deze 2 modelen samen te voegen om een beter model te maken.

Om op deze conclusie te komen hebben we de data gebruikt die Factory Zero ons heeft gegeven.
Deze data bestond uit 120 excel sheets, een voor elk huis, met daarin verschillende tabellen voor de verschillende sensoren.
Deze data bestond uit een timestamp in seconden en daar aan vast de data die de sensor gemeten had.
De huizen zelf stonden in een wijk in Zoetermeer en de data ging van jan 2019 t/m dec 2019.
We hebben deze data door gespit voor bruikbare data dat we konden gebruiken voor het onderzoek.
Hiervoor hebben we verschillende visualisaties gemaakt zoals deze heat map die Niels van Drunen heeft gemaakt:
![Heatmap](Heatmap_production.png) 
Hier is ook een overzicht van het energy opbrengst en gebruik per huis van het hele jaar (hij is redelijk groot):
![energy_van_een_jaar](EnergyUse&Prod_OneYear_AllHouses.png)
of mijn visualisatie van de pieken in hoofdstuk Peak detection code.

Ook heeft onze problem owner (Mnr. Rahola) ons begelijd in de eerste paar weken door ons visualisaties te maken van veel delen van de data die ons gegeven is.
Een goed voorbeeld hiervan was het visualiseren van de energie verbruik van de huizen om te kijken of ze ook echt NZEB waren.
Tijdens het verkennen van de data zijn we verschillende problemen tegen gekomen.

De Timestamps waren niet altijd 5 minuten uit elkaar en weken per sensor soms af.
Deze time stamps zouden allemaal gelijk moeten zijn om te voorkomen dat we de verkerde data punten bij elkaar zetten van verschillende sensors.
Hier zijn we niet 100% omheen gekomen maar we hebben het minder relevant gemaakt door het te resampelen en huizen te gebruiken waar dit het minst voorkomen.

In de data zaten vaak gaten die zelfs konde oplopen tot uren of dagen.
Hierbij is er dan of geen data of word de laatste meeting opnieuw meegegeven.
Dit heeft ons geforseerd om de beste huizen te zoeken, dit is ons gelukt door de heatmap hierboven.

Voor meer informatie en detail van de data cleaning/preperation verweis ik u door naar pagina 2 en 3 van de ![paper](Paper_v04.docx) .

## 3. Scrum
Onze scrum master was Jefry el Bhwash 16095065 en ik was de backup scrum master als Jefry afwezig was
We hebben trello gebruikt als scrum board en dit zijn de kaartjes waar ik aan heb gewerkt. ![Trello kaartjes](TrelloKaartjes.zip) 
Deze screenshots waren genomen voor de deadline van de paper voor het actuele trello bord is hier een link: https://trello.com/b/kDceuyG7
Alleen week 16 word nog geupdate op he moment dat ik dit schrijf.

## 4. Leerdoelen
Voor dit project heb ik een aantal leerdoelen voor mezelf opgezet:
1) Door te leren over applied data science wil ik mijn SE (Software Engeneer) kennis vergroten voor een breeder portfolio. Ik wil daarom leren wat machine learning modellen zijn, waar ze voor gebruikt kunnen worden en hoe ze werken.
2) Ervaring in scrum is erg belangrijk voor een SE. Daarom wil ik dit project het scrum bord strak bijhouden.
3) Proffecioneel omgaan met de project/problem owner is een belangrijke skill voor een SE. Dit wil dit project verbeteren.

## 5. Modellen en mijn toevoegingen
Ik heb gewerkt aan verschillende modellen als navigator of ik heb onderdelen van de feature set gemaakt of bij gedragen als navigator voor deze features.
Het model waar ik aan gewerkt heb is een verbetering van de LSTM in week 14. ![LSTM](W14_LSTM_Improvements.pdf) 
Dit is de lijst aan features waar ik aan heb gewerkt of aan heb geholpen:
1) Is_peak ![Is_peak](Is_peak_code.pdf) (zie hoofdstuk 7)
2) Mean day/week ![dag en week gemiddelde](day-week-Mean.py) (zie hoofdstuk 8)
3) geschaalde collomen voor energy productie en gebruik

Mijn andere bijdragen bestaan vooral uit navigator rol zijn voor verschillende onderdelen van mijn project genoten.
Dit heb ik gedaan zodat ik mijn kennis over programmeren kon versprijden over het team ipv alles zelf doen.
In mijn mening heeft dit voor een soepeler proces gezorgd tijdens het maken van de modellen en generale fouten verbeteren in de code die werd geschreven.
Deze bijdragen zijn te zien in de trello kaartjes. ![Trello kaartjes](TrelloKaartjes.zip) 

## 6. Load_Data.py
Load_Data.py is code dat ik heb geschreven om data dat in numpy bestanden opgeslagen waren op de serven in te laden en dit om te zetten in bruikbare data voor modellen en andere doel einde zoals plottjes.
Deze code was makkelijk te importeren en begrijpen en heeft ons als groep tijd bespaard omdat we makkelijk specifieke huizen en tabbelen konden inladen zonder opzoek te gaan naar complexe code en het op die manier in te laden.
Ik heb comments gezet in het bestand met uitleg erin over de functies die ik heb gebouwd. ![Load_data](Load_data.py) 

## 7. Peak detection code
Tijdens het maken van de LSTM wouden we proberen of een feature dat aangaf of de data een piek was verbeteringing gaf aan het model. Deze taak heb ik op me genomen.
Om dit voor elkaar te krijgen heb ik een formule geschreven dat gebruik maakt van het gemiddelde en standaart deviatie binnen een moving window.
Deze formule gaf de treshold aan en als de energy daar over heen ging was het een piek.
Na een lange tijd spelen met de formulen ben ik tevreden met het resultaat die het levert en hebben we het geimplementeerd in de feature set.
De notebook met de code: ![Is_peak](Is_peak_code.pdf) 

En een bijbehorend plottje:

![Is_peak plotje](Is_peak.png) 

## 8. Mean day/week code
Er was een feature nodig dat binnen de window het gemiddelde van de dag en van de week kon berekenen en dit terrug gaf aan het model.
Omdat dit een gemiddelde binnen een window was zorgde dit ervoor dat de eerste week aan data geen accurate gemiddelde berekend kon worden.
Dit is de code dat daar uit kwam: ![dag en week gemiddelde](day-week-Mean.py) 

## 9. Toevoeging Paper
Ondanks dat het nog niet is afgerond tijdens het schrijven van mijn portfolio zijn dit mijn toevoegingen aan de paper.
Hoofdstuk 2.1.2 en 5
Ook heb ik net zoals de rest van mijn groep het document nagekeken en verbeterd.
Ik heb ook de taak op me genomen om alle tabellen en grafieken te verbeteren waar nodig en ervoor zorgen dat ze alles hebben dat ze moeten hebben zoals een titel.

## 10. Feedback
In dit hoofdstuk ga ik feedback geven op mijn team, mijn bijdragen aan dit project en aan de leerdoelen die ik heb opgesteld in hoofdstuk 4.

### 10.1 Team Reflectie
Ik heb mijn collegas onder verdeeld in delen dat zij hebben geleverd aan dit project in %

Niels van Drunen (18062814): 24%

Levi Duivenvoorden (18005152): 24%

Jefry el Bhwash (16095065): 24%

Niels van Schaik (18150845) :23%

Amin Mansouri (18097367): 5%


Ondanks dat ik een week later begon met deze minor werd ik goed ontvangen door iedereen in het team en werd het al snel duidelijk dat het een prettig project zou gaan worden.
Tussen mij Jefry, Niels en Levi was de communicatie open eerlijk en concreet. Feedback werd seerieus genomen en het was prettig werken tussen ons 4.
Echter kan ik niet hetzelfde zeggen over Amin, hij was vaak afwezig en als hij aanwezig was zat hij gedempt in de meeting en voegde weinig toe aan het gesprek.
Ook was hij niet open en duidelijk over de taken die hij op zich nam of werden aangewezen. Deze taken waren vaak niet optijd af en vroeg hij niet of te laat om hulp.
Dit leide tot wat gesprekenne met Mevrouw G.E. in 't Veld waarna hij zij dat ie meer open zou communiceren en zijn taken optijd zou volbrengen of anders optijd om hulp vragen.
Hier heb ik persoonlijk weinig verbetering in gezien.
De rest van de groep hebben hier omheen gewerkt en hebben we met hem de afspraak gemaakt dat als we merken dat het niet af kwam wij de taak over nemen.
Dit hebben we gedaan zodat we hem de kans konden geven om mee toe doen met het onderzoek en dat hij de kans heeft om dingen te doen zodat hij belangrijke dingen in zijn portfolio kon stoppen zonder dat wij hem in de weg stonden.

### 10.2 Reflectie leerdoelen
1.  Kennis over Machine learning verbreden. 7/10

Dit leerdoel heb ik goed volbracht door middel van de lesstof en mijn bijdrage aan de modellen die we voor ons onderzoek hebben gemaakt.
Ik heb ervaring op gedaan met de stof en heb persoonlijk gezien wat de moddelen kunnen doen en hoe je ze moet maken.

2. Ervaring met Scrum. 6/10

Tijdens dit project hebben we volledig gebruik gemaakt van scrum. Ik heb daarom meer ervaring op gedaan met scrum.
De reden waarom ik dit alleen een 6 geef is omdat ik zelf niet het scrumbord strak genoeg heb bijgehouden voor dit leerdoel.

3. Proffecionele omgang met de problem/project owner. 5/10

Dit leerdoel heb ik niet voldoende afgerond. Dit komt omdat ik pas halverwege de minor hier op ben gaan letten. Hierdoor kan ik mezelf geen voldoende geven voor dit leerdoel.
Ik ga het alleen geen lager cijfer geven omdat ik wel een meeting heb ondernomen om punten uit te leggen aan mijn team zodat we dit wel goed konden doen. Na deze meeting heb ik een verbetering gezien in proffecionaliteit en een effecientere omgang met de tijd die we hadden met onze problem/project owner.

### 10.3 Reflectie bijdrage
Zoals te zien in de team reflectie heb ik mijzelf minder procentuele bijdrage geven dan andere collegas. Dit komt omdat ik ondanks ik veel heb geholpen met de code van mijn collegas, ik minder taken persoonlijk op me heb genomen.
Dit zou ook zijn gebeurt omdat ik bewust ervoor heb gekozen om mijn kennis over proggrammeren te sprijden over het team, echter denk ik ondanks dit feit nogsteeds dat ik meer taken persoonlijk op me had kunnen nemen binnen dit project.
Als ik dit project opnieuw zou doen zal ik nogsteeds proberen om mijn kennis over het team te sprijden. Maar dit wel met een focus op meer taken zelf op me te nemen.

## 11. Presentaties
Ook tijdens dit project heb ik verschillende presentaties online gepresenteerd:
1) Weekelijkse presentatie week 3:  ![presentatie_Week3](PresentatieWeek3.pptx) 
2) Weekelijkse presentatie week 8:  ![presentatie_Week8](PresentatieWeek8.pptx) 
3) Weekelijkse presentatie week 14: ![presentatie_Week14](PresentatieWeek14.pptx) 

## 12. Afsluiting
Persoonlijk vond ik dit een heel interesant onderzoek. Ik had voor deze minor veel intresse in wat AI kon doen en had veel plezier in het maken van deze modellen.
Ook met corona had ik een team gevoel en waren de lessen goed opgezet en makkelijk te volgen.

Bedankt voor het lezen van mijn portfolio en veel succes met het beoordelen van mijn en toekomstige portfolios.
Niels van Schaik
18150845
