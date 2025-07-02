import csv

"""Filtrerar bort ord av ordklassen 'namn'."""

def filtrera_ord_saol(saol_csv_fil, ord_txt_fil, utdata_txt_fil):
    """Filtrerar ord som har ordklassen 'namn' enligt SAOL."""
    namn_ord = set()

    # Las in alla ord med ordklassen 'namn'
    with open(saol_csv_fil, mode='r', encoding='utf-8') as saol_fil:
        saol_reader = csv.reader(saol_fil)
        for rad in saol_reader:
            if len(rad) > 2 and rad[2].strip().lower() == 'namn':
                ordet = rad[1].strip().lower()
                namn_ord.add(ordet)
                namn_ord.add(ordet + 's')

    filtrerade_ord = []

    # Filtrera ord fran den andra textfilen
    with open(ord_txt_fil, mode='r', encoding='utf-8') as ord_fil:
        for rad in ord_fil:
            ordet = rad.strip().lower()
            if ordet not in namn_ord:
                filtrerade_ord.append(rad.strip())

    # Skriv de filtrerade orden till en ny fil
    with open(utdata_txt_fil, mode='w', encoding='utf-8') as utdata_fil:
        for ordet in filtrerade_ord:
            utdata_fil.write(ordet + '\n')

    print(f"Filtreringen ar klar! De filtrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal borttagna ord (inkl. bojningar med 's'): {len(namn_ord)}")
    print(f"Antal ord kvar efter filtrering: {len(filtrerade_ord)}")


# Ange dina filnamn har
saol_filnamn = 'saol2018clean.csv'  # Byt ut mot namnet pa din SAOL CSV-fil
ord_filnamn = 'saol_wordlist.txt'    # Byt ut mot namnet pa din textfil med ord
utdata_filnamn = 'filtrerade_ord.txt'  # Namnet pa den nya filen med filtrerade ord


if __name__ == "__main__":
    filtrera_ord_saol(saol_filnamn, ord_filnamn, utdata_filnamn)
