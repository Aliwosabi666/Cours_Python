"""
    programme que saisir 3 nombre x, y, z et de lui afficher leur maximum
"""
def max(x,y):
    if(x>=y):
        return x
    else:
        return  y
x = int(input("Entre le nombre x :"))
y = int(input("Entre le nombre y :"))
z = int(input("Entre le nombre z :"))

max_3 = max(x,max(y,z))
print("Le maximum des 3 nombre x, y, z est :",max_3)
