from errno import ENETRESET
from tkinter import *
from tkinter.messagebox import showinfo


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("CSV-NSI")
        self.geometry("1280x720")
        
    def alert():
        showinfo("alerte", "Bravo!")

    menubar = Menu(ENETRESET)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Créer", command=alert)
    menu1.add_command(label="Editer", command=alert)
    menu1.add_separator()
    menu1.add_command(label="Quitter", command=fenetre.quit)
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="Couper", command=alert)
    menu2.add_command(label="Copier", command=alert)
    menu2.add_command(label="Coller", command=alert)
    menubar.add_cascade(label="Editer", menu=menu2)

    menu3 = Menu(menubar, tearoff=0)
    menu3.add_command(label="A propos", command=alert)
    menubar.add_cascade(label="Aide", menu=menu3)

    fenetre.config(menu=menubar)

App().mainloop()
