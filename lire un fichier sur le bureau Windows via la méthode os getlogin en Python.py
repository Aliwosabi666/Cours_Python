"""
Ecrire un programme python qui permet de lire un fichier existant sur le bureau
nommé monfichier.txt on doit préalablement récupérer le nom d'utilisateur via la
commande os.getlogin()
"""
import os
nomUtilisateur = os.getlogin()
file = open("C:/Users/"+ nomUtilisateur +"/PycharmProjects/Cour python/test.txt")
content = file.read()
print(content)