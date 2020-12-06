# test_debugger3.py
# python 3

def carre(nb):
    resultat = nb*nb
    return resultat

a = 1
print(a)
while a < 5:
    a += 1
    print(carre(a))
print('Fin du programme')

