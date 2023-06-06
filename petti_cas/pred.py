licnost = { "ime":"nenad",
            "prezime":"ristov", 
            "email":"ristovn18@gmail.com",
            "tel_broj":000,
            "pol":"maski",
            # index : value,
            0:"vrednost"
    }

#print(licnost["email"])
#print(licnost["ime"])

# *** CIKLUSI ZA MINUVANJE NIZ INDEXI ***
"""for i in licnost:#samo niz indexi
    #print(i)
    print(licnost[i])

for index in licnost.keys(): # licnost.keys() -> lista od indexi
    #print(i)
    print(licnost[i])"""

"""for value in licnost.values(): # licnost.values() -> lista od vrednosti
    print(value)"""

licnost={"ime":"Milorad",
         "prezime":"Atanasov",
         "email":"milorad.atanasov5@gmail.com",
         "tel_broj":"001"
         }
print(licnost["email"])
print(licnost["ime"])
licnost.update({"boja na oci":"kafeavi"})

licnost.pop("ime")
del licnost["prezime"]
print(licnost)