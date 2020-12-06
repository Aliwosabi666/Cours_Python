"""

    1)Ecrire une classe Rectangle en langage python permettant de construire une
        constriuire un rectangle dotée d'attributs longueur et largeur.
    2)Créer une méthode perimetre() permettant de calculer le périmétre du
        rectangel et une methode surface() permettant de calculer la surface
        du rectangle.
    3)Créer une classe fille parallelepipende héritant de la classe Rectangle
         Volume() permettant de calculer le volume du parallélépipéde.
"""

# 1)

class Rectangle:
    def _init_(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur


monRectangle = Rectangle(7, 5)
print("La longueur de mon rectangle est :", monRectangle.longueur)
print("La longueur de mon rectangle est :", monRectangle.largeur)







# 2)
"""
class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def Perimetre(self):
        return 2*(self.longueur+self.largeur)
    def Surface(self):
        return self.longueur*self.largeur



monRectangle = Rectangle(2, 3)
print("La Surface de mon rectangle est : ",monRectangle.Surface())
print("La Perimetre de mon rectangle est :", monRectangle.Perimetre())

"""



"""
# 3)

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

        def Perimetre(self):
            return 2 * (self.longueur + self.largeur)

        def Surface(self):
            return self.longueur * self.largeur

class parallelepipede(Rectangle):
    def __init__(self, longueur, largeur , hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur
    def Volume(self):
        return  self.longueur*self.largeur*self.hauteur

parallelepipede = parallelepipede(7, 5, 2)
print("Le volume de mon parallelepipede est :",parallelepipede.Volume())


"""