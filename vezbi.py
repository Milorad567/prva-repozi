"""x="Daden e proizvolen pravoagolnik, vnesete gi dimenziite na stranite za da gi presmetame perimetarot L i plostinata P."
print(x)
a=float(input("Vnesete ja dolzinata na stranata a:"))
b=float(input("Vneseteja dolzinata na stranata b:"))
L=2*a+2*b
P=a*b
print(f"Perimetarot na pravoagolnikot e {L} cm")
print(f"Plostinata na pravoagolnikot e {P} cm^2")
if L>P and L<10:
    print("Perimetarot na pravoagolnikot e pogolem od plostinata i e pomal od 10.")
elif L<10 and L<50:
    print("Perimetarot e pogolem od plostinata pogolem od 10 a e pomal od 50.")
elif L>50:
    print("Perimetarot e pogolem od plostinata i pogolem od 50")
elif P>L and P<10:
    print("Plostinata e pogolema od perimetarot i e pomala od 10")
elif P>10 and P<50:
    print("Plostinata e pogolema od perimetarot, pogolem od 10 i e pomal od 50")
else:
    print("Plostinata e pogolema od perimetarot i e pogolema od 50")"""

ime_prezime = "Milorad Atanasov"

print(ime_prezime)
x_golemo=ime_prezime.upper()
print(x_golemo)

x_malo=ime_prezime.lower()
print(x_malo)

x_prva_golema=ime_prezime.capitalize()
print(x_prva_golema)

x_br_karakteri=ime_prezime.count("a")
print(x_br_karakteri)

x_dolzina=len(ime_prezime)
print(x_dolzina)

x_mesto=ime_prezime.index("l")
print(x_mesto)


