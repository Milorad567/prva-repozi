"""Вежба 15: Напиши програма што ќе бара од корисникот да внесе реченица. Раздели ја реченицата на зборови и зачувај ги во листа.
Потоа, испечати го бројот на зборови кои започнуваат со голема буква."""
vasa_recenica=[]
recenica=input("Vnesete ja vasata recenica:  ")
print(recenica)
vasa_recenica=recenica.split(" ")
print(vasa_recenica)
for golema_prva in vasa_recenica:
    print(golema_prva.capitalize())