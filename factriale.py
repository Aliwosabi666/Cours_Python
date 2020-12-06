"""

Ecrire un programme en python que demande à l'utilisateur de saisire un nombre entire n et de lui
afficher la valeur de la factorial 1+2+3+4+......+n=

"""
fact = 1
n = int(input("Entre ne nombre n:"))
for i in range(1,n+1):
    fact = fact * i
    print ("La Somme 1*2*3*....*n=",fact)

