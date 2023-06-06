"""Da se kreira lista vo koja korisnikot ke moze da dodade 5 broevi.
Da se pomina neiz celata lista i da se ispecatat samo parnite broevi sto se vneseni"""

lista = [2, 4, 6, 8, 10]

for i in range(5):
    broj = int(input('Vnesete go vasiot {} broj: '.format(i+1)))
    lista.append(broj)
print('Listata so site broevi: ', lista)

lista = [2, 5, 7, 9, 13]
parni_broevi = []
for broj in lista:
    if broj % 2 == 0:
        parni_broevi.append(broj)
print('Parni broevi od listata se: ',parni_broevi)