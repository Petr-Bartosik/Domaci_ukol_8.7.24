def vypocitej_statistiky(obsah_souboru):
    #omlouvam se, musim cele v cestine, se mi to v eng plete
    #vytvorim kompletni sumar funkci pro vypocet
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

# Vybral jsem text1 pro analýzu požadovaných hodnot a na konci přidal pár číslic pro ověření
obsah_souboru = """Takto lze klasifikovat všechny soubory:

hlavní - jejichž přítomnost je povinná pro fungování operačního systému nebo jiného softwaru;
servisní - zodpovědné za různé konfigurace hlavních souborů;
pracovní - hlavní soubory pracují se svým obsahem, mění a vytvářejí data;
dočasné - někdy se vytvářejí při práci ně123456789"""

# Výpočet statistik
statistiky = vypocitej_statistiky(obsah_souboru)

# vytisknuti statistik na obrazovku. nikoliv v txt zvlast.
for nazev, hodnota in statistiky.items():
    print(f"{nazev}: {hodnota}")
