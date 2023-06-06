godini=float(input("kolku imate godini"))

penzija=int(input("na kolku godini ke odite vo penzija"))

zbir=penzija-godini

print(f"ke rabotite uste {zbir} godini")

x="Daden e proizvolen pravoagolnik, vnesete gi dimenziite na stranite za da gi presmetame perimetarot L i plostinata P."
print(x)
a =float(input ("Vnesete ja dolzinata na strana a: "))
b =float(input ("Vnesete ja dolzinata na strana b: "))
L = 2*a+2*b
P = a*b
print(f"Perimetarot na pravoagolnikot e {L}cm.")
print(f"Plostinata na pravoagolnikot e {P}cm^2 ")
if L > P and L < 10:
    print("Perimetarot na pravoagolnikot e pogolem od plostinata i e pomal od 10")
elif L > 10 and L < 50:
    print("Perimetarot na pravoagolnikot e pogolem od plostinata, pogolem od 10 i pomal od 50 cm.")
elif L > 50:
    print("Perimetarot na pravoagolnikot e pogolem od plostinata i e pogolem od 50 cm.")
elif P > L and P < 10:
    print("Plostinata na pravoagolnikot e pogolema od perimetarot i e pomala od 10")
elif P > 10 and P < 50:
    print("Plostinata na pravoagolnikot e pogolema od perimetarot, pogolema od 10 i pomala od 50 cm.")
else:
    print("Plostinata na pravoagolnikot e pogolema od perimetarot i e pogolema od 50 cm.")