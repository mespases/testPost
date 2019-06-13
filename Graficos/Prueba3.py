from Tkinter import *

root = Tk()
root.title("Prueba2")
root.iconbitmap('hola.ico')

# Variables dinamicas
texto = StringVar()
texto.set("Un nuvo texto")

"""frame = Frame(root, width=480, height=320)
frame.pack()"""

"""lable = Label(frame, text="Hola mudo")
lable.place(x=100, y=100)"""
# Label(frame, text="Hola mundo").place(x=150, y=200)

"""Label(root, text="Hola mundo").pack(anchor="nw")
Label(root, text="Hola de nuevo").pack(anchor="center")
Label(root, text="Hola hola").pack(anchor="se")"""

Label(root, text="Hola mundo").pack(anchor="nw")
label = Label(root, text="Hola de nuevo")
label.pack(anchor="center")
Label(root, text="Hola hola").pack(anchor="se")

label.pack(anchor="center")
label.config(bg="green", fg="blue", font=("Arial", 24))# fg es el color del texto
label.config(textvariable=texto)


root.mainloop()