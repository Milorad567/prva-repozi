#6 Zadaca: Da se napravi programa 
# vo koja korisnikot ke vnese broj 
# i da se proveri dali toj broj e pomal od 10, 
# pomal od 100, pomal od 1000 ili pogolem od 1000

broj1 = int(input("Vnesete go vasiot broj: "))

if broj1 < 10:
    print("Vasiot broj {} e pomal od 10".format(broj1))
elif broj1 < 100:
    print("Vasiot broj {} e pomal od 100".format(broj1))
elif broj1 < 1000:
    print("Vasiot broj {} e pomal od 1000".format(broj1))
else:
    print("Vasiot broj {} e pogolem od 1000".format(broj1))