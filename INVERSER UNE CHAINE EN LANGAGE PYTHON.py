"""

    Ecrire un programme qui demende à l'utilisateur de saisir un mot et de lui
    renvoyer son inverse.Exemaple si l'utilisateur saisi le mot python le
    programme lui revoie nohtyp

"""

s = input("Tapez un mot : ")
inv = s[::-1]   
print("l'invere du mot ", s ,"est:" , inv)



"""
s = input("Tapez un mot : ")
inv =""
for x in s:
     inv = x + inv    
print("l'invere du mot ", s ,"est:" , inv)
"""
