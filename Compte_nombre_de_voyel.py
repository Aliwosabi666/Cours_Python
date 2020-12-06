s = "anticonstitutionellement"
n = len(s)
nbVoyelle = 0
for i in range(0,n):
    if(s[i] in ['a','e','o','u','y','i']):
        nbVoyelle = nbVoyelle + 1
print("La chaine 's' posséde ",nbVoyelle ,"Voyelle")
        
