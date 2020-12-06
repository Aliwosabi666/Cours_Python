"""
       Erire un programme python qui permet de
       Supprimer les elements dupliques d'une liste
       """

def removeDuplicate(l):
    unique = []
    for x in l:
        if x not in unique:
            unique.append(x)
    return unique
print(removeDuplicate([2,13,13,13,2,6,6,7,7]))

        

