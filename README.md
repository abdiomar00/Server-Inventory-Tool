# Server Inventory Tool

## 1. Introduktion

Server Inventory Tool är ett Python-program som används för att hantera, organisera och övervaka servrar i olika miljöer.

Syftet med programmet är att göra det enklare för en administratör att hålla reda på sina servrar och kontrollera om de är tillgängliga via nätverket.

Programmet kan registrera nya servrar, visa befintliga servrar, filtrera servrar efter miljö, ta bort servrar, kontrollera serverstatus och exportera information till CSV-filer.

All serverinformation sparas i en JSON-fil. Det innebär att informationen finns kvar även när programmet avslutas.

Projektet är utvecklat i Python och uppdelat i flera moduler för att göra koden strukturerad, lättläst och enkel att underhålla.

## 2. Programmets syfte och funktioner

Programmet har följande funktioner:

### 2.1 Hantera servrar

Användaren kan:

- Lägga till nya servrar.
- Visa alla registrerade servrar.
- Filtrera servrar efter miljö.
- Söka efter servrar.
- Ta bort servrar från inventeringen.

Varje server innehåller information om namn, adress, miljö, roll, status och senaste kontrolltid.

### 2.2 Övervaka servrar

Programmet använder Linux-kommandot `ping` för att kontrollera om en server är tillgänglig via nätverket.

Det finns två alternativ:

- Kontrollera en specifik server.
- Kontrollera alla registrerade servrar.

Efter kontrollen uppdateras serverns status och tidpunkten för den senaste kontrollen.

Serverstatus kan exempelvis vara:

- `unknown`: Servern har ännu inte kontrollerats.
- `online`: Servern svarade på ping.
- `offline`: Servern svarade inte på ping.

### 2.3 Exportera rapporter

Användaren kan exportera serverinformationen till CSV-format.

Programmet skapar automatiskt en mapp med namnet `reports`.

Rapportfilen får ett filnamn som innehåller datum och tid, exempelvis:

`inventory_2026-11-12_1030.csv`

## 3. Systemkrav

Programmet använder standardbibliotek från Python, bland annat:

- `json` för att läsa och spara serverinformation.
- `csv` för att skapa rapporter.
- `subprocess` för att köra ping-kommandot.
- `argparse` för att hantera kommandoradsargument.
- `os` för att hantera miljövariabler och sökvägar.
- `datetime` för att registrera datum och tid.

### 4 Kontrollera projektets filer

Projektet ska innehålla följande filer:

server-inventory-tool/
│
├── main.py
├── meny.py
├── lagring.py
├── kontroller.py
├── servers.json
├── reports/
├── .gitignore
└── README.md

Mappen `reports` skapas automatiskt när en CSV-rapport exporteras om den inte redan finns.

## 5. Projektets uppbyggnad och moduler

Projektet är uppdelat i flera moduler. Varje modul har ett eget ansvarsområde. Detta gör att programmet blir mer organiserat och att samma kod inte behöver skrivas flera gånger.

### 5.1 main.py

`main.py` är programmets huvudfil och startpunkt.

Den ansvarar för att:

- Starta programmet.
- Läsa kommandoradsargument med `argparse`.
- Ladda in serverinformationen.
- Avgöra vilket kommando användaren har valt.
- Anropa funktioner från övriga moduler.
- Hantera programmets avslutningskoder.

Filen innehåller även:

if __name__ == "__main__":
    main()

Detta gör att huvudfunktionen körs när filen startas direkt.

### 5.2 meny.py

`meny.py` hanterar programmets interaktiva meny.

Den ansvarar för att:

- Visa menyalternativ.
- Ta emot användarens val.
- Låta användaren lägga till servrar.
- Visa och filtrera serverinformation.
- Ta bort servrar.
- Kontrollera att användarens inmatning är giltig.

Miljöerna som kan användas är `dev`, `test` och `prod`.

Om användaren försöker ta bort en produktionsserver krävs en extra bekräftelse.

### 5.3 lagring.py

`lagring.py` ansvarar för programmets datalagring.

Den innehåller funktioner för att:

- Läsa in serverinformation från JSON.
- Spara ändringar i JSON-filen.
- Hantera sökvägen till datafilen.
- Exportera serverinformation till CSV.
- Skapa rapportmappen automatiskt.

JSON används eftersom formatet är enkelt att läsa, skriva och hantera med Python.

### 5.4 kontroller.py

`kontroller.py` ansvarar för att kontrollera om servrar är tillgängliga.

Modulen använder:

subprocess.run()

för att köra Linux-kommandot:

ping -c 1 SERVER_ADDRESS

Flaggan `-c 1` innebär att ett ping-paket skickas.

Programmet använder kommandots returvärde för att avgöra om servern svarade.

- Returvärde `0`: Servern är tillgänglig.
- Annat returvärde: Servern betraktas som otillgänglig.

## 6. Datalagring med JSON

Serverinformationen sparas i filen `servers.json`.

Varje server innehåller följande fält:

| Fält | Beskrivning |
|---|---|
| `namn` | Serverns namn |
| `adress` | Serverns IP-adress eller värdnamn |
| `miljo` | Serverns miljö |
| `roll` | Serverns funktion |
| `status` | Serverns aktuella status |
| `senast_kontrollerad` | Tidpunkten för senaste kontroll |

Exempel på serverinformation:

[
    {
        "namn": "web01",
        "adress": "192.168.1.10",
        "miljo": "prod",
        "roll": "web server",
        "status": "unknown",
        "senast_kontrollerad": null
    }
]

Om JSON-filen inte finns när programmet startas ska programmet börja med en tom serverlista.

När användaren lägger till, ändrar eller tar bort information sparas ändringarna i JSON-filen.

## 7. Miljövariabel – INVENTORY_DATAFIL

Programmet använder miljövariabeln `INVENTORY_DATAFIL` för att bestämma vilken JSON-fil som ska användas för att lagra serverinformationen.

Om miljövariabeln inte är angiven används standardfilen:

`servers.json`

## 7. Starta programmet – interaktivt läge

Programmet har två olika körlägen.

Det första är det interaktiva läget. Det används när programmet startas utan kommandoradsargument.

Starta programmet med:

python3 main.py

Programmet visar då en meny där användaren kan välja mellan olika alternativ.

Exempel på menyalternativ:

1. Visa alla servrar.
2. Filtrera servrar efter miljö.
3. Lägg till en server.
4. Ta bort en server.
5. Kontrollera en server.
6. Kontrollera alla servrar.
7. Exportera CSV-rapport.
8. Avsluta programmet.

Användaren väljer ett alternativ genom att skriva motsvarande nummer.

Menyn fortsätter att visas tills användaren väljer att avsluta programmet.

## 8. Validering och felhantering

Programmet innehåller olika kontroller för att förhindra felaktig information och felaktig användning.

### 8.1 Kontroll av miljö

När en ny server läggs till måste användaren välja en giltig miljö:

- `dev`
- `test`
- `prod`

Om användaren anger ett ogiltigt värde får användaren försöka igen.

### 8.2 Dubbla servernamn

Programmet tillåter inte att två servrar registreras med samma namn.

Detta förhindrar att servrar blandas ihop när de ska kontrolleras eller tas bort.

### 8.3 Skydd för produktionsservrar

Innan en server i miljön `prod` tas bort måste användaren bekräfta borttagningen en extra gång.

Det minskar risken för att en viktig produktionsserver tas bort av misstag.

### 8.4 Saknad JSON-fil

Om JSON-filen saknas startar programmet med en tom lista i stället för att avslutas med ett fel.

### 8.5 Server som inte hittas

Om användaren försöker kontrollera en server som inte finns registrerad visas ett felmeddelande.

## 9. Avslutningskoder

Programmet använder avslutningskoder för att visa om en operation lyckades.

| Avslutningskod | Betydelse |
|---|---|
| `0` | Operationen lyckades |
| `1` | Servern hittades inte eller en eller flera serverkontroller misslyckades |

Detta gör det möjligt att använda programmet i automatiserade skript och andra DevOps-processer.

## 10. CSV-export och rapporthantering

CSV-exporten gör det möjligt att spara serverinventeringen i ett format som kan användas i andra program.

När exportfunktionen körs:

1. Programmet hämtar serverinformationen.
2. Kontrollerar om mappen `reports` finns.
3. Skapar mappen om den saknas.
4. Skapar ett filnamn med datum och tid.
5. Skriver serverinformationen till en CSV-fil.

Exempel på rapportmapp:

reports/
├── inventory_2026-11-12_1030.csv
└── inventory_2026-11-12_1145.csv

På så sätt kan flera rapporter sparas utan att tidigare rapporter skrivs över.

## 11. Testning av programmet

Följande funktioner bör testas för att kontrollera att programmet fungerar korrekt:

- Starta programmet utan argument.
- Visa alla servrar.
- Lägga till en ny server.
- Försöka lägga till en server med ett namn som redan finns.
- Ange en ogiltig miljö.
- Filtrera servrar efter miljö.
- Ta bort en server.
- Försöka ta bort en produktionsserver.
- Kontrollera en server som är tillgänglig.
- Kontrollera en server som inte är tillgänglig.
- Kontrollera alla servrar.
- Exportera en CSV-rapport.
- Starta programmet när JSON-filen saknas.
- Testa programmet med en egen sökväg via miljövariabeln.

Testerna bör utföras i Linux-miljön där programmet är avsett att köras.

## 12. Säkerhet och goda programmeringsvanor

Projektet följer några grundläggande principer för säker och strukturerad programmering:

- Serverinformation lagras separat från programmets kod.
- Miljövariabler används för konfiguration av datafilens sökväg.
- Användarinmatning kontrolleras innan information sparas.
- Produktionsservrar har ett extra skydd vid borttagning.
- Koden är uppdelad i moduler med tydliga ansvarsområden.
- `.gitignore` används för att undvika att tillfälliga filer och rapporter inkluderas i Git.

## 13. Sammanfattning

Server Inventory Tool är ett Python-baserat verktyg för att hantera och kontrollera servrar.

Projektet visar hur ett program kan delas upp i flera moduler, hantera data permanent, kommunicera med operativsystemet och erbjuda både interaktiv användning och automatiserad körning.
