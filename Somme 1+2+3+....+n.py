"""

Ecrire un programme en python que demande à l'utilisateur de saisire un nombre entire n et de lui
afficher la valeur de la somme 1+2+3+4+......+n=

"""
s = 0
n = int(input("Entre ne nombre n:"))
for i in range(0,n+1):
    s = s + i
    print ("La Somme 1+2+3+....+n=",s)

