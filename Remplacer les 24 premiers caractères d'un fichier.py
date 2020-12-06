"""
Creer un programme python permettant de remplacer les 24 premiers caractéres d'un
fichier par la phrase : "Le contenu de ce fichier a été modifié".
C:/Users/Ali_s/PycharmProjects/Cour python/monFichier.txt
"""
file = open("//monFichier.txt", "r")
content = file.read()
content2 = "Le contenu de ce fichier a été mofifié ...."+ content[24:]
file.close()
file = open("//monFichier.txt", "w")
file.write(content2)
file.close()