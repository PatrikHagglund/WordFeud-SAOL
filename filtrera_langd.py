def filtrera_ord_efter_langd(indata_txt_fil, utdata_txt_fil, min_langd=2, max_langd=15):
    """
    Filtrerar ord i en textfil baserat på deras längd.

    Args:
        indata_txt_fil (str): Sökvägen till textfilen med ord som ska filtreras.
        utdata_txt_fil (str): Sökvägen där den filtrerade listan ska sparas.
        min_langd (int): Minsta tillåtna längd för ett ord.
        max_langd (int): Största tillåtna längd för ett ord.
    """

    godkanda_ord = []

    # Läs in ord från indatafilen och filtrera dem
    try:
        with open(indata_txt_fil, mode='r', encoding='utf-8') as indata_fil:
            for rad in indata_fil:
                ordet = rad.strip() # Behåll ursprunglig skiftläge
                if min_langd <= len(ordet) <= max_langd:
                    godkanda_ord.append(ordet)
    except FileNotFoundError:
        print(f"Fel: Indatafilen '{indata_txt_fil}' kunde inte hittas.")
        return
    except Exception as e:
        print(f"Ett fel uppstod vid läsning av indatafilen: {e}")
        return

    # Skriv de filtrerade orden till en ny fil
    try:
        with open(utdata_txt_fil, mode='w', encoding='utf-8') as utdata_fil:
            for ordet in godkanda_ord:
                utdata_fil.write(ordet + '\n')
        print(f"Filtreringen är klar! De längdfiltrerade orden har sparats i '{utdata_txt_fil}'.")
        print(f"Antal ord kvar efter längdfiltrering: {len(godkanda_ord)}")
    except Exception as e:
        print(f"Ett fel uppstod vid skrivning till utdatafilen: {e}")

# Ange dina filnamn här
# Anta att 'filtrerade_ord.txt' är resultatet från det förra skriptet
indata_filnamn = 'filtrerade_ord.txt' # Byt ut mot namnet på filen du vill filtrera
utdata_filnamn = 'filtrerade_langd_ord.txt' # Namnet på den nya filen med längdfiltrerade ord

# Anropa funktionen för att starta filtreringen
if __name__ == "__main__":
    filtrera_ord_efter_langd(indata_filnamn, utdata_filnamn)