

br_na_lica = int(input('Za kolku lica sakate da vnesite podatoci? '))
for i in range(br_na_lica):
    ime = input('Vnesete ime: ')
    prezime = input('Vnesete prezime: ')
    godini = int(input('Vnesete godini: '))
    if godini > 18:
        print(f'Liceto {ime} {prezime} e polnoletno.')
    elif godini < 18:
     print(f'Liceto {ime} {prezime} e tocno 18.')
    else:
        print(f'Liceto {ime} {prezime} e maloletno.')
