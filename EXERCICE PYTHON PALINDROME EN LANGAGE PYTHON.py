"""

    Ecrire un programme qui demende à l'utilisateur de saisir un mot et de lui
    renvoyer s'il s'agit d'un palindrome ou non
     note : palindrome like laval ,radar , sos

"""

s = input("Tapez un mot : ")
inv = s[::-1]
if(s == inv):
    print("le mot ", s ,"est un palindrome:")
else:
    print("le mot ", s ,"n'est pas un palindrome:")
    
    

