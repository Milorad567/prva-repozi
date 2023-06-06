"""Вежба 16: Напиши програма што ќе бара од корисникот да внесе серија на броеви.
Зачувај ги броевите во листа и потоа испечати само парните броеви од листата."""
serija_na_broevi=[]
broj=1
for i in range(8):
    broj = int(input(f"Vnesete go vasiot {i} broj: "))
    serija_na_broevi.append(broj)
print(serija_na_broevi)
parni_broevi=[]
for broj in serija_na_broevi:
    if broj % 2 == 0:
        parni_broevi.append(broj)
print(f"Parni broevi od listata se:{parni_broevi} ")