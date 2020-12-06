"""
    https://www.youtube.com/watch?v=oxD3NZe_1HU&list=PLh-rUZWaw76H854IJM3NXVGWbE8o_cuw7&index=18
    Ecrire un programme en langage python qui demande à l'utilisateur de saisir
    le nom d'un fichier et de lui renvoyer son extension.exapmle si l'utilisateur
    saisie courpython.pdf, le programme lui renvoie le message 'l'extension du
    fichier est .pdf'

    """
fichier = input("Saisir le nom du fichier avec son extension: ")
L = fichier.split(".")
print("l'extension du fichier est ", "." + L[-1])
