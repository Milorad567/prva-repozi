
from lice import Lice
class TransakcijaSmetka(Lice):
    
    def __init__(self, ime, prezime, embg, mesto_na_ziveenje, br_na_smetka, suma, datum_na_kreiranje):
        super().__init__(ime, prezime, embg, mesto_na_ziveenje)
        self.br_na_smetka = br_na_smetka
        self.suma = suma
        self.datum_na_kreiranje = datum_na_kreiranje
        
    def povleci_pari(self, suma_za_povlecuvanje):
        if suma_za_povlecuvanje > self.suma:
            print("ne mozete da povlecete poveke od toa sto imate")
        else:
            self.suma = self.suma - suma_za_povlecuvanje
            print("Uspesno povleceni sredstva")
            print(f"Na vasata smetka ostanuvaat {self.suma}")
    
    def dodadi_pari(self, suma_za_dodavanje):
        self.suma = self.suma + suma_za_dodavanje
        print("Uspesno dodadeni sredstva")
        print(f"Na vasata smetka ostanuvaat {self.suma}")