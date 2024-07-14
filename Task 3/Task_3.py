print ("Task 3")


def odstranit_posledni_radek(obsah_souboru):

    radky = obsah_souboru.split('\n')
    upravene_radky = radky[:-1]
    upraveny_obsah = '\n'.join(upravene_radky)

    return upraveny_obsah


def zapis_do_noveho_souboru(obsah, nazev_noveho_souboru):
    with open(nazev_noveho_souboru, 'w', encoding='utf-8') as f:
        f.write(obsah)

obsah_souboru = """Takto lze klasifikovat všechny soubory:

hlavní - jejichž přítomnost je povinná pro fungování operačního systému nebo jiného softwaru;

dočasné - někdy se vytvářejí při práci některých hlavních souborů pro ukládání mezivýsledků jejich práce."""

upraveny_obsah = odstranit_posledni_radek(obsah_souboru)

nazev_noveho_souboru = "txt_k_task_3.txt"
zapis_do_noveho_souboru(upraveny_obsah, nazev_noveho_souboru)

print(f"Odesláno do: {nazev_noveho_souboru}.")
