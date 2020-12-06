"""
Créer une fonction python nommée toutEnMajuscule() qui permet de transformer une
liste de chaines en une autre liste constituée de chaines en majuscule
"""
def toutEnMajuscule(L):
    L_Majuscules = []
    for s in L:
        s = s.upper()
        L_Majuscules.append(s)
    return L_Majuscules
L = ["Python","Java","Mysql","django"]
print(toutEnMajuscule(L))
