"""Introducir dos numeros
Pedir el tipo de operacion que se quiere realizar
Mostrar resultado"""

from Tkinter import *
class Interfaz():

    def __init__(self):
        self.root = Tk()
        self.root.config(bd=15)
        self.root.resizable(1,1)
        self.root.title("Calculadora")
        self.root.iconbitmap('Graficos/hola.ico')

        self.__confGrid()

        self.__setFrame()
        self.__diseno()

        self.root.mainloop()

    def __setFrame(self):
        self.frame = Frame(self.root)
        self.frame.grid(row=0, column=0)

    def __diseno(self):
        i = 1
        for row_index in range(3):
            Grid.rowconfigure(self.frame, row_index, weight=1)
            for col_index in range(3):
                Grid.columnconfigure(self.frame, col_index, weight=1)
                btn = Button(self.frame, text=i)
                btn.grid(row=row_index, column=col_index, sticky=N + S + E + W)
                i += 1
        self.__espCar()


    def __confGrid(self):
        Grid.rowconfigure(self.root, 0, weight=1)
        Grid.columnconfigure(self.root, 0, weight=1)

    def __espCar(self):
        btn = Button(self.frame, text=0)
        btn.grid(row=3, column=0, sticky=N + S + E + W)
        btn = Button(self.frame, text=".")
        btn.grid(row=3, column=1, sticky=N + S + E + W)
        btn = Button(self.frame, text="=")
        btn.grid(row=3, column=2, sticky=N + S + E + W)
        btn = Button(self.frame, text="+")
        btn.grid(row=3, column=3, sticky=N + S + E + W)
        btn = Button(self.frame, text="/")
        btn.grid(row=0, column=3, sticky=N + S + E + W)
        btn = Button(self.frame, text="*")
        btn.grid(row=1, column=3, sticky=N + S + E + W)
        btn = Button(self.frame, text="-")
        btn.grid(row=2, column=3, sticky=N + S + E + W)
        ent = Entry(self.root)
        ent.grid(row=4, sticky=N + S + E + W)


c = Interfaz()