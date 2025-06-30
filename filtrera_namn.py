import csv

def filtrera_ord_saol(saol_csv_fil, ord_txt_fil, utdata_txt_fil):
    """
    Filtrerar bort ord med ordklassen 'namn' från en textfil baserat på en SAOL CSV-fil.

    Args:
        saol_csv_fil (str): Sökvägen till SAOL CSV-filen.
        ord_txt_fil (str): Sökvägen till textfilen med ord som ska filtreras.
        utdata_txt_fil (str): Sökvägen där den filtrerade listan ska sparas.
    """

    namn_ord = set()

    # Läs in alla ord med ordklassen 'namn' från SAOL CSV-filen
    try:
        with open(saol_csv_fil, mode='r', encoding='utf-8') as saol_fil:
            saol_reader = csv.reader(saol_fil)
            for rad in saol_reader:
                if len(rad) > 2 and rad[2].strip().lower() == 'namn':
                    ordet = rad[1].strip().lower()
                    namn_ord.add(ordet)
                    # Lägg även till böjningar med 's' i uppsättningen
                    namn_ord.add(ordet + 's')
    except FileNotFoundError:
        print(f"Fel: SAOL CSV-filen '{saol_csv_fil}' kunde inte hittas.")
        return
    except Exception as e:
        print(f"Ett fel uppstod vid läsning av SAOL CSV-filen: {e}")
        return

    filtrerade_ord = []

    # Filtrera ord från den andra textfilen
    try:
        with open(ord_txt_fil, mode='r', encoding='utf-8') as ord_fil:
            for rad in ord_fil:
                ordet = rad.strip().lower()
                if ordet not in namn_ord:
                    filtrerade_ord.append(rad.strip()) # Behåll ursprungligt format om möjligt
    except FileNotFoundError:
        print(f"Fel: Ord-textfilen '{ord_txt_fil}' kunde inte hittas.")
        return
    except Exception as e:
        print(f"Ett fel uppstod vid läsning av ord-textfilen: {e}")
        return

    # Skriv de filtrerade orden till en ny fil
    try:
        with open(utdata_txt_fil, mode='w', encoding='utf-8') as utdata_fil:
            for ordet in filtrerade_ord:
                utdata_fil.write(ordet + '\n')
        print(f"Filtreringen är klar! De filtrerade orden har sparats i '{utdata_txt_fil}'.")
        print(f"Antal borttagna ord (inkl. böjningar med 's'): {len(namn_ord)}")
        print(f"Antal ord kvar efter filtrering: {len(filtrerade_ord)}")
    except Exception as e:
        print(f"Ett fel uppstod vid skrivning till utdatafilen: {e}")

# Ange dina filnamn här
saol_filnamn = 'saol2018clean.csv'  # Byt ut mot namnet på din SAOL CSV-fil
ord_filnamn = 'saol_wordlist.txt'    # Byt ut mot namnet på din textfil med ord
utdata_filnamn = 'filtrerade_ord.txt' # Namnet på den nya filen med filtrerade ord

# Anropa funktionen för att starta filtreringen
if __name__ == "__main__":
    filtrera_ord_saol(saol_filnamn, ord_filnamn, utdata_filnamn)