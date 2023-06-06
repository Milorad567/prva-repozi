"""2. Da se kreira klasa Pravoagolnik so konstrukot sto ke gi prima 2te strani na pravogolniot. Da se kreiraat metodi koi ke ja presmetuvaat plostinata i perimetarot na pravogolnik. Da se kreira objekt
 i da se presmeta plostinata i perimetarot na pravogoalnikot"""

 
class Pravolagolnik:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def presmetaj_plostina(self):
        return self.a * self.b
    def presmetaj_perimetar(self):
        return 2 * (self.a + self.b)
pravoagolnik = Pravolagolnik(2, 8)
plostina = pravoagolnik.presmetaj_plostina()
perimetar = pravoagolnik.presmetaj_perimetar()
print("Ploštinata na pravoagolnikot e:", plostina, "a perimetarot na pravoagolnikot e", perimetar)







