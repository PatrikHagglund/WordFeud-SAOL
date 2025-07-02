"""Tar bort dubletter och sorterar en ordlista."""

def sortera_och_ta_bort_dubletter(indata_txt_fil, utdata_txt_fil):
    """Rensar dubletter och sorterar orden."""
    unika_ord = set()

    # Las in ord fran indatafilen
    with open(indata_txt_fil) as indata_fil:
        for rad in indata_fil:
            ordet = rad.strip()
            if ordet:
                unika_ord.add(ordet)

    sorterade_unika_ord = sorted(unika_ord)

    # Skriv resultatet till en ny fil
    with open(utdata_txt_fil, 'w') as utdata_fil:
        for ordet in sorterade_unika_ord:
            utdata_fil.write(ordet + '\n')

    print("Filtreringen ar klar! Dubletter har tagits bort och orden har sorterats.")
    print(f"De sorterade unika orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal unika ord: {len(sorterade_unika_ord)}")


# Ange dina filnamn har
# Anta att 'filtrerade_langd_ord.txt' ar resultatet fran det forra skriptet
indata_filnamn = 'filtrerade_langd_ord.txt'  # Byt ut mot namnet pa filen du vill rensa
utdata_filnamn = 'slutlig_ordlista.txt'    # Namnet pa den nya filen med sorterade, unika ord


if __name__ == "__main__":
    sortera_och_ta_bort_dubletter(indata_filnamn, utdata_filnamn)
