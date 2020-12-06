"""
    Créer une fonction en python nombreOccurences() qui s'applique à une liste
    L  et un élément x comme paramétres et qui retourne le nombre de fois ou
    l'élement x apparit dans la list L sans utiliser la fonction count()
"""
def nombreOccurences(L , a):
    i = 0
    for x in L:
        if(x == a):
            i = i + 1
    return i
L = [1,2,5,4,5,6,5]
print("Le nombre d'occurrences de 5 est :",nombreOccurences(L , 5))
        
        
    
