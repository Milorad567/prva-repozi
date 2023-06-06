from banka.transakciska_smetka import TransakcijaSmetka
smetka1 = TransakcijaSmetka("Trajce", "Trajcev", "1233456", "Skopje", "000123", 15000, "30.05.2023")
smetka1.povleci_pari(20000)