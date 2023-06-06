"""Вежба 14: Напиши програма што ќе бара од корисникот да внесе реченица. Раздели ја реченицата на зборови и зачувај ги во листа.
Потоа, испечати ги зборовите во обратен редослед."""
vasa_recenica=[]
recenica=input("Vnesete ja vasata recenica:  ")

vasa_recenica=recenica.split(" ")
print(vasa_recenica)


vasa_recenica.sort(reverse=True)
print(vasa_recenica)

