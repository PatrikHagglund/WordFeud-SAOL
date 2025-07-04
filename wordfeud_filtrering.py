"""Filtrera SAOL 14 för WordFeud.

Läser SAOL CSV och ordlista för att transformera och filtrera bort ord
för att passa WordFeud."""

import csv
import re

# Mappning för ersättning av vissa diakritiska tecken.
# ÉÈÀ men tex ej ÅÄÖ
accent_map = str.maketrans({
    'É': 'E', 'È': 'E', 'À': 'A'
})

# Regex för otillåtna tecken: siffror, bindestreck, vissa accenter m.m.
invalid_re = re.compile(r"[-QWÊÑÇÜÆ:/'0-9 ]", re.IGNORECASE)

def filtrera_ord_saol(saol_fil, saol_csv_fil):
    """Filtrera bort ord med ordklassen 'namn'.

    Tar bort namnord (inklusive 's'-former) enligt SAOL CSV ordlistan.
    """
    with open(saol_csv_fil) as csv_fil:
        namn_ord = {
            form
            for rad in csv.reader(csv_fil)
            if len(rad) > 2 and rad[2].strip().lower() == 'namn'
            for form in (rad[1].strip().lower(), rad[1].strip().lower() + 's')
        }

    with open(saol_fil) as ord_fil:
        alla_ord = [rad.strip() for rad in ord_fil]

    print(f"Läser '{saol_fil}' och '{saol_csv_fil}'")
    print(f"Antal ord från början: {len(alla_ord)}")

    filtrerade_ord = [
        w
        for w in alla_ord
        if w.lower() not in namn_ord
    ]

    print(f"Antal ord kvar efter bortrensning av namn: {len(filtrerade_ord)}")
    return filtrerade_ord


def rensa_tecken(indata_ord):
    """Ersätt diakritiska tecken och filtrera bort ord med otillåtna tecken."""
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

    print(f"Antal ord kvar efter rensning och filtrering på tecken: {len(godkanda_ord)}")
    return godkanda_ord


def filtrera_ord_efter_langd(indata_ord, min_langd=2, max_langd=15):
    """Filtrera bort för korta och långa ord."""
    godkanda_ord = [
        w
        for w in indata_ord
        if min_langd <= len(w) <= max_langd
    ]

    print(f"Antal ord kvar efter rensning på ordlängd: {len(godkanda_ord)}")
    return godkanda_ord


def sortera_och_ta_bort_dubletter(indata_ord):
    """Rensa dubletter och sortera ord."""
    sorterade_unika_ord = sorted({w for w in indata_ord if w})

    print(f"Antal ord kvar efter rensning av dubbletter: {len(sorterade_unika_ord)}")
    return sorterade_unika_ord


def main():
    import argparse

    p = argparse.ArgumentParser(description="Filtrera SAOL för WordFeud.")
    p.add_argument("--saol", default="saol_wordlist.txt")
    p.add_argument("--saol-csv", default="saol2018clean.csv")
    p.add_argument("--output", default="WordFeud_ordlista.txt")
    args = p.parse_args()

    ord1 = filtrera_ord_saol(args.saol, args.saol_csv)
    ord2 = rensa_tecken(ord1)
    ord3 = filtrera_ord_efter_langd(ord2)
    ord4 = sortera_och_ta_bort_dubletter(ord3)

    with open(args.output, "w", newline='') as fd:
        fd.writelines(w + "\n" for w in ord4)
    print(f"Sparat i '{args.output}'")

if __name__ == "__main__":
    main()
