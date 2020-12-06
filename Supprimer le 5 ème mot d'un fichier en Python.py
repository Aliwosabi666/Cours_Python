"""
Ecrire un programme pyhon qui supprime le 5eme mot d'un fichier.

"""
file = open("//monFichier.txt", "r")
content = file.read()
content = content.split()
content.pop(4)
s = " "
s = " ".join(content)
file.close()
file = open("//monFichier.txt", "w")
file.write(s)
file.close()