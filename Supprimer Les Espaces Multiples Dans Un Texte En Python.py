"""
    Ecrire un programme en python permettant de supprimer les espaces
    multiples dans une chaine s
    """
s = "Exemple de     texte   avec     des espaces    multiple"
L = s.split()
newText = ""
for x in L:
    newText = newText + x + " " #if you wonna espace and if not you must use this
    #loi                     newText = newText + x       
print(newText)
