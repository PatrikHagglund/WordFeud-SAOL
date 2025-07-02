"""Filtrerar ord i en textfil baserat pa deras langd."""

def filtrera_ord_efter_langd(indata_txt_fil, utdata_txt_fil, min_langd=2, max_langd=15):
    """Filtrerar ord baserat pa langd."""
    godkanda_ord = []

    # Las in ord fran indatafilen och filtrera dem
    with open(indata_txt_fil) as indata_fil:
        for rad in indata_fil:
            ordet = rad.strip()  # Behall ursprunglig skiftlage
            if min_langd <= len(ordet) <= max_langd:
                godkanda_ord.append(ordet)

    # Skriv de filtrerade orden till en ny fil
    with open(utdata_txt_fil, 'w') as utdata_fil:
        for ordet in godkanda_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Filtreringen ar klar! De langdfiltrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal ord kvar efter langdfiltrering: {len(godkanda_ord)}")


# Ange dina filnamn har
# Anta att 'filtrerade_ord.txt' ar resultatet fran det forra skriptet
indata_filnamn = 'filtrerade_ord.txt'  # Byt ut mot namnet pa filen du vill filtrera
utdata_filnamn = 'filtrerade_langd_ord.txt'  # Namnet pa den nya filen med langdfiltrerade ord


if __name__ == "__main__":
    filtrera_ord_efter_langd(indata_filnamn, utdata_filnamn)
