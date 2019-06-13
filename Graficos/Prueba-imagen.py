from Tkinter import *

root = Tk()

imagen = PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=0).pack(side="left")


root.mainloop()