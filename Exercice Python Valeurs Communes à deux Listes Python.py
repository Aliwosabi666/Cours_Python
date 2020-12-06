"""
     Ecrire une fonction en python qui permet de comparer deux listes et
     de nous indiquer si ces deux listes ont une valeur commune ou non

     """
def valeurCommune(L1,L2):
    compteur = 0
    for x in L1:
        if(x in L2):
            compteur = compteur + 1
            if(compteur > 0):
                return True
            else:
                return False
L1 = [2,3,4,5,70]
L2 = [2,30,6,80,70]
print(valeurCommune(L1,L2))

            
