"""
    Ecrire un programme en python qui renvoie toutes les listes
    obtenues en permutant les termes d'une liste données.
    """
import intertools
L = [1,2,3,4,5]
permutations = intertools.permutations(L)
L = list(permutations)
print(L)
