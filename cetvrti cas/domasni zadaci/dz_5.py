"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати производот на броевите, 
да се провери дали резултатот е парен или не парен."""

broj1=int(input("Vnesete eden broj:" ))
broj2=int(input("Vnesete drug broj:"))
Proizvod=1
Proizvod=broj1*broj2
print(f"Proizvodot e: {Proizvod}.")
if Proizvod%2==0:
    print(f"proizvodot na brojot {broj1} i brojot {broj2} e paren broj")
else:
    print(f"proizvodot na brojot {broj1} i brojot {broj2} e neparen broj")