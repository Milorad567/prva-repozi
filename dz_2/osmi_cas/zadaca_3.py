"""Da se napravi programa koja ke go cita fajlot i ke gi pecati site podatoci za licata vo novi redovi
*BONUS: napravete go da bide za kolku lica saka korisnikot tolku"""

fajl = open('2.1.VtoraZadaca.txt', mode='r')
tekst = fajl.readlines()
for i in tekst:
    print(i)
