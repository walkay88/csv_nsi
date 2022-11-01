from tkinter import Tk


class App(Tk):
    def __init__(self):
        Tk.__init__(self)

        self.title("CSV-NSI")
        self.geometry("1280x720")


App().mainloop()
