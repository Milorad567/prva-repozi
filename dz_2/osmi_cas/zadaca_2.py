""" Da se napravi programa vo koja korisnikot ke moze da vnesuva ime prezime, pol i godini na 10 lica i sekoj toj podatok da se zapise vo txt
fajl."""

for i in range(10):
    ime = input('Vnesete go vaseto ime: ')
    prezime = input('{} vnesete vaseto prezime: '.format(ime))
    pol = input('{} {} vnesete go vasiot pol: '.format(ime,prezime))
    godini = int(input('{} {} vnesete gi vasite godini: '.format(ime,prezime)))


    fajl = open('2.1.VtoraZadaca.txt', mode='a')
    fajl.write('\nIme: {}'.format(ime))
    fajl.write('\nPrezime: {}'.format(prezime))
    fajl.write('\nPol: {}'.format(pol))
    fajl.write('\nGodini: {}'.format(godini))
fajl.close()