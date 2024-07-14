print ("Task 2")
def vypocitej_statistiky(obsah_souboru):
    samohlasky = "aeiouáéíóúýěůAEIOUÁÉÍÓÚÝĚŮ"
    souhlasky = "bcčdďfghjklmnňpqrřsštťvwxzžBCČDĎFGHJKLMNŇPQRŘSŠTŤVWXZŽ"

    pocet_znaku = len(obsah_souboru)
    pocet_radku = obsah_souboru.count('\n') + 1
    pocet_samohlasek = sum(1 for char in obsah_souboru if char in samohlasky)
    pocet_souhlasek = sum(1 for char in obsah_souboru if char in souhlasky)
    pocet_cislic = sum(1 for char in obsah_souboru if char.isdigit())

    return {
        "Počet znaků": pocet_znaku,
        "Počet řádků": pocet_radku,
        "Počet samohlásek": pocet_samohlasek,
        "Počet souhlásek": pocet_souhlasek,
        "Počet číslic": pocet_cislic
    }

def zapis_statistiky_do_souboru(statistiky, nazev_vystupniho_souboru):
    with open(nazev_vystupniho_souboru, 'w', encoding='utf-8') as f:
        for klic, hodnota in statistiky.items():
            f.write(f"{klic}: {hodnota}\n")

# Obsah zdrojového souboru (poskytnutý text)
obsah_souboru = """Takto lze klasifikovat všechny soubory:

hlavní - jejichž přítomnost je povinná pro fungování operačního systému nebo jiného softwaru;
servisní - zodpovědné za různé konfigurace hlavních souborů;
pracovní - hlavní soubory pracují se svým obsahem, mění a vytvářejí data;
dočasné - někdy se vytvářejí při práci ně"""

# Výpočet statistik
statistiky = vypocitej_statistiky(obsah_souboru)

# Zápis statistik do nového souboru
nazev_vystupniho_souboru = "statistiky.txt"
zapis_statistiky_do_souboru(statistiky, nazev_vystupniho_souboru)

print(f"Statistiky byly zapsány do souboru {nazev_vystupniho_souboru}.")
