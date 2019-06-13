from Tkinter import *

def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()

def restar():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()

def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def borrar():
    n1.set("")
    n2.set("")

root = Tk()
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

Label(root, text="Numero1").pack()
Entry(root, justify="center", textvariable=n1).pack()
Label(root, text="Numero2").pack()
Entry(root, justify="center", textvariable=n2).pack()
Label(root, text=" ").pack()
Label(root, text="Resultado").pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()
Button(root, text="Sumar", command=sumar).pack(side="left")
Button(root, text="Restar", command=restar).pack(side="left")
Button(root, text="Producto", command=producto).pack(side="left")



root.mainloop()
