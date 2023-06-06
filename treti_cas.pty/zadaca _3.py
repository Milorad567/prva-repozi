a = int(input("Внеси ја ширинат на правоаголникот:"))
b = int(input("Внеси ја должината на правоаголникот:"))
#perimetar
perimetar = 2*a+2*b
plostina= a*b
print(f"Периметарот на правоаголникот е {perimetar}")
print(f"Плоштината на правоаголникот е {plostina}")
if perimetar == plostina:
    print(f"Периметарот и плоштината се еднакви")
else:
    if perimetar > plostina:
        print(f"Периметарот е поголем од  плоштината")
    else:
        print(f"Плоштината е поголема од  периметарот")
    