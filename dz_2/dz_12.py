"""Вежба 12: Напиши програма што ќе бара од корисникот да внесе серија на броеви. 
Зачувај ги броевите во листа и потоа испечати го најголемиот број во листата."""

serija_na_broevi=[]
broj=1
for i in range(8):
    broj = int(input(f"Vnesete go vasiot {i} broj: "))
    serija_na_broevi.append(broj)
print(serija_na_broevi)
print(max(serija_na_broevi))