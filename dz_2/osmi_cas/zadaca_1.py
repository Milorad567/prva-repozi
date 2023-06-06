"""1. Da se napravi programa vo koja korisnikot ke vnese 2 broevi. Da se izvrsat osnovnite matematicki operacii
 i da izrazite da se zapisaat vo
txt fajl
broj1+broj2 = zbir"""

"""broj1=int(input("Vnesete eden broj: "))
broj2=int(input("Vnesete drug broj: "))
zbir=0
proizvod=1
zbir=broj1+broj2
razlika=broj1-broj2
proizvod=broj1*broj2
kolicnik=broj1/broj2
print(f"Zbirot na dvata broja e: {zbir}")
print(f"Razlikata na dvata broja e: {razlika}")
print(f"Proizvodot na dvata broja e: {proizvod}")
print(f"Kolicnikot na dvata broja e: {kolicnik}")"""

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