x=input('Vnesi broj: ')
if int(x)>0:
    print('Brojot e pozitiven')
else:
     print('Brojot e negativen')

godini=input("Vnesi go brojot na godini: ")
if int(godini)>18:
    print('Vie ste polnoleten! ')
else:
    print('Vie ste maloleten!')

    a = int(input("Внеси ја ширинат на правоаголникот:"))
b = int(input("Внеси ја должината на правоаголникот:"))
#perimetar
perimetar = 2*a+2*b
plostina= a*b
print(f"Периметарот на правоаголникот е {perimetar}")
print(f"Плоштината на правоаголникот е {plostina}")
if perimetar == plostina:
    print(f"Периметарот и плоштината се еднакви")
else:
    if perimetar > plostina:
        print(f"Периметарот е поголем од  плоштината")
    else:
        print(f"Плоштината е поголема од  периметарот")

        ime = input ( "Vnesete go vaseto ume: ")
print (f"Zdravo, {ime}")
BrNaPovtoruvanja = ime.count ("a")
print (f"Vo vasheto ime samoglaskata 'a' se pojavuva {BrNaPovtoruvanja} pati")
BrNaPovtoruvanja = ime.count ("e")
print (f"Vo vasheto ime samoglaskata 'e' se pojavuva {BrNaPovtoruvanja} pati")
BrNaPovtoruvanja = ime.count ("i")
print (f"Vo vasheto ime samoglaskata 'i' se pojavuva {BrNaPovtoruvanja} pati")
BrNaPovtoruvanja = ime.count ("o")
print (f"Vo vasheto ime samoglaskata 'o' se pojavuva {BrNaPovtoruvanja} pati")
BrNaPovtoruvanja = ime.count ("u")
print (f"Vo vasheto ime samoglaskata 'u' se pojavuva {BrNaPovtoruvanja} pati")