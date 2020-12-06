"""
1) Définir une classe cercle permettant de créer une cercle c(O,r) de centre
O(a,b) et de rayon r à l'aide du constructeur
        def __init__(self,a,b,r):
            self.a= a
            self.b= b
            self.c= c
2)Définir une méthode Surface() de la classe qui permet de calculer la surface
du cercle
3)Définir une méthode Perimetre() de la classe qui permet de calculer le périmétre
 du cercle
4)Définir une méthode testAppartenance()  de la classe qui permet de tester si un
point A(x,y) appartient ou non au cercle C(O,r)
"""
from math import *
class Cercle:
    def __init__(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
    def perimetre(self):
        return 2*pi*self.r
    def Surface(self):
        return pi*self.r**2
    def testAppartenance(self, x , y):
        return (x-self.a)**2 + (y-self.b)**2 == self.r**2

monCercle = Cercle(0,0,1)
print("Le perimetre du cercle est :",monCercle.perimetre())
print("Le Surface du cercle est :",monCercle.Surface())
print("Le Test Appartenance du Point A :",monCercle.testAppartenance(0,1))
