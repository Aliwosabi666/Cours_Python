"""
                Class Compte Bancaire:
1) creer une class python nommée CompteBancaire qui représente une compte bancaire,
ayant pour attributes : numeroCompte (type numérique) , nom(nom du propriétaire du
compte du type chaine), solde.
2) Créer un constructeur ayant comme paramétres : numeroCompte, nom , solde.
3) Créer une méthode Versement() qui gére les versements.
4) Créer une méthode Retrait() qui gére les retraits.
5)Créer une méthode Agios() permettant d'appliquer les agois à un pourcentage de 5%
du solde.
6) Créer une méthode afficher() permettant d'afficher les détalis sur le compte
7) Créer le code complet de la classe CompteBancaire.
"""
#1)
class CompteBancaire:
#2)
    def __init__(self, numeroCompte,nomPrenom, solde ):
        self.numeroCompte = numeroCompte
        self.nomPrenom = nomPrenom
        self.solde = solde
#3)
    def Versement(self, Somme):
        self.solde = self.solde + Somme

#4)
    def Retrait(self, Somme):
        if(Somme > self.solde):
            print("Solde insuffisant !")
        else:
            self.solde = self.solde - Somme

#5)
    def Agios(self):
        self.solde = self.solde*95/100


newCompte = CompteBancaire(124423235235,"Ali Wsb",2600)
#3)#newCompte.Versement(300)
#4)newCompte.Retrait(300)
newCompte.Agios()
print("Le numéro de compte est: ", newCompte.numeroCompte)
print("Nom du propriétaire : ", newCompte.nomPrenom)
print("Solde sauf erreur ou omission: ", newCompte.solde)

