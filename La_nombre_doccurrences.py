"""
       La nombre d'occurrences
"""

s = "ali wosabi"
n = len(s)
L = []
for i in range(0,n):
    if s[i] not in L:
        L.append(s[i])
        print("Le caractere ","'",s[i],"'","Figure",s.count(s[i]),"Fois dans la chaoine s")
    


