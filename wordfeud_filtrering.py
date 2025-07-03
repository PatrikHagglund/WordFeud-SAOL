import csv
import re

# Mappning för ersättning av specifika diakritiska tecken
accent_map = str.maketrans({
    'É': 'E', 'È': 'E', 'À': 'A',
    'é': 'E', 'è': 'E', 'à': 'A'
})

# Reguljärt uttryck för ogiltiga tecken (siffror, bindestreck, vissa accenter m.m.)
invalid_re = re.compile(r"[-QWÊÑÇÜÆ:/'0-9 ]", re.IGNORECASE)

"""Filtrera SAOL 14 för WordFeud."""

# ----- Ta bort ord med ordklassen 'namn' -----

def filtrera_ord_saol(saol_csv_fil, ord_txt_fil):
    """Filtrerar ord som har ordklassen 'namn' enligt SAOL."""
    # Läs in alla ord med ordklassen 'namn' (inkl. böjning på 's')
    with open(saol_csv_fil) as saol_fil:
        namn_ord = {
            form
            for rad in csv.reader(saol_fil)
            if len(rad) > 2 and rad[2].strip().lower() == 'namn'
            for form in (rad[1].strip().lower(), rad[1].strip().lower() + 's')
        }

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
    delar_att_ta_bort = {
        part
        for w in indata_ord if ' ' in w
        for part in w.split()
    }
    godkanda_ord = []
    for w in indata_ord:
        if ' ' in w or invalid_re.search(w):
            continue
        w2 = w.translate(accent_map)
        if w2 in delar_att_ta_bort:
            continue
        godkanda_ord.append(w2)

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




def main():
    import argparse

    p = argparse.ArgumentParser(description="Filtrera SAOL för WordFeud.")
    p.add_argument("--saol-csv", default="saol2018clean.csv")
    p.add_argument("--saol", default="saol_wordlist.txt")
    p.add_argument("--output", default="WordFeud_ordlista.txt")
    args = p.parse_args()

    ord1 = filtrera_ord_saol(args.saol_csv, args.saol)
    ord2 = rensa_tecken(ord1)
    ord3 = filtrera_ord_efter_langd(ord2)
    ord4 = sortera_och_ta_bort_dubletter(ord3)

    with open(args.output, "w", newline='') as fd:
        fd.writelines(w + "\n" for w in ord4)
    print(f"Sparat {len(ord4)} ord i '{args.output}'")

if __name__ == "__main__":
    main()
