from csv import reader
from tkinter import BOTH, BOTTOM, CENTER, NO, RIGHT, X, Y, Frame, Menu, Scrollbar, Tk
from tkinter.filedialog import askopenfilename
from tkinter.simpledialog import askstring
from tkinter.ttk import Treeview
from tkinter import *
from tkinter.font import *
import random

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Nollan")
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.maxsize(1920, 1080)
        self.config(background="#23262E")
        self.iconbitmap("assets/icon.ico")
        self.protocol("WM_DELETE_WINDOW", self.quit)

        # Add a menu bar with a "File" menu
        self.barmenu = Menu(self)
        filemenu = Menu(self.barmenu, tearoff=0)
        filemenu.add_command(label="Ouvrir", command=self.choosefile)
        filemenu.add_separator()
        filemenu.add_command(label="Quitter", command=self.quit)
        self.barmenu.add_cascade(label="Fichier", menu=filemenu)
        self.config(menu=self.barmenu)

        # Add a frame
        self.frame = Frame(self)
        self.frame.config(bg="#23262E")
        self.frame.pack(fill=BOTH, expand=True)

        # Add a treeview
        self.tree = Treeview(self.frame)
        scroll_Y = Scrollbar(self.tree, orient="vertical",
                             command=self.tree.yview)
        scroll_X = Scrollbar(self.tree, orient="horizontal",
                             command=self.tree.xview)
        self.tree.configure(yscrollcommand=scroll_Y.set,
                            xscrollcommand=scroll_X.set)
        scroll_Y.pack(side=RIGHT, fill=Y)
        scroll_X.pack(side=BOTTOM, fill=X)
        self.tree.pack(fill=BOTH, expand=True)

        self.mainloop()

    def choosefile(self):
        file = askopenfilename(
            title="Ouvrir un fichier CSV",
            filetypes=[
                ("Fichier CSV", "*.csv"),
                ("Fichiers TXT", "*.txt"),
                ("Tous les fichiers", "*.*"),
            ],
        )
        rows = []
        with open(file, "r") as file:
            for row in reader(file, delimiter=";"):
                rows.append(tuple(row))

        self.tree.delete(*self.tree.get_children())

        self.tree.column("#0", anchor=CENTER, width=0, stretch=NO)
        self.tree.heading("#0", text="", anchor=CENTER)

        self.tree["columns"] = rows.pop(0)
        for key in self.tree["columns"]:
            self.tree.column(key, anchor=CENTER, minwidth=100)
            self.tree.heading(key, text=key, anchor=CENTER)

        for row in rows:
            self.tree.insert("", "end", values=row)       

    def quit(self):
        print("Quitting...")
        self.destroy()


App()
