import csv
import re

"""Filtrera SAOL 14 för WordFeud."""

# ----- Ta bort ord med ordklassen 'namn' -----

def filtrera_ord_saol(saol_csv_fil, ord_txt_fil, utdata_txt_fil):
    """Filtrerar ord som har ordklassen 'namn' enligt SAOL."""
    # Läs in alla ord med ordklassen 'namn' (inkl. böjning på 's')
    with open(saol_csv_fil) as saol_fil:
        namn_ord = {
            rad[1].strip().lower()
            for rad in csv.reader(saol_fil)
            if len(rad) > 2 and rad[2].strip().lower() == 'namn'
        }
    namn_ord |= {f"{w}s" for w in namn_ord}

    # Filtrera ord från ordlista (exkl. namnord)
    with open(ord_txt_fil) as ord_fil:
        filtrerade_ord = [
            rad.strip()
            for rad in ord_fil
            if rad.strip().lower() not in namn_ord
        ]

    # Skriv de filtrerade orden till en ny fil
    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in filtrerade_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Filtreringen ar klar! De filtrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal borttagna ord (inkl. bojningar med 's'): {len(namn_ord)}")
    print(f"Antal ord kvar efter filtrering: {len(filtrerade_ord)}")


# ----- Ersätt diakritiska tecken och filtrerar bort ord med ogiltiga tecken. -----

def rensa_tecken(indata_txt_fil, utdata_txt_fil):
    accent_map = str.maketrans({
        'É': 'E', 'È': 'E', 'À': 'A',
        'é': 'E', 'è': 'E', 'à': 'A'
    })
    invalid_re = re.compile(r"[QWÊÑÇÜÆ\-:/'0-9 ]", re.IGNORECASE)

    delar_att_ta_bort = {
        part
        for line in open(indata_txt_fil)
        if ' ' in line.strip()
        for part in line.strip().split()
    }
    godkanda_ord = [
        word
        for line in open(indata_txt_fil)
        for word in [line.strip().translate(accent_map)]
        if ' ' not in line.strip() and not invalid_re.search(word) and word not in delar_att_ta_bort
    ]

    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in godkanda_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Rensningen ar klar! De sanerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal ord kvar efter rensning: {len(godkanda_ord)}")


# ----- Filtrerar bort för korta och långa ord. -----

def filtrera_ord_efter_langd(indata_txt_fil, utdata_txt_fil, min_langd=2, max_langd=15):

    # Läs in ord från indatafil och filtrera på längd
    with open(indata_txt_fil) as indata_fil:
        godkanda_ord = [
            rad.strip()
            for rad in indata_fil
            if min_langd <= len(rad.strip()) <= max_langd
        ]

    # Skriv de filtrerade orden till en ny fil
    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in godkanda_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Filtreringen ar klar! De langdfiltrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal ord kvar efter langdfiltrering: {len(godkanda_ord)}")


# ----- Rensar dubletter och sorterar orden. -----

def sortera_och_ta_bort_dubletter(indata_txt_fil, utdata_txt_fil):

    # Läs in ord och skapa sorterad lista av unika ord
    with open(indata_txt_fil) as indata_fil:
        sorterade_unika_ord = sorted(
            {rad.strip() for rad in indata_fil if rad.strip()}
        )

    # Skriv resultatet till en ny fil
    with open(utdata_txt_fil, 'w', newline='') as utdata_fil:
        for ordet in sorterade_unika_ord:
            utdata_fil.write(ordet + '\n')

    print("Filtreringen ar klar! Dubletter har tagits bort och orden har sorterats.")
    print(f"De sorterade unika orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal unika ord: {len(sorterade_unika_ord)}")




if __name__ == "__main__":

    saol_filnamn = 'saol2018clean.csv'  # SAOL CSV-fil utan alla ordformer
    ord_filnamn = 'saol_wordlist.txt'   # SAOL med alla ordformer
    filtrerade_namn_fil = 'filtrerade_ord1.txt'
    filtrera_ord_saol(saol_filnamn, ord_filnamn, filtrerade_namn_fil)

    sanerade_fil = 'filtrerade_ord2.txt'
    rensa_tecken(filtrerade_namn_fil, sanerade_fil)

    filtrerade_langd_fil = 'filtrerade_ord3.txt'
    filtrera_ord_efter_langd(sanerade_fil, filtrerade_langd_fil)

    slutlig_fil = 'WordFeud_ordlista.txt'
    sortera_och_ta_bort_dubletter(filtrerade_langd_fil, slutlig_fil)

