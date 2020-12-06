"""
Créer à l'aide de la bibliothéque graphique Thinkter, une interface graphique
qui affiche deux champs de saisies demadant à l'utilisateur de saisir un nombre
entier et en cliquant sur le bouton de validation, le deuxiéme champ affiche le
double du nombre saisi.
"""

from  tkinter import *

def action():
    N = int(enteryNombre1.get())
    N2 = 2*N
    enteryNombre2.delete(0,END)
    enteryNombre2.insert(0 , N2)


fen= Tk()
fen.geometry("400x300")

lblnombre1 = Label(fen , text = "Enter la valeur de N :")
lblnombre1.place(x=50 , y= 50 )
enteryNombre1 = Entry(fen)
enteryNombre1.place(x = 200 , y = 50)

lblnombre2 = Label(fen , text = "Voici le double")
lblnombre2.place(x=50 , y= 100 )
enteryNombre2 = Entry(fen)
enteryNombre2.place(x = 200 , y = 100)

Valider = Button(fen , text="Valider l'operation", command = action)
Valider.place(x = 200 , y = 150)

fen.mainloop()

