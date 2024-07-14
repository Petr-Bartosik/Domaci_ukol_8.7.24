def najit_a_nahradit(cesta_k_souboru, hledane_slovo, nahradit_slovo):
    # stejny postup jak z ukolu 5
    with open(cesta_k_souboru, 'r', encoding='utf-8') as soubor:
        obsah_souboru = soubor.read()

    # rutina z drivejsich ukolu
    novy_obsah = obsah_souboru.replace(hledane_slovo, nahradit_slovo)

    # novy obsah musim zpet zapsat
    with open(cesta_k_souboru, 'w', encoding='utf-8') as soubor:
        soubor.write(novy_obsah)

    print(f"Slovo '{hledane_slovo}' nahrazeno '{nahradit_slovo}'.")
#cemu uplne nerozumim, proc to bere jen nazev souboru, ale bez pripony.
cesta_k_souboru = 'Text2'

#klasika inputy
hledane_slovo = input("Co najdeme?: ")
nahradit_slovo = input("Čím nahradíme?: ")
najit_a_nahradit(cesta_k_souboru, hledane_slovo, nahradit_slovo)
