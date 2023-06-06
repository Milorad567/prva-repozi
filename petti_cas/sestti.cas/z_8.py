"""Da se napravi programa vo koja korisnikot ke vnese ime, prezime, klas na nekoj ucenik i  ke se zacuvaat vo dictionary.
 Vo index otceni sto ke bide lista da se vnesat otcenite na ucenikot. Da se napravi funkcija koja ke go presmetuva prosekot na ucenik 
 i ke go vraka kako rezultat. Prosekot da se zacuva vo index prosek. Da se napravi druga funkcija koja ke go odreduva uspehot na ucenikot 
 a kako parametar ke se dava prosekot
0-1.5 - ne dovolen
1.5-2.5 dovolen
2.5-3.5 dobar
3.5-4.5 dobar
4.- 5 odlicen"""

klas = {
    "ime: ": "Bujamin",
    "prezime: ": "Curri",
    "Klas: ": 8,
    "otceni: ": [5, 4, 3, 4, 2, 4, 5, 5, 2, 3, 4, 3, 4, 5]
}

def prosek(klass):
    suma = sum(klas["otceni: "])
    klas['prosek'] = suma / len(klas["otceni: "])
    return klas['prosek']

klas['prosek'] = prosek(klas)
print('Prosekot na ucenikot e:', round(klas['prosek'], 2))

def uspeh(skolo):
    uspeh =""
    if klas['prosek'] >= 4.5:
        print('Uspehot na ucenikot {} e odlicen {}.'.format(klas["ime: "],klas['prosek']))
        uspeh ="odlicen"
    elif klas['prosek'] >= 3.5 and klas['prosek'] < 4.5:
        print('Uspehot na ucenikot {} e dobar {}.'.format(klas["ime: "],klas['prosek']))
        uspeh ="mn dobar"
    elif klas['prosek'] >= 2.5 and klas['prosek'] < 3.5:
        print('Uspehot na ucenikot {} e dobar {}.'.format(klas["ime: "],klas['prosek']))
        uspeh ="dobar"
    elif klas['prosek'] >= 1.5 and klas['prosek'] <2.5:
        print('Uspehot na ucenikot {} e dovolen {}.'.format(klas["ime: "],klas['prosek']))
        uspeh ="dovolen"
    elif klas['prosek'] > 0 and klas['prosek'] < 1.5:
        print('Uspehot na ucenikot {} e nedovolen {}.'.format(klas["ime: "],klas['prosek']))
        uspeh ="ne dovolen"
    return uspeh
klas['uspeh'] =uspeh(klas)
print(klas)