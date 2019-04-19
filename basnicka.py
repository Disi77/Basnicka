from random import shuffle


def hlavicka(string):
    '''
    Vytiskne hlavičku se zadaným stringem
    '''
    print()
    print(50*'-')
    print(string.upper())
    print()


# Původní básnička
hlavicka('Původní básnička:')
with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor.readlines():
        print(radek.rstrip())


# Načíst básničku ze souboru a vrátit zpátky řádky v obráceném pořadí
hlavicka('Básnička - řádky v obráceném pořadí:')
with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in reversed(list(soubor.readlines())):
        print(radek.rstrip())


# Orátit pořadí slov ve verších
hlavicka('Básnička - slova v řádku v obráceném pořadí:')
seznam = []
with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor.readlines():
        seznam.append(radek.rstrip())

for zaznam in seznam:
    radek = zaznam.split()
    radek.reverse()
    novy_radek = ' '.join(radek)
    print(novy_radek)


# Obrátit pořadí slok (sloky oddělené prázdným řádkem)
hlavicka('Soubor s básničkou - sloky v obráceném pořadí:')
seznam = []
with open('basnicka.txt', encoding='utf-8') as soubor:
    text = soubor.read()

zacatek = 0
for x in range(text.count('\n\n')):
    konec = text.index('\n\n', zacatek+1)
    seznam.append(text[zacatek:konec].strip())
    zacatek = konec
seznam.append(text[zacatek:].strip())

seznam.reverse()
for sloka in seznam:
    print(sloka)
    print()


# Slova náhodně se zachováním původní struktury básně
hlavicka('Soubor s básničkou - přeházená slova:')
radky = []
with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor.readlines():
        radky.append(radek.rstrip())

# nejdříve zkoumám strukturu textu
delka_radek = []
seznam_0 = []
for radek in radky:
    delka = len(radek)
    delka_radek.append(delka)
    seznam_0.extend(radek.split())

seznam = []
for slovo in seznam_0:
    slovo = slovo.replace(',', '').replace('.', '').lower()
    seznam.append(slovo)

shuffle(seznam)

# pak z přeházených slov znovu tvořím báseň
nova_basnicka = []
pocet_radku = len(delka_radek)
pocet_mezer = delka_radek.count(0)
pocet_slov_na_radek, zbytek = divmod(len(seznam), (pocet_radku - pocet_mezer))

for kolo in range(pocet_radku):
    if delka_radek[kolo] != 0:
        radek = ''
        for x in range(pocet_slov_na_radek):
            radek += ' ' + seznam.pop()
        nova_basnicka.append(radek.strip())
    else:
        nova_basnicka.append('\n')

try:
    for zaznam in nova_basnicka:
        if len(zaznam) > 1:
            radek = zaznam
            radek = zaznam + ' ' + seznam.pop()
            nova_basnicka[nova_basnicka.index(zaznam)] = radek
except IndexError:
    pass

# Nastavím správný syntax - velké písmeno na začátku sloky apod.
index_mezery_odstavec = []
for i, x in enumerate(delka_radek):
    if x == 0:
        index_mezery_odstavec.append(i)

nova_basnicka[0] = nova_basnicka[0].capitalize()
for index in index_mezery_odstavec:
    nova_basnicka[index+1] = nova_basnicka[index+1].capitalize()

for i, radek in enumerate(nova_basnicka):
    if i == pocet_radku-1:
        nova_basnicka[i] += '.'
    elif (i+1) in index_mezery_odstavec:
        nova_basnicka[i] += '.'
    elif i in index_mezery_odstavec:
        pass
    else:
        nova_basnicka[i] += ','

for x in nova_basnicka:
    print(x)
