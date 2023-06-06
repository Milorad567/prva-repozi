#7 Zadaca: Da se napravi programa 
# vo koja korisnikot ke vnese stranite na pravoagolnik, 
# da se presmeta plostinata i perimetarot na pravoagolnikot. 
# Da se sporedat koj rezultat e pogolem i da se odredi dali 
# pogolemiot broj pomal od pomal od 10, pogolem od 10 
# a pomal od 50, pomal od 100 ili pogolem od 100


stranaA = int(input('Vnesete dimenzii na strana A od pravoagolnikot: '))
stranaB = int(input('Vnesete dimenzii na strana B od pravoagolnikot: '))

plostina = stranaA * stranaB
perimetar = 2*stranaA + 2*stranaB
print()
print('Plostinata na pravoagolnikot e {}.'.format(plostina))
print()
print('Perimetarot na pravoagolnikot e {}.'.format(perimetar))
print()

if plostina > perimetar:
    print('Plostinata na pravoagolnikot e {}, pogolema od perimetarot.'.format(plostina))
    print()
    if plostina < 10:
        print('Plostinata na pravoagolnikot {} e pomala od 10.'.format(plostina))
    elif plostina > 10 and plostina < 50:
        print('Plostinata na pravoagolnikot {} e pogolema od 10 a pomala od 50.'.format(plostina))
    elif plostina < 100:
        print('Plostinata na pravoagolnikot {} e pomala od 100.'.format(plostina))
    else:
        print('Plostinata na pravoagolnikot {} e pogolema od 100.'.format(plostina))
else:
    print('Perimetarot na pravoagolnikot e {} e pogolem od plostinata.'.format(perimetar))
    if perimetar < 10:
        print('Perimetar na pravoagolnikot {} e pomala od 10.'.format(perimetar))
    elif perimetar > 10 and perimetar < 50:
        print('Perimetar na pravoagolnikot {} e pogolema od 10 a pomala od 50.'.format(perimetar))
    elif perimetar < 100:
        print('Perimetar na pravoagolnikot {} e pomala od 100.'.format(perimetar))
    else:
        print('Perimetar na pravoagolnikot {} e pogolema od 100.'.format(perimetar))