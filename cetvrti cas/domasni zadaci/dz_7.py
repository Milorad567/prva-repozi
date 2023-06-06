"""Напишете програма која ќе прочита големина на агли во триаголник, да се провери дали може да се формира триаголник со тие агли
(збирот мора да биде 180) и ако може да се формира триаголник
 да се провери каков триаголник може да се формира"""

broj1=int(input("Vnesete golemina na agol: "))
broj2=int(input("Vnesete golemina na vtor agol: "))
broj3=int(input("Vnesetegoleminana tret agol: "))
zbir=0
zbir=broj1+broj2+broj3==180
print(f"zbirot na aglite e {zbir} ")
if broj1+broj2+broj3 ==180:
    print(f"zbirot na aglite {broj1}, {broj2} i {broj3} moze da formira triagolnik. ")
else:
    print(f"zbirot na aglite {broj1}, {broj2} i {broj3} ne moze da formira triagolnik. ")
if broj1==broj2==broj3:
    print("Triagolnikot e ramnostran. ")
else:
    print("Triagolnikot ne e ramnostran. ")
if broj1==broj2:
    print("Triagolnikot e ramnkrak. ")
else:
    print("Triagolnikot ne e ramnokrak" )
if broj1>broj2>broj3:
    print("Triagolnikot e raznostran. ")
elif broj1<broj2>broj3:
    print("Triagolnikot e raznostran. ")
elif broj1>broj2<broj3:
    print("Triagolnikot e raznostran. ")
elif broj1<broj2<broj3:
    print("Triagolnikot e raznostran. ")
else:
    print("Triagolnikot ne e raznostran. ")
