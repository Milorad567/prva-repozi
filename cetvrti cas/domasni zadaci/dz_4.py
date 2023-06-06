"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот на броевите помеѓу нив што се делливи со 4."""

broj1=int(input("Vnesete eden broj"))
broj2=int(input("Vnesete drug broj"))
zbir=0
zbir=broj1+broj2
print(f"zbir: {zbir}. ")
if zbir%4==0:
    print(f"zbirot na {broj1} i {broj2} e delliv so 4. ")
else:
    print(f"zbirot na {broj1} i {broj2} ne e delliv so 4. ")
