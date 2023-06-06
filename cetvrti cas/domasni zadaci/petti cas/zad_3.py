"""Da se kreira lista so 5 broevi, da se dodadat 3 novi broevi sto ke bidat vneseni od korisnikot.
da se ispecatat poslednite elementite od index 3 do kraj"""
lista_broevi=[10,20,30,40,50]
print(lista_broevi)
novi_broevi=input("Vnesete novi tri broja")
lista_broevi.append(novi_broevi)
print(lista_broevi)
print(lista_broevi [3:-1])

lista = [2, 5, 7, 9, 13]

for i in range(3):
    broj = int(input('Vnesete go vasiot {} broj: '.format(i+1)))
    lista.append(broj)

print('Lista so dodadenite tri broevi od strana na korisnikot: ',lista)
print('Poslednite 3 elementi od listata se: ', lista[-3])
