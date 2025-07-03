import csv
import re
import subprocess

"""Filtrera SAOL 14 för WordFeud."""

# Git-objektshashar för filer som används av skriptet. Uppdatera dessa med:
#   git hash-object saol_wordlist.txt saol2018clean.csv WordFeud_ordlista.txt
EXPECTED_HASHES = {
    "saol_wordlist.txt": "d179d76cb04baafcd5741767c027b36b8230a839",
    "saol2018clean.csv": "1ff05dc06860ac85fde80dc938979556de90366e",
    "WordFeud_ordlista.txt": "362f6e71ba0491dba348523c654763271630b434",
}

def git_hash_of_file(path: str) -> str:
    """Returnera git-objektets SHA-1-hash för en fil."""
    return subprocess.check_output([
        "git",
        "hash-object",
        path,
    ], text=True).strip()

def test_expected_hashes() -> None:
    """Kontrollera att filer inte förändrats sedan de checkades in."""
    for fil, expected in EXPECTED_HASHES.items():
        actual = git_hash_of_file(fil)
        assert actual == expected, f"Hashvärdet för {fil} stämmer inte"

# ----- Ta bort ord med ordklassen 'namn' -----

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

# ----- Ersätt diakritiska tecken och filtrerar bort ord med ogiltiga tecken. -----

def rensa_tecken(indata_txt_fil, utdata_txt_fil):
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


# ----- Filtrerar bort för korta och långa ord. -----

def filtrera_ord_efter_langd(indata_txt_fil, utdata_txt_fil, min_langd=2, max_langd=15):

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


# ----- Rensar dubletter och sorterar orden. -----

def sortera_och_ta_bort_dubletter(indata_txt_fil, utdata_txt_fil):

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
    test_expected_hashes()
