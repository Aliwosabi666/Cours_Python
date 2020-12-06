# script animation.py
#(C) Fabrice Sincère
from tkinter import *
import random

def Cercle():
    """ Dessine un cercle de centre (x,y) et de rayon r """
    global Arret
    x = random.randint(0,Largeur)
    y = random.randint(0,Hauteur)
    r = 10
    Canevas.create_oval(x-r, y-r, x+r, y+r, outline='red', fill='red')
    if Arret == False:
        # appel de la fonction Cercle() après une pause de 50 millisecondes
        Mafenetre.after(50,Cercle)

def Arreter():
	""" Arrêt de l'animation """
	global Arret
	Arret = True

def Demarrer():
    """ Démarre l'animation """
    global Arret
    Canevas.delete(ALL)
    if Arret == True:
        Arret = False
        Cercle() # un seul appel à cette fonction

Arret = True

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Animation')

# Création d'un widget Canvas
Largeur = 480
Hauteur = 320
Canevas = Canvas(Mafenetre, width = Largeur, height =Hauteur, bg ='white')
Canevas.pack(padx =5, pady =5)

# Création d'un widget Button (bouton Démarrer)
BoutonGo = Button(Mafenetre, text ='Démarrer', command = Demarrer)
BoutonGo.pack(side = LEFT, padx = 10, pady = 10)

# Création d'un widget Button (bouton Arrêter)
BoutonArreter = Button(Mafenetre, text ='Arrêter', command = Arreter)
BoutonArreter.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Quitter)
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy)
BoutonQuitter.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()
