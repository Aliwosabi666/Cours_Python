"""
    Ecrire un programme en python calculant la somme des nombres pairs de 0 à 100
    et la somme des nombres impairs de  1 à 101
"""
    
n = int(input("Enter un entier n:"))
sommePaire = 0
somImpaire = 0
for i in range(0 , n+2):
    if(i%2== 0):
        sommePaire = sommePaire + i
    else:
        somImpaire = somImpaire + i
print("La somme des entiers pairs de 1 à n est = ",sommePaire)
print("La somme des entiers impairs de 1 à n est = ",somImpaire)

