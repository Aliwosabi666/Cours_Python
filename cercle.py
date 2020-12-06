# script cercle.py
#(C) Fabrice Sincère
from tkinter import *
import random

def Cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    x = random.randint(0,Largeur)
    y = random.randint(0,Hauteur)
    r = 20
    Canevas.create_oval(x-r, y-r, x+r, y+r, outline='blue', fill='blue')

def Effacer():
    """ Efface la zone graphique """
    Canevas.delete(ALL)

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Cercle')

# Création d'un widget Canvas (zone graphique)
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Canevas.pack(padx =5, pady =5)

# Création d'un widget Button (bouton Go)
BoutonGo = Button(Mafenetre, text ='Go', command = Cercle)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Effacer)
BoutonEffacer = Button(Mafenetre, text ='Effacer', command = Effacer)
BoutonEffacer.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()
