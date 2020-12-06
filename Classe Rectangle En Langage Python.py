"""

    1)Ecrire une classe Rectangle en langage python permettant de construire une
        constriuire un rectangle dotée d'attributs longueur et largeur.
    2)Créer une méthode perimetre() permettant de calculer le périmétre du
        rectangel et une methode surface() permettant de calculer la surface
        du rectangle.
    3)Créer une classe fille parallelepipende héritant de la classe Rectangle
         Volume() permettant de calculer le volume du parallélépipéde.
"""
class Rectangle:
     def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
monRectangle = Rectangle()
print("La longueur de mon rectangle est :",monRectangle.longueur)
print("La longueur de mon rectangle est :",monRectangle.largeur)

        

