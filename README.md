# WordFeud ordlista SAOL 14
Filen `WordFeud_ordlista.txt´ innehåller en lista på alla giltiga ord som går att lägga i WordFeud med ordlistan "svenska - alla ordformer".

Ordlistor för SAOL 14 hämtade jag från [axki/saol-wordlist](https://github.com/axki/saol-wordlist) och [Torbacka/wordlist](https://github.com/Torbacka/wordlist).

## Ändringar av SAOL 14
I WordFeud används SAOL 14 som ordlista, fast med vissa ändringar.

Följande ord är inte giltiga i WordFeud: 
* Ord som har färre än 2 eller fler än 15 bokstäver
* Ord som har ordklassen “namn”
* Ord som innehåller någon av de följande bokstäverna eller tecknen: 
    * Q eller W
    * Ê, Ñ, Ç, Ü eller Æ
    * bindestreck (-), kolon (:), eller apostrof (‘)
    * siffror
    * mellanslag

För uppslagsorden som innehåller mellanslag går det även inte att lägga de ingående orden för sig själva. För till exempel uppslagsordet “a priori” i SAOL 14 går det inte att lägga “priori” i WordFeud. 

Ord som innehåller särskilda bokstäver med diakritiska tecken går fortfarande att lägga i WordFeud med hjälp av motsvarande bokstav utan diakritiskt tecken.
* É -> E (filé skrivs som FILE)
* È -> E (chèvre skrivs som CHEVRE)
* À -> A (piteà skrivs som PITEA)