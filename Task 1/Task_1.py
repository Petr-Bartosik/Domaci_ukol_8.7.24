def compare_files(file1_content, file2_content):
    # text pro zmenu rozdelim na radky pres split \n
    lines1 = file1_content.split('\n')
    lines2 = file2_content.split('\n')

    # Zjistime, zda se radky shoduji. tady jsem se zasekl na enumerate a zipu.
    #zkosuel jsem jine varianty, ale tuhle jsem se doptal chatu gpt i pro vysvetleni proc
    #tuto variantu
    for i, (line1, line2) in enumerate(zip(lines1, lines2), 1):
        if line1 != line2:
            print(f"Neshoduje se v: {i}:")
            print(f"Text1: {line1}")
            print(f"Text2: {line2}")

    # Zohledneni ruznych delek textu, tedy jejich celkoveho zpracovani
    if len(lines1) > len(lines2):
        for i in range(len(lines2), len(lines1)):
            print(f"Soubor 1 má extra řádek {i + 1}: {lines1[i]}")
    elif len(lines2) > len(lines1):
        for i in range(len(lines1), len(lines2)):
            print(f"Soubor 2 má extra řádek {i + 1}: {lines2[i]}")

file1_content = """Takto lze klasifikovat všechny soubory:

hlavní - jejichž přítomnost je povinná pro fungování operačního systému nebo jiného softwaru;
servisní - zodpovědné za různé konfigurace hlavních souborů;
pracovní - hlavní soubory pracují se svým obsahem, mění a vytvářejí data;
dočasné - někdy se vytvářejí při"""

file2_content = """Takto lze klasifikovat všechny soubory:

hlavní - jejichž přítomnost je povinná pro fungování operačního systému nebo jiného softwaru;

dočasné - někdy se vytvářejí při """

# musim vyvolat funkci pro porovnani obou textu
compare_files(file1_content, file2_content)
