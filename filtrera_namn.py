import csv

from pathlib import Path
current_working_directory = Path.cwd()
print(current_working_directory)

def filtrera_ord_saol(saol_fil, saol_csv_fil, utdata_txt_fil, utdata2_txt_fil):
    """
    Filtrerar bort ord med ordklassen 'namn' från en textfil baserat på en SAOL CSV-fil.

    Args:
        saol_fil (str): Sökvägen till textfilen med ord som ska filtreras.
        saol_csv_fil (str): Sökvägen till SAOL CSV-filen.
        utdata_txt_fil (str): Sökvägen där den filtrerade SAOL-listan ska sparas.
        utdata2_txt_fil (str): Sökvägen där de bortfiltrerade orden ska sparas.
    """

    # Ord som är namn och namn med 's' tillagt på slutet (genitivböjning) 
    namn_ord = set()

    # Läs in alla ord med ordklassen 'namn' från SAOL CSV-filen
    with open(saol_csv_fil) as csv_fil:
        csv_reader = csv.reader(csv_fil)
        for rad in csv_reader:
            if len(rad) > 2 and rad[2].strip().lower() == 'namn':
                ordet = rad[1].strip().lower()
                namn_ord.add(ordet)
                # Lägg även till böjningar med 's' i uppsättningen
                namn_ord.add(ordet + 's')

    filtrerade_ord = []

    # Filtrera dessa ord från textfilen med all ord i SAOL
    with open(saol_fil) as fil:
        for rad in fil:
            ordet = rad.strip().lower()
            if ordet not in namn_ord:
                filtrerade_ord.append(rad.strip())

    # Skriv den filtrerade SAOL-listan till utdatafilen
    with open(utdata_txt_fil, mode='w') as utdata_fil:
        for ordet in filtrerade_ord:
            utdata_fil.write(ordet + '\n')

    # Skriv bortfiltrerade ord till en andra utdatafil
    with open(utdata2_txt_fil, mode='w') as utdata2_fil:
        for ordet in namn_ord:
            utdata2_fil.write(ordet + '\n')

    print(f"Filtreringen är klar! De filtrerade orden har sparats i '{utdata_txt_fil}'.")
    print(f"Antal borttagna ord (inkl. böjningar med 's'): {len(namn_ord)}")
    print(f"Antal ord kvar efter filtrering: {len(filtrerade_ord)}")


# Filnamn
saol_filnamn = 'saol_wordlist.txt'            # SAOL textfil med alla ordformer 
saol_ordklasser_filnamn = 'saol2018clean.csv' # SAOL CSV-fil med ordklasser

utdata_filnamn = 'filtrerade_ord.txt'         # Utdata där ordklassen "namn" har rensats bort
utdata2_filnamn = 'bortfiltrerade_ord.txt'    # Ord som rensades bort

if __name__ == "__main__":
    filtrera_ord_saol(saol_filnamn, saol_ordklasser_filnamn, utdata_filnamn, utdata2_filnamn)