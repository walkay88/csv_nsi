from tkinter import *
import csv
class FSA():
    def __init__(self):
     
        self.fen=Tk()
        self.fen.title('nsi_csv')
        self.fen.pack_propagate(0)
 
        self.cadre = Frame(self.fen, bg='white', borderwidth=2, relief=GROOVE)
        self.cadre.pack(side=TOP, padx=10, pady=10)
 
        self.cadre2 = Frame(self.fen, bg='white', borderwidth=2, relief=GROOVE)
        self.cadre2.pack(side=LEFT,padx=10, pady=10)
 
        self.cadre3 = Frame(self.fen, bg='white', borderwidth=2, relief=GROOVE)
        self.cadre3.pack(side=BOTTOM,padx=10, pady=10)
            
        self.bouton=Button(self.cadre, text='Action')
        self.bouton.config(command=self.action)
        self.bouton.pack()
 
        self.bouton2=Button(self.cadre2, text='Quitter')
        self.bouton2.config(command=self.fen.destroy)
        self.bouton2.pack()
 
        self.bouton3=Button(self.cadre3, text='CSV')
        self.bouton3.config(command=self.action2)
        self.bouton3.pack()
 
    def run(self):
     
        self.fen.mainloop()
     
    def action(self):
 
        self.lab = Label(self.cadre)
        self.lab.config(text='bonjour')
        self.lab.pack()
 
    def action2(self):
         
        self.fname="large.csv"
        self.file=open(self.fname, "rb")
        try:
            self.reader=csv.reader(self.file)
            for row in self.reader :
                print (row)
        finally :
            self.file.close()
 
if __name__ == '__main__' :
    app= FSA()
    app.run()