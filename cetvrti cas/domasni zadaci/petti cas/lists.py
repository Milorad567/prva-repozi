#prva lista=list()
#vtora lista=[]


#print(lista_ovosje)
#print(lista_ovosje[-2])
#print(lista_ovosje[0:2])
#lista_ovosje=["jabolka","krusi","banani","citroni","cresi"]

#print(lista_ovosje[0:2:4])

#broevi=[0,1,2,3,4,5,6,7,8,9,10]
#print(broevi[0:8:10])

#for ovosje in lista_ovosje:
   # print(ovosje.upper())
#lista_ovosje=["jabolka","krusi","banani","citroni","cresi"]   
#lista_ovosje.append(12)

#lista_ovosje.insert(3,"nov podatok so insert")
#print(lista_ovosje)

#lista_ovosje.remove("jabolka")
#print(lista_ovosje)

#lista_ovosje.pop(3)
#print(lista_ovosje)

#print(len(lista_ovosje))

#print(lista_ovosje.index("banani"))

#print(lista_ovosje.count("banani"))

broevi=[0,1,2,3,4,5,6,7,8,9,10]
broevi.sort(reverse=True)
#lista_ovosje.sort(reverse=True)

print(max(broevi))
print(min(broevi))
print(sum(broevi))

zbor="lele sto napravivme"
lista_string=zbor.split(" ")
print(lista_string)

nov_zbor=" ".join(lista_string)
print(nov_zbor)