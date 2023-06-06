zbir = 0
while True:
    broj = int(input('Vnesete broj koj e 100 < x > 500: '))
    print(f'broj: {broj}')
    zbir = zbir + broj
    print(f'zbir: {zbir}')
    if broj < 100 or broj > 500:
        break