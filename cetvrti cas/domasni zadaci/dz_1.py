"""Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот, разликата, производот и количникот на двата броја.
 Споредете кој резултат е поголем, збирот или производот"""

broj1=int(input("Внесете го првиот број"))
broj2=int(input("Внесете го вториот број"))

zbir=broj1+broj2
razlika=broj2-broj1
kolicnik=broj1/broj2
proizvod=broj1*broj2
print(f"zbirot na broevite {broj1} i {broj2} e {zbir}")
print(f"razlikata megu broevite {broj2} i {broj1} e {razlika}")
print(f"kolicnikot na broevite {broj2} i {broj1} e {kolicnik}")
print(f"proizvodot na broevite {broj1} i {broj2} e {proizvod}")

if zbir==proizvod:
        print(f"zbirot i proizvodot se isti")

if proizvod > zbir:
        print(f"Производот е поголем од  збирот")
else:
        print(f"Збирот е поголем од производот")