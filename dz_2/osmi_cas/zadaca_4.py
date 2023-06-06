"""4. Da se napravi programa vo koja korisnikot ke vnese dva broevi, ke se zacuvaat vo dictionary, ke se izvrsat osnovnite matematicki operacii i isto taka ke se zacuvaat vo dictionary.
Celiot toj dictionary da se zapise vo nov json fajl"""

x = int(input('Vnesete go vasiot 1 broj: '))
y = int(input('Vnesete go vasiot 2 broj: '))

zbir = x + y
razlika = x - y
proizvod = x * y
kolicnik = x / y

fajl = open('1.1.PrvaZadaca.txt', mode='a')
fajl.write('\nZbirot na vasite broevi {} + {} e: {}'.format(x, y, zbir)) 
fajl.write('\nRazlikata na vasite broevi {} - {} e: {}'.format(x,y,razlika))
fajl.write('\nProizvodot na vasite broevi {} * {} e: {}'.format(x,y,proizvod))
fajl.write('\nKolicnikot na vasite broevi {} / {} e: {}'.format(x,y,kolicnik))
fajl.close()