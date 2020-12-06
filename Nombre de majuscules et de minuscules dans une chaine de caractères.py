"""
Ecrire un programme python qui demande à l'utilisateur de saisire un texte sous
forme de chaines de caractéres et qui doit lui afficher le nombre de minuscules
et de majuscules contenu dans le texte saisi.
"""
s = "Langage Python"
M = 0
m = 0
for x in s:
    if(x.isupper()):
        M = M + 1
    else:
        m = m + 1
print("Le nombre de majuscules de s est :", M)
print("Le nombre de minuscules de s est :", m)
