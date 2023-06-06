""" Da se napravi funkcija koja ke prima broj kako parametar i da pecati dali brojot e paren ili ne paren"""

def proverka(n):
    if n%2==0:
        print(n,'e paren broj!')
    else:
        print(n,'e neparen broj!')
n=int(input("Vnesi broj: "))
proverka(n)
