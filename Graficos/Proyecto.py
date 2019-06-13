from Tkinter import *
import tkFileDialog as FileDialog
from io import open

ruta = "" # Se usara para almacenar la ruta de un fichero
fichero = ""
contenido = ""

def nuevo():
    global ruta
    mensaje.set("Nuevo fichero")
    ruta = ""
    texto.delete(1.0, "end")
    root.title(ruta + " - Mi Editor")

def abrir():
    global ruta, fichero, contenido
    mensaje.set("Abrir fichero")
    ruta = FileDialog.askopenfilename(
        initialdir='C:\CursoPython\Fase 4 - Temas avanzados\Tema 13 - Interfaces graficas con tkinter\Apuntes',
        filetype=(("Ficheros de texto", "*.txt"),),
        title="Abrir un fichero de texto")

    if ruta != "":
        fichero = open(ruta, 'r')
        contenido = fichero.read()
        texto.delete(1.0, 'end')
        texto.insert('insert', contenido)
        fichero.close()
        root.title(ruta + " - Mi editor")

def guardar():
    global ruta, fichero, contenido
    mensaje.set("Guardar fichero")
    if ruta != "":
        contenido = texto.get(1.0,  'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("El fichero se ha guardado correctamente")
    else:
        guardarcomo()

def guardarcomo():
    global ruta, fichero, contenido
    mensaje.set("Guardar fichero como...")
    fichero = FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, 'end-1c')
        fichero = open(ruta, 'w+')
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Fichero guardado correctamente")
    else:
        mensaje.set("Guardado cancelado")
        ruta = ""



root = Tk()
root.title("Mi editor")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guadar como...", command=guardarcomo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archivo")

texto = Text(root)
texto.pack(fill="both", expand=1)
texto.config(bd=0, padx=6, pady=4, font=("Consolas", 12))

mensaje = StringVar()
mensaje.set("Bienvenido a tu Editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)

root.mainloop()