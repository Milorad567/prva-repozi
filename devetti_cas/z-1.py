"""1. Da se kreira klasa Lice, so konstrukto koj ke treba da gi prima slednive parametri, Ime, prezime, godini, email, mesto na ziveenje.
Kreirajte 3 lica( objekti)i ispecatete gi iminjata i godinite na sekoe od licata"""


class Lice:

    def __init__(self, ime, prezime, godini, email, mesto_na_ziveenje):
        self.ime = ime
        self.prezime = prezime
        self.godini = godini
        self.email = email
        self.mesto_na_ziveenje = mesto_na_ziveenje



Lice1 = Lice("Milorad", "Atanasov", "48", "milorad.atanasov@....mk", "Vinica")
print(f"Imeto na prvoto lice e: {Lice1.ime}")
print(f"Godinite na prvoto lice se= {Lice1.godini}")

Lice2  = Lice("Aleksandar", "Atanasov", 21, "almail@...mk", "Ljubljana")
print(f"Imeto na vtoroto lice e: {Lice2.ime}")
print(f"Godinite na vtoroto lice se= {Lice2.godini}")

Lice3  = Lice("Ognen", "Atanasov", 15, "ogmail@...mk", "Vinica")
print(f"Imeto na tretoto lice e: {Lice3.ime}")
print(f"Godinite na tretoto lice se= {Lice3.godini}")
