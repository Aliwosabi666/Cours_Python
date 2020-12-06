# -*- coding: utf-8 -*-
# CompteBancaire.py

# définition de la classe Compte

class Compte:
   """Un exemple de classe :
   gestion d'un compte bancaire"""

   # définition de la méthode spéciale __init__
   def __init__(self, soldeInitial):
      """Initialisation du compte avec la valeur soldeInitial."""
      # assignation de l'attribut d'instance solde
      self.solde = float(soldeInitial)

   # définition de la méthode NouveauSolde()
   def NouveauSolde(self, somme):
      """Nouveau solde de compte avec la valeur somme."""
      self.solde = float(somme)

   # définition de la méthode Solde()
   def Solde(self):
      """Retourne le solde."""
      return self.solde

   # définition de la méthode Credit()
   def Credit(self, somme):
      """Crédite le compte de la valeur somme. Retourne le solde."""
      self.solde += somme
      return self.solde

   # définition de la méthode Debit()
   def Debit(self, somme):
      """Débite le compte de la valeur somme. Retourne le solde."""
      self.solde -= somme
      return self.solde

   # définition de la méthode spéciale __add__ (surcharge de l'opérateur +)
   def __add__(self, somme):
      """x.__add__(somme) <=> x+somme
      Crédite le compte de la valeur somme.
      Affiche 'Nouveau solde : somme'"""
      self.solde += somme
      print("Nouveau solde : {:+.2f} €".format(self.solde))      
      return self

   # définition de la méthode spéciale __sub__ (surcharge de l'opérateur -)
   def __sub__(self, somme):
      """x.__sub_(somme) <=> x-somme
      Débite le compte de la valeur somme.
      Affiche 'Nouveau solde : somme'"""
      self.solde -= somme
      print("Nouveau solde : {:+.2f} €".format(self.solde))
      return self

if __name__ == '__main__':
   # Ce bloc d'instructions est exécuté si le module est lancé en tant que programme autonome
   # Instanciation de l'objet cb1 de la classe Compte
   cb1 = Compte(1000)
   # formatage des données pour afficher deux chiffres après la virgule et le signe
   print("{:+.2f}".format(cb1.Solde()))
   print("{:+.2f}".format(cb1.Credit(200)))
   print("{:+.2f}".format(cb1.Debit(50.23)))
   print("{:+.2f}".format(cb1.Solde()))
   cb1.NouveauSolde(5100)
   print("{:+.2f}".format(cb1.Solde()))
   cb1+253.2
   cb1-1000+100
   cb1-cb1.Solde()
