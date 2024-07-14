import os #jsem si musel nechat poradit
def delka_nejdelsiho_slova(cesta_k_souboru):
    # utf-8 jsem si musel nechat poradit, ale je to paradni vec
    with open(cesta_k_souboru, 'r', encoding='utf-8') as soubor:
        obsah_souboru = soubor.read()

    # rozdelime obsah na slova, snadna zalezitost
    slova = obsah_souboru.split()

    # ze slov najdeme to nejdelsi, snadna vec
    nejdelsi_slovo = max(slova, key=len)
    delka_nejdelsiho_slova = len(nejdelsi_slovo)

    return delka_nejdelsiho_slova


# task 4 jsem pridal do slozky textu1. celkove jsem trochu zle rozdelil zlozky, ale uz to tak necham
cesta_k_souboru = 'Text1'

# delka nejdelsiho slova, to je uz easy
delka = delka_nejdelsiho_slova(cesta_k_souboru)

print(f"Délka nejdelšího slova je: {delka}")
