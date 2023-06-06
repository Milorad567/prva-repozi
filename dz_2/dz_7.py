"""Вежба 7: Напиши програма за пребројување и печатење на бројот на парни броеви во листа."""
lista=[]
broj=1
for i in range(8):
    broj = int(input(f"Vnesete go vasiot {i} broj: "))
    lista.append(broj)
print(lista)
print((f"Dolzinata na listata e: {len(lista)}"))
parni_broevi=[]
for broj in lista:
    if broj % 2 == 0:
        parni_broevi.append(broj)
print(f"Parni broevi od listata se:{parni_broevi} ")



