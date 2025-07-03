# WordFeud ordlista SAOL 14
Filen `WordFeud_ordlista.txt` innehåller en lista på alla giltiga ord som går att lägga i [WordFeud](https://sv.wikipedia.org/wiki/Wordfeud) med ordlistan "svenska - alla ordformer".

Ordlistor för SAOL 14 är hämtade från [axki/saol-wordlist](https://github.com/axki/saol-wordlist) (`saol_wordlist.txt` med alla ordformer) och [Torbacka/wordlist](https://github.com/Torbacka/wordlist) (`saol2018clean.csv` utan alla ordformer, men används för att identifiera ord med ordklassen "namn").

## Ändringar av SAOL 14
I WordFeud används SAOL 14 som ordlista, fast med vissa ändringar.

Följande ord är inte giltiga eller omöjliga i WordFeud:
* Ord som har ordklassen “namn”.
* Ord som har färre än 2 eller fler än 15 bokstäver.
* Ord som innehåller någon av följande bokstäver eller tecken: 
    * Q eller W
    * Ê, Ñ, Ç, Ü eller Æ
    * bindestreck (-), kolon (:), snedstreck (/), eller apostrof (‘)
    * siffror
    * mellanslag

För uppslagsorden som innehåller mellanslag går det även inte att lägga de ingående orden fristående. För till exempel uppslagsordet “a priori” i SAOL 14 går det inte att lägga “priori” i WordFeud.

Ord som innehåller särskilda bokstäver med diakritiska tecken går att lägga i WordFeud med motsvarande bokstav utan diakritiskt tecken:
* É -> E (filé skrivs som FILE)
* È -> E (chèvre skrivs som CHEVRE)
* À -> A (piteà skrivs som PITEA)
