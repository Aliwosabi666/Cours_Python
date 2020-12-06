# -*- coding: UTF8 -*-
# script lecture_gif_poo.py
# python 3
# (C) Fabrice Sincère
# & Cyril Ury
# www.kholo-informatique.fr

from tkinter import *
import tkinter.messagebox
import tkinter.filedialog as fd


class Display_Image(Tk):
    """ Interface graphique afficheur d'images gif """

    def __init__(self):
        """ Constructeur """
        # Tk.__init__(self)
        super().__init__()

        self.title("Image")

        # Création d'un widget Menu
        self.affiche_menu()

        # Création d'un widget Canvas
        self.canevas = Canvas(self)
        self.canevas.pack(padx=5, pady=5)

    def affiche_menu(self):
        """ Création d'un widget Menu """
        menubar = Menu(self)

        menufichier = Menu(menubar, tearoff=0)
        menufichier.add_command(label="Ouvrir une image",
                                command=self.ouvrir_image)
        menufichier.add_command(label="Fermer l'image",
                                command=self.fermer_image)
        menufichier.add_command(label="Quitter", command=self.destroy)
        menubar.add_cascade(label="Fichier", menu=menufichier)

        menuaide = Menu(menubar, tearoff=0)
        menuaide.add_command(label="A propos", command=self.fenetre_a_propos)
        menubar.add_cascade(label="Aide", menu=menuaide)

        # Affichage du menu
        self.config(menu=menubar)

    def ouvrir_image(self):
        """ Ouvrir image """
        self.canevas.delete(ALL)  # on efface la zone graphique

        titre = "Ouvrir une image"
        filtres = [('gif files', '.gif'), ('all files', '.*')]
        filename = fd.askopenfilename(title=titre, filetypes=filtres)

        self.photo = PhotoImage(file=filename)

        self.canevas.create_image(0, 0, anchor=NW, image=self.photo)
        self.canevas.config(height=self.photo.height(),
                            width=self.photo.width())

        self.title("Image {} x {}".format(self.photo.width(),
                                          self.photo.height()))

    def fermer_image(self):
        """ Fermer image """
        self.canevas.delete(ALL)
        self.title("Image")

    def fenetre_a_propos(self):
        """ Fenêtre A propos """
        titre, message = "A propos", \
            "Tutorial Python Tkinter\n© Fabrice Sincère ; Cyril Ury"
        tkinter.messagebox.showinfo(titre, message)

    def run(self):
        """ Main window """
        self.mainloop()

if __name__ == "__main__":
    fenetre = Display_Image()
    fenetre.run()
