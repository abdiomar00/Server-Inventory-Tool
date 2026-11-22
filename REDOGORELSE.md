Välj tre olika konstruktioner i koden, till exempel ett villkor, en loop och en funktion med parametrar och return. Förklara hur syntaxen fungerar och vad koden gör.

*Villkor* I `meny.py`, funktionen `find_server(servers, namn)`, används en for-loop för att gå igenom servrarna. Villkoret `if server["namn"].lower() == namn.lower()` jämför namnen utan att skilja på stora och små bokstäver. Om namnet matchar returneras serverns dictionary, annars returneras `None`.

*Loop* I `meny.py`, funktionen `run_menu(servers, data_file)`, används `while True` för att visa menyn igen. När användaren väljer alternativ 8 avslutar `break` loopen.

*Funktion med parametrar och returvärde* I `kontroller.py` tar funktionen `check_server(server)` emot en server-dictionary, gör pingkontrollen, uppdaterar serverns status och tid för senaste kontroll och returnerar statusen `up` eller `down`.

Varför passar en lista med dictionaries för att lagra servrarna? Vilka datatyper har värdena i en server?

En lista passar eftersom programmet hanterar flera servrar och behöver kunna gå igenom dem. Varje dictionary samlar egenskaper för en server under tydliga nycklar. Värdena `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad` är strängar. `senast_kontrollerad` är en tom sträng innan servern har kontrollerats.

Varför sparar du data i JSON men exporterar rapporten som CSV?

JSON används för den löpande lagringen eftersom det kan representera en lista med dictionaries och läsas in igen av Python. CSV passar för rapporter eftersom informationen sparas i tabellformat och kan öppnas i exempelvis kalkylprogram. Funktionen `export_csv` skriver serverns namn, adress, miljö, roll, status och senaste kontrolltid till en CSV-fil i mappen `reports`.

Hur är programmet uppdelat i moduler och funktioner? Vilket ansvar har varje fil?

`main.py` startar programmet, läser kommandoradsargument med `argparse`, laddar serverlistan och anropar funktioner från de andra modulerna. `meny.py` ansvarar för textmenyn och funktioner för att hitta, visa, lägga till och ta bort servrar. `lagring.py` läser och sparar JSON samt exporterar CSV. `kontroller.py` utför pingkontroller och uppdaterar serverns status och kontrolltid. `server.json.py` innehåller exempeldata i JSON-format.

Vilka moduler från standardbiblioteket använder du och till vad?

`pathlib` används i `lagring.py` för sökvägar och kataloger. `json` läser och skriver serverdata. `csv` skapar rapporter. `datetime` skapar tidsstämplar för kontroller och rapportfilnamn. `subprocess` kör pingkommandot. `os` läser miljövariabler för datafilens sökväg och pingens timeout. `argparse` läser kommandoradsargument och `sys` skickar programmets avslutningskod till operativsystemet.

Ge tre exempel på god praxis från din kod och förklara varför de är bra.

*Beskrivande namn* Funktioner som `check_server()` och `export_csv()` visar vad de gör.

*En uppgift per modul* Lagring, pingkontroller och meny ligger i olika filer. Det gör koden lättare att förstå och ändra.

*Återanvändning* Både meny och kommandoradsgränssnitt använder kontrollfunktionerna från `kontroller.py`, därför behöver pinglogiken bara underhållas på ett ställe.

Vilka källor och hjälpmedel har du använt och till vad? Det kan till exempel vara kursboken, dokumentation, forum eller AI-verktyg.

Jag har använt kursmaterial och lektionsanteckningar, AI-verktyg, YouTube och W3Schools som hjälp för att förstå Python och programmets funktioner.
