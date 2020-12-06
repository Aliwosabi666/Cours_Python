# script heure.py
#(C) Fabrice Sincère
from tkinter import *

import time

def maj():
    # on arrive ici toutes les 1000 ms
    heure.set(time.strftime('%H:%M:%S'))
    Mafenetre.after(1000,maj)

Mafenetre = Tk()
Mafenetre.title("Heure courante")

# Création d'un widget Label
heure = StringVar()
Label(Mafenetre,textvariable=heure).pack(padx=10,pady=10)

maj()

Mafenetre.mainloop()
