"""Вежба 10: Напиши програма што ќе бара од корисникот да внесува серија на броеви сè додека не внесе '0'.
 Зачувај ги броевите во листа и потоа испечати ја листата."""
lista=[]
broj=1
while True:
    broj = int(input("Vnesete broj {}: "))
    lista.append(broj)
    if broj ==0:
        break
print(lista)