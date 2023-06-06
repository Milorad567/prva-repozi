"""Вежба 8: Напиши програма за пребројување и печатење на бројот на непарни броеви во листа."""
lista=[]
broj=1
for i in range(8):
    broj = int(input(f"Vnesete go vasiot {i} broj: "))
    lista.append(broj)
print(lista)
print((f"Dolzinata na listata e: {len(lista)}"))
neparni_broevi=[]
for broj in lista:
    if broj % 2 == 1:
        neparni_broevi.append(broj)
print(f"Neparni broevi od listata se:{neparni_broevi} ")