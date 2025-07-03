import csv
import re

"""Filtrera SAOL 14 för WordFeud."""

# ----- Ta bort ord med ordklassen 'namn' -----

def filtrera_ord_saol(saol_csv_fil, ord_txt_fil):
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

    print("Filtreringen ar klar!")
    print(f"Antal borttagna ord (inkl. bojningar med 's'): {len(namn_ord)}")
    print(f"Antal ord kvar efter filtrering: {len(filtrerade_ord)}")
    return filtrerade_ord


# ----- Ersätt diakritiska tecken och filtrerar bort ord med ogiltiga tecken. -----

def rensa_tecken(indata_ord):
    accent_map = str.maketrans({
        'É': 'E', 'È': 'E', 'À': 'A',
        'é': 'E', 'è': 'E', 'à': 'A'
    })
    invalid_re = re.compile(r"[QWÊÑÇÜÆ\-:/'0-9 ]", re.IGNORECASE)

    delar_att_ta_bort = {
        part
        for w in indata_ord
        if ' ' in w
        for part in w.split()
    }
    godkanda_ord = [
        w.translate(accent_map)
        for w in indata_ord
        if ' ' not in w and not invalid_re.search(w.translate(accent_map)) and w not in delar_att_ta_bort
    ]

    print("Rensningen ar klar!")
    print(f"Antal ord kvar efter rensning: {len(godkanda_ord)}")
    return godkanda_ord


# ----- Filtrerar bort för korta och långa ord. -----

def filtrera_ord_efter_langd(indata_ord, min_langd=2, max_langd=15):
    godkanda_ord = [
        w
        for w in indata_ord
        if min_langd <= len(w) <= max_langd
    ]

    print("Filtreringen ar klar!")
    print(f"Antal ord kvar efter langdfiltrering: {len(godkanda_ord)}")
    return godkanda_ord


# ----- Rensar dubletter och sorterar orden. -----

def sortera_och_ta_bort_dubletter(indata_ord):
    sorterade_unika_ord = sorted({w for w in indata_ord if w})

    print("Filtreringen ar klar! Dubletter har tagits bort och orden har sorterats.")
    print(f"Antal unika ord: {len(sorterade_unika_ord)}")
    return sorterade_unika_ord




if __name__ == "__main__":
    saol_filnamn = 'saol2018clean.csv'  # SAOL CSV-fil utan alla ordformer
    ord_filnamn = 'saol_wordlist.txt'   # SAOL med alla ordformer
    slutlig_fil = 'WordFeud_ordlista.txt'

    filtrerade_ord = filtrera_ord_saol(saol_filnamn, ord_filnamn)
    sanerade_ord = rensa_tecken(filtrerade_ord)
    langdfiltrerade_ord = filtrera_ord_efter_langd(sanerade_ord)
    slutlig_ordlista = sortera_och_ta_bort_dubletter(langdfiltrerade_ord)

    with open(slutlig_fil, 'w', newline='') as f:
        for ordet in slutlig_ordlista:
            f.write(ordet + '\n')

    print(f"Slutlig ordlista sparad i '{slutlig_fil}' med {len(slutlig_ordlista)} ord.")

