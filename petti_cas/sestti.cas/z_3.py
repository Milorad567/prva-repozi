""" Da se napravat funkcii koi ke primaat 2 parametri i ke presmetuvaat plostina i perimetar na pravoagolnik"""

def pravoagolnik(a,b):
    L=2*(a+b)
    P=a*b
    print("Perimetarot e: ",L)
    print("Plostinata e: ",P)
a=int(input("Vnesi ja stranata A na pravoagolnikot: "))
b=int(input("Vnesi ja stranata B na pravoagolnikot: "))
pravoagolnik(a,b)