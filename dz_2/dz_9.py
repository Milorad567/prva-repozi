"""Вежба 9: Напиши програма што ќе бара од корисникот да внесе 5 броеви и да ги зачува во листа. Потоа, испечати го збирот на тие броеви."""

lista=[]
broj=1
for i in range(5):
    broj = int(input(f"Vnesete go vasiot {i} broj: "))
    lista.append(broj)
print(lista)
print(f"Zbirot na broevite od lista e:{sum(lista)}")