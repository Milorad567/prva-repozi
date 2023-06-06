"""Вежба 11: Напиши програма што ќе бара од корисникот да внесе реченица. Раздели ја реченицата на зборови и зачувај ги во листа. 
Потоа, испечати го должината на секој збор во листата."""

recenica=input(f"Vnesete ja vasata recenica:  ")
print(recenica)

vasa_recenica=recenica.split(" ")
print(vasa_recenica)
print (f"Dolzinata na prviot zbor e: {len(vasa_recenica[0])}")
print (f"Dolzinata na vtoriot zbor e: {len(vasa_recenica[1])}")
print (f"Dolzinata na tretiot zbor e: {len(vasa_recenica[2])}")
print (f"Dolzinata na cetvrtiot zbor e: {len(vasa_recenica[3])}")
print (f"Dolzinata na petiot zbor e: {len(vasa_recenica[-5])}")
print (f"Dolzinata na sestiot zbor e: {len(vasa_recenica[-4])}")
print (f"Dolzinata na sedmiiot zbor e: {len(vasa_recenica[-3])}")
print (f"Dolzinata na osmiot zbor e: {len(vasa_recenica[-2])}")
print (f"Dolzinata na devetiot zbor e: {len(vasa_recenica[-1])}")


