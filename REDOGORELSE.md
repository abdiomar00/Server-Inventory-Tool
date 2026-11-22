# Redogörelse

## Tre konstruktioner i koden

### Villkor

I `meny.py` använder `find_server(servers, namn)` en `for`-loop för att gå igenom servrarna. Villkoret `if server["namn"].lower() == namn.lower()` jämför namnen utan att skilja på stora och små bokstäver. Funktionen returnerar serverns dictionary vid träff och `None` om ingen server hittas.

### Loop

I `meny.py` använder `run_menu(servers, data_file)` en `while True`-loop för att visa menyn om och om igen. `break` avslutar loopen när användaren väljer alternativ 8. De andra valen anropar funktioner för att visa, lägga till, ta bort, kontrollera eller exportera servrar.

### Funktion med parametrar och returvärde

I `kontroller.py` tar `check_server(server)` emot en servers dictionary. Funktionen kör `ping` med `subprocess.run`, uppdaterar fälten `status` och `senast_kontrollerad` och returnerar statusen `up` eller `down`.

## Varför passar en lista med dictionaries för servrarna? Vilka datatyper har värdena?

En lista passar eftersom programmet hanterar flera servrar och behöver kunna gå igenom dem. Varje dictionary samlar fälten för en server under nycklar. Värdena `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad` är strängar. Innan servern kontrollerats är `senast_kontrollerad` en tom sträng.

## Varför sparas data i JSON men exporteras rapporten som CSV?

JSON passar för programmets löpande lagring eftersom det kan spara listan av dictionaries och läsas in igen av Python. CSV är praktiskt för rapporter eftersom det är tabellformat och kan öppnas eller bearbetas i exempelvis kalkylprogram. `export_csv` skapar mappen `reports` vid behov och skriver fälten `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad` till en ny CSV-fil.

## Hur är programmet uppdelat i moduler och funktioner?

- `main.py` läser kommandoradsargument med `argparse`, laddar serverlistan och anropar meny-, kontroll- och lagringsfunktioner.
- `meny.py` innehåller den interaktiva menyn samt funktioner för att hitta, visa, lägga till och ta bort servrar.
- `lagring.py` väljer sökväg till datafilen, läser och sparar JSON samt exporterar CSV.
- `kontroller.py` kör pingkontroller och uppdaterar status och tid för senaste kontroll.
- `server.json.py` innehåller exempeldata i JSON-format.

## Vilka moduler från standardbiblioteket används och till vad?

- `argparse` läser kommandoradsargument i `main.py`.
- `sys` skickar programmets avslutningskod till operativsystemet.
- `json` läser och skriver serverlistan.
- `csv` skriver CSV-rapporter.
- `os` läser miljövariabler för datafilens sökväg och pingens timeout.
- `pathlib` hanterar sökvägar och skapar kataloger.
- `datetime` skapar tidpunkten för senaste kontroll och tidsstämpeln i rapportfilens namn.
- `subprocess` kör systemkommandot `ping`.

## Tre exempel på god praxis

- **Beskrivande namn:** `check_server` och `export_csv` gör funktionernas uppgifter tydliga.
- **Uppdelning i moduler:** meny, lagring och pingkontroller ligger i separata filer, vilket gör koden enklare att hitta och ändra.
- **Återanvändning:** både menyn och kommandoradsgränssnittet använder kontrollfunktionerna i `kontroller.py`, så pinglogiken finns på ett ställe.

## Vilka källor och hjälpmedel har använts och till vad?

Jag har använt kursmaterial och lektionsanteckningar, AI, YouTube och W3Schools som hjälp för att förstå Python och programmets funktioner.
