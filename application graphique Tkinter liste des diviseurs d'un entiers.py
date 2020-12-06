"""
Créer un programme en python qui propose à l'utilisateur une fenetre Thinter
lui demandant de saisir un entier N et lui renvoie tous les diviseurs de N
"""
from tkinter import *

def action():
    N = int(entryNombre.get())
    lblDiviseurs['text'] = "Diviseurs de N : "
    for i in range(1 , N+1):
        if(N%i == 0):
            lblDiviseurs['text'] = lblDiviseurs['text'] + " " + str(i) + " "




fen = Tk()
fen.geometry("400x175")
lblNombre = Label(fen , text = "Entrer la valeur de N:")
lblNombre.place(x = 10, y = 20)
entryNombre = Entry(fen)
entryNombre.place(x = 200, y = 20)
lblDiviseurs = Label(fen , text = "Les diviseurs de N: ")
lblDiviseurs.place(x = 10 , y = 50)
Valider = Button(fen , text = "Valider l'opération" , command = action)
Valider.place(x = 200, y = 90)
fen.mainloop()