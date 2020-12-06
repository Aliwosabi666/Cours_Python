"""
     Ecrire un programme python qui permet de chercher le mot le plus long
     sur une chaine s
     """
def motMax(s):
    L = s.split()
    mot = ""
    for x in L:
        if(len(mot)<len(x)):
            mot = x
    return mot
s = "python est un langage de programmation orienté objet"
print(motMax(s))
        
