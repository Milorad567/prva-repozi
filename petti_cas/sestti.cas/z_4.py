"""Da se kreiraat 4 funkcii za osnovnite matematicki operacii koi primaat 2 broevi. Korisnikot da vnese dva broevi, 
da ja vnese operacijata sto saka da se izvrsi i da se povika soodvetnata funkcija"""

def zbir(x,y):
    print("Zbirot e: ",x+y)
def razlika(x,y):
    print('Razlikata e: ',x-y)
def mnozenje(x,y):
    print("Prozivodot e: ",x*y)
def delenje(x,y):
    print("Kolicnikot e: ",x/y)
x=int(input("Vnesi go prviot broj: "))
y=int(input("Vnesi go vtoriot broj: "))
operacija=input("Vnesi operacija koja sakas da se izvrsuva(sobiranje(+),odzemanje(-),mnozenje(*) ili delenje(/)   )")
if operacija=='sobiranje' or operacija=='+':
    zbir(x,y)
elif operacija=='odzemanje' or operacija=='-':
    razlika(x,y)
elif operacija=='mnozenje'or operacija=='*':
    mnozenje(x,y)
elif operacija=='delenje'or operacija=="/":
    delenje(x,y)







