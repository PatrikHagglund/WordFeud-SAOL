import csv
import re

"""Utility functions to process word lists for WordFeud."""

# ----- Previously in filtrera_namn.py -----

def filtrera_ord_saol(saol_csv_fil, ord_txt_fil, utdata_txt_fil):
    """Filtrerar ord som har ordklassen 'namn' enligt SAOL."""
    namn_ord = set()

    # Las in alla ord med ordklassen 'namn'
    with open(saol_csv_fil) as saol_fil:
        saol_reader = csv.reader(saol_fil)
        for rad in saol_reader:
            if len(rad) > 2 and rad[2].strip().lower() == 'namn':
                ordet = rad[1].strip().lower()
                namn_ord.add(ordet)
                namn_ord.add(ordet + 's')

    filtrerade_ord = []

    # Filtrera ord fran den andra textfilen
    with open(ord_txt_fil) as ord_fil:
        for rad in ord_fil:
            ordet = rad.strip().lower()
            if ordet not in namn_ord:
                filtrerade_ord.append(rad.strip())

    # Skriv de filtrerade orden till en ny fil
    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in filtrerade_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Filtreringen ar klar! De filtrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal borttagna ord (inkl. bojningar med 's'): {len(namn_ord)}")
    print(f"Antal ord kvar efter filtrering: {len(filtrerade_ord)}")


def rensa_tecken(indata_txt_fil, utdata_txt_fil):
    """Ersatter diakritiska tecken och filtrerar bort ord med ogiltiga tecken."""
    accent_map = str.maketrans({
        'É': 'E', 'È': 'E', 'À': 'A',
        'é': 'E', 'è': 'E', 'à': 'A'
    })
    invalid_re = re.compile(r"[QWÊÑÇÜÆ\-:/'0-9 ]", re.IGNORECASE)

    delar_att_ta_bort = set()
    godkanda_ord = []

    with open(indata_txt_fil) as indata_fil:
        for rad in indata_fil:
            ordet = rad.strip()

            if ' ' in ordet:
                for delord in ordet.split():
                    delar_att_ta_bort.add(delord)
                continue

            ordet = ordet.translate(accent_map)

            if not invalid_re.search(ordet):
                godkanda_ord.append(ordet)

    godkanda_ord = [o for o in godkanda_ord if o not in delar_att_ta_bort]

    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in godkanda_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Rensningen ar klar! De sanerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal ord kvar efter rensning: {len(godkanda_ord)}")


# ----- Previously in filtrera_langd.py -----

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
    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in godkanda_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Filtreringen ar klar! De langdfiltrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal ord kvar efter langdfiltrering: {len(godkanda_ord)}")


# ----- Previously in sortera_dubletter.py -----

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
    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in sorterade_unika_ord:
            utdata_fil.write(ordet + '\n')

    print("Filtreringen ar klar! Dubletter har tagits bort och orden har sorterats.")
    print(f"De sorterade unika orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal unika ord: {len(sorterade_unika_ord)}")


# Example pipeline when run as a script
if __name__ == "__main__":
    # Ange dina filnamn har
    saol_filnamn = 'saol2018clean.csv'  # SAOL CSV-fil
    ord_filnamn = 'saol_wordlist.txt'   # Textfil med ord
    filtrerade_namn_fil = 'filtrerade_ord.txt'

    filtrera_ord_saol(saol_filnamn, ord_filnamn, filtrerade_namn_fil)

    sanerade_fil = 'sanerade_ord.txt'
    rensa_tecken(filtrerade_namn_fil, sanerade_fil)

    filtrerade_langd_fil = 'filtrerade_langd_ord.txt'
    filtrera_ord_efter_langd(sanerade_fil, filtrerade_langd_fil)

    slutlig_fil = 'slutlig_ordlista.txt'
    sortera_och_ta_bort_dubletter(filtrerade_langd_fil, slutlig_fil)
