import os


def spocitat_vyskyt_slova(cesta_k_souboru, hledane_slovo):
    with open(cesta_k_souboru, 'r', encoding='utf-8') as soubor:
        obsah_souboru = soubor.read()

    slova = obsah_souboru.split()
    vyskyt = slova.count(hledane_slovo)

    return vyskyt

cesta_k_souboru = 'Text2'

hledane_slovo = input("Které slovo napočíítáme?: ")
vyskyt = spocitat_vyskyt_slova(cesta_k_souboru, hledane_slovo)
print(f"Slovo '{hledane_slovo}' se v souboru vyskytuje {vyskyt} krát.")
