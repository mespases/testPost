from Tkinter import *

root = Tk()

texto = Text(root)
texto.pack()
texto.config(width=30, height=10, font=("Conslolas", 12), padx=15, pady=5, selectbackground="red") # selectbackground="red" cambia el color de seleccion

root.mainloop()