# script cible.py
#(C) Fabrice Sincère
from tkinter import *
import random

def Cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    x = random.randint(0,Largeur)
    y = random.randint(0,Hauteur)
    r = 10
    
    # on dessine un cercle dans la zone graphique
    item = Canevas.create_oval(x-r, y-r, x+r, y+r, outline='black', fill='black')
    
    print("Création du cercle (item" , item ,")")
    # affichage de tous les items de Canevas
    print(Canevas.find_all())

def Undo():
    """ Efface le dernier cercle"""
    if len(Canevas.find_all()) > 1:
        item = Canevas.find_all()[-1]
        # on efface le cercle
        Canevas.delete(item)
       
        print("Suppression du cercle (item" , item ,")")
        # affichage de tous les items de Canevas
        print(Canevas.find_all())

def EffacerTout():
    """ Efface tous les cercles"""
    while len(Canevas.find_all()) > 1:
        Undo()


# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Cible')

# Image de fond
photo = PhotoImage(file="tk_cible.gif")

# Création d'un widget Canvas (zone graphique)
Largeur = 550
Hauteur = 550
Canevas = Canvas(Mafenetre,width = Largeur, height =Hauteur)
item = Canevas.create_image(0,0,anchor=NW, image=photo)
print("Image de fond (item",item,")")
Canevas.pack()

# Création d'un widget Button
BoutonGo = Button(Mafenetre, text ='Tirer', command = Cercle)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button
BoutonEffacer = Button(Mafenetre, text ='Effacer le dernier tir', command = Undo)
BoutonEffacer.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button
BoutonEffacerTout = Button(Mafenetre, text ='Effacer tout', command = EffacerTout)
BoutonEffacerTout.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 10, pady = 10)

Mafenetre.mainloop() 
