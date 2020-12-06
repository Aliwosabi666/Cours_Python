"""
    Créez une fonction python, appelée nombreDivisibles, qui s'applique à une
    Liste de nombres et un entier n, et qui renvoie le nombre d'éléments de la
    liste qui sont divisible par n.
    """
def nombreDiv(L,n):
    i = 0
    for x in L:
        if(x%n == 0):
            i = i + 1
    return i
#Test de l'algorithme
n = 3
L = [12,5,7,14,17,21]
print("Le nombre d'élément de L qui sont divisible par ",n,"est",nombreDiv(L,n))
            
    
    
