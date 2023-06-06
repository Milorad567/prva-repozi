"""Напишете програма која ќе прочита страни на правоаголник и квадрат, да се пресмета плоштината
 и да се провери дали збирот на плоштините е деллив со 2,3 или 5"""

a=int(input("Vnesete ja ednata strana na pravoagolnikot: "))
b=int(input("Vnesete ja drugata strana na pravoagolnikot: "))
P=a*b
print(f"Plostinata na pravoagolnikot e: {P} ")
a1=int(input("Vnesete ja  stranata na kvadratot: "))
P1=a1*a1
zbir=P+P1
print(f"Plostinata na kvadratot e: {P1} ")
zbir=0

print(f"Zbirot na plostinite {P} i {P1} iznesuva:{zbir} ")
if zbir%2==0:
    print(f"Zbirot na plostinite {P} i {P1} e delliv so 2: ")
else:
     print(f"Zbirot na plostinite {P} i {P1} ne e delliv so 2: ")
if zbir%3==0:
    print(f"Zbirot na plostinite {P} i {P1} e delliv so 3: ")
else:
     print(f"Zbirot na plostinite {P} i {P1} ne e delliv so 3: ")
if zbir%5==0:
    print(f"Zbirot na plostinite {P} i {P1} e delliv so 5: ")
else:
     print(f"Zbirot na plostinite {P} i {P1} ne e delliv so 5: ")