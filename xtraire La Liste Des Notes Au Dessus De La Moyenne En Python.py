"""
    Etant donnée la liste des notes des éléves : notes=[12,4,14,11,18,13,7
    ,10,5,9,15,8,14,16].Ecrire un programme python qui permet d'extraire de
    cette liste et creer une autre liste qui contient uniquement les notes
    au-desssus de la moyenne (les notes >= 10)
    """
notes = [12,4,14,11,18,13,7,10,5,9,15,8,14,16]
moyenne = []
for x in notes:
    if(x>= 10):
        moyenne.append(x)
print("la liste des notes au dessus de la moyenne est :",moyenne)
