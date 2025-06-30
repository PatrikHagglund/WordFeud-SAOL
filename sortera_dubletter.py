def sortera_och_ta_bort_dubletter(indata_txt_fil, utdata_txt_fil):
    """
    Tar bort dubletter och sorterar orden i bokstavsordning från en textfil.

    Args:
        indata_txt_fil (str): Sökvägen till textfilen med ord som ska behandlas.
        utdata_txt_fil (str): Sökvägen där den rensade och sorterade listan ska sparas.
    """

    unika_ord = set() # Använd en set för att automatiskt hantera dubletter

    # Läs in ord från indatafilen och lägg till dem i seten
    try:
        with open(indata_txt_fil, mode='r', encoding='utf-8') as indata_fil:
            for rad in indata_fil:
                ordet = rad.strip()
                if ordet: # Se till att det inte är en tom rad
                    unika_ord.add(ordet)
    except FileNotFoundError:
        print(f"Fel: Indatafilen '{indata_txt_fil}' kunde inte hittas.")
        return
    except Exception as e:
        print(f"Ett fel uppstod vid läsning av indatafilen: {e}")
        return

    # Konvertera seten till en lista och sortera den bokstavsordning
    sorterade_unika_ord = sorted(list(unika_ord))

    # Skriv de sorterade och unika orden till en ny fil
    try:
        with open(utdata_txt_fil, mode='w', encoding='utf-8') as utdata_fil:
            for ordet in sorterade_unika_ord:
                utdata_fil.write(ordet + '\n')
        print(f"Filtreringen är klar! Dubletter har tagits bort och orden har sorterats.")
        print(f"De sorterade unika orden har sparats i '{utdata_txt_fil}'.")
        print(f"Antal unika ord: {len(sorterade_unika_ord)}")
    except Exception as e:
        print(f"Ett fel uppstod vid skrivning till utdatafilen: {e}")

# Ange dina filnamn här
# Anta att 'filtrerade_langd_ord.txt' är resultatet från det förra skriptet
indata_filnamn = 'filtrerade_langd_ord.txt' # Byt ut mot namnet på filen du vill rensa
utdata_filnamn = 'slutlig_ordlista.txt'    # Namnet på den nya filen med sorterade, unika ord

# Anropa funktionen för att starta processen
if __name__ == "__main__":
    sortera_och_ta_bort_dubletter(indata_filnamn, utdata_filnamn)