Välj tre olika konstruktioner i koden, till exempel ett villkor, en loop och en funktion med parametrar och return. Förklara hur syntaxen fungerar och vad koden gör.
*Vilkor* I meny.py, funktionen hämta_server(), används if för att jämför servernamn. Om namnet matchar returneras servers dictionary annars fortsätter loopen.
*Loop* I meny.py , funktionen kör_meny(), används while true för att visa meny igen tills användaren väljer alternativ 8 och break avslutar loopen.
*Funktion med parametrar och returvärde* I kontroller.py, funktionen kontrollera_server(server), tar funktionen emot en serverdictionary, gör pingkontrollen och retunerar statusen up eller down.

Varför passar en lista med dictionaries för att lagra servrarna? Vilka datatyper har värdena i en server?
En lista passar eftersom programmet hanterar flera servrar och behöver kunna loopa igenom dem. Varje dictionary samlar egenskaper för en server under tydliga. nycklar. Exempelvis är 'namn', 'adress', 'miljo', 'roll' och 'status' strängar. 'senast_kontrollerad' är också en sträng, som är tom innan första kontrollen.

Varför sparar du data i JSON men exporterar rapporten som CSV?
JSON används för den löpande lagringen eftersom den kan representera en lista med dictionaries och kan läsas in igen av Python.

Hur är programmet uppdelat i moduler och funktioner? Vilket ansvar har varje fil?
Main.py startar programmet och hanterar CLI med argparse. Meny.py ansvarar för textmeny och användarens val. Lagring.py läser och sparar JSON samt exporterar CSV. Kontroller.py utför pingkontroller och uppdaterar servers status. Meny och CLI återanvänder lagrings och kontrollfunktionerna.

Vilka moduler från standardbiblioteket använder du och till vad?
Pathlib används i lagring.py för sökvägar och kontroll av om datafilen finns.
JSON läser och skriver JSON_data. CSV skapar rapporter.
Datetime skapar tidsstmpel för sökvägar och kontroller och rapportfilnamn.
Subprocess kör miljövatiabler. Argpares läser kommandoradsargument.
SYS skickar programmet exit code till operativsystemet.

Ge tre exempel på god praxis från din kod och förklara varför de är bra.
*Beskrivande namn* funktioner som kontrollera_server() och exportera-csv visar vad de gör.
*En ska per modul* lagring, ping och meny ligger i olika filer. Det gör koden lättare att förstå och ändra.
*Återanvändning* både meny och CLI använder samma kontrollfunktion därför behöver pinglogiken bara underhållas på ett ställe.

Vilka källor och hjälpmedel har du använt och till vad? Det kan till exempel vara kursboken, dokumentation, forum eller AI-verktyg.
Jag har använd kursmaterial och lektionsanteckningar, AI och we3school.
