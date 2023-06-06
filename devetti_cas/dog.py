
class Dog:

    def __init__(self, ime, rasa, pol, godini, boja):
        self.ime = ime
        self.rasa = rasa
        self.pol = pol
        self.godini = godini
        self.boja = boja

    def get_name(self):
        return self.ime
    
    def set_name(self, novo_ime):
        self.ime = novo_ime
    
    def presmetaj_godina_na_ragjanje(self):
        godina = 2023 - self.godini
        return godina
    



kuce = Dog("ime1", "rasa1", "maski", 6, "crno")


godina_ragjanje = kuce.presmetaj_godina_na_ragjanje()
print(f"kuceto {kuce.get_name()} e rodeno vo {godina_ragjanje}")

