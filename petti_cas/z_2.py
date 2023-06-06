"""Da se kreira tuple od 10 broevi sto ke gi vnese korisnikot. parnite broevi da se dodadat vo eden tuple a ne parnite vo drug tuple"""

#zadaca2
nov_tuple=()
lista_broevi=list(nov_tuple )
for i in range(10):
    nov_broj=int(input('Vnesi broj: '))
    lista_broevi.append(nov_broj)
nov_tuple=tuple(lista_broevi)
print(nov_tuple)
parni_tuple=()
neparni_tuple=()
p_lista=list(parni_tuple)
n_lista=list(neparni_tuple)
for broj in nov_tuple:
    if broj%2==0 :
        p_lista.append(broj)
    else:
        n_lista.append(broj)
parni_tuple=tuple(p_lista)
neparni_tuple=tuple(n_lista)
print("Parni broevi: ",parni_tuple)
print("Neparni broevi: ",neparni_tuple)

