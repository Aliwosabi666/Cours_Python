s = "python est un langage de programmation"
L = s.split()
n = len(L)
premier  = L[0]
dernier = L[n-1]
L.pop()
L.pop(0)
s1 = " ".join(L)
s2 = dernier + "  "+ s1 +"  "+premier
print(s2)
