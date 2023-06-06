"""Da se kreira programa vo koja korisnikot ke vnese stranite na pravogaolnik i ke se zacuvaat vo dictionary.
 Da se presmeta plostinata i perimetarot, rezultatite isto taka da se zacuvaat vo dictionary vo razlicni indexi. 
   Da se napravi sporedba koj rezultat e pogolem i da se zacuva toa vo index "pogolem"""

pravoagolnik = {}

stranaA = int(input('Vnesete dimenzii na stranaA: '))
stranaB = int(input('Vnesete dimenzii na stranaB: '))

pravoagolnik['StranaA'] = stranaA
pravoagolnik['StranaB'] = stranaB

plostina = pravoagolnik["StranaA"] * pravoagolnik["StranaB"]
perimetar = 2*pravoagolnik['StranaA'] + 2*pravoagolnik['StranaB']

pravoagolnik['Plostina'] = plostina
pravoagolnik['Perimetar'] = perimetar

if plostina > perimetar:
    print('Plostinata na pravoagolnikot {} e pogolemo od perimetarot {}.'.format(plostina,perimetar))
    pravoagolnik['Pogolem'] = plostina
else:
    pravoagolnik['Pogolem'] = perimetar
    print('Perimetarot na pravoagolnikot {} e pogolem od plostinata {}.'.format(perimetar,plostina))

print("Plostinata e: {} * {} = {}".format(pravoagolnik["StranaA"],pravoagolnik["StranaB"], plostina))
print("Perimetarot e: 2*{} + 2*{} = {}".format(pravoagolnik["StranaA"], pravoagolnik["StranaB"], perimetar))

for i in pravoagolnik.items():
    print(i)