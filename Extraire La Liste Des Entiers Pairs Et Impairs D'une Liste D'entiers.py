"""

    Ecrire un  programme python qui permet d'extraire la liste des entiere paires
    et la liste des entiers impiars d'une liste de nombres
    """
def extract(L):
    pair = []
    impaire = []
    for x in L:
        if(x%2 == 0):
            pair.append(x)
        else:
            impaire.append(x)
        
        print("La liste des entire pairs est :",pair)
        print("-----------------------------------------")
        print("La liste des entire impaire est :",impaire)
#Test l'algorithme
L = [2,3,4,5,6,7,8,9,10]
print(extract(L))

