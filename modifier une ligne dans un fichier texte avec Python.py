"""
Ecrire un programme en python qui permet de remplacer la 3eme ligne d'une
fichier texte, par la phrase "désolé! le conteun de cette ligne a été changé
C:/Users/Ali_s\PycharmProjects/Cour python/monFichier.txt
"""
file = open("//monFichier.txt")
lignes = file.readlines()
file.close()
lignes[2] = "Désolé! le conteun de cette ligne a été changé!\n"
file = open("//monFichier.txt", "w")
file.writelines(lignes)
file.close()