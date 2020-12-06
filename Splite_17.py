"""

    comment créer un programme Python qui demande
    à l'utilisateur de taper un texte sous forme d'une chain de
    caractères et de lui renvoyer tous les mots du texte
    qui commencent avec la lettre a
    """
s = input("Taper une chaine de caracter s:")
s = s.split()
for x in s:
    if(x[0] == 'a'):
        print("Le mot ", x , "commece par la letter 'a'")
    
