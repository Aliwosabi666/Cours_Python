"""
Ecrire un programme en python qui permet d'echanger la troisiéme ligne avec
la deuxiéme ligne.
"""
file = open("//monFichier.txt", "r")
L = file.readlines()
file.close()
x = ""
x = L[1]
L[1] = L[2]
L[2] = x
file = open("//monFichier.txt", "w")
file.writelines(L)
file.close()