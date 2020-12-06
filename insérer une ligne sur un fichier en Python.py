"""
Ecrire un programme en python qui permet d'insérer à une position donnée sur
un fichier texte, la ligne : "Cette ligne a été insérée via un code python!"
"""
file = open("//monFichier.txt", "r")
L = file.readlines()
file.close()
s = "Cette ligne a été insérée via un code python \n"
L.insert(2 , s)
file = open("//monFichier.txt", "w")
file.writelines(L)
file.close()