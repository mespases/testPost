from Tkinter import *
import tkMessageBox
import tkColorChooser
import tkFileDialog


root = Tk()

def test():
    # tkMessageBox.showinfo("Hola", "Hola mundo")
    # tkMessageBox.showwarning("Alerta", "Seccion solo para admin")
    # tkMessageBox.showerror("Error", "Ha ocurrido un error inesperado")
    """resultado = tkMessageBox.askquestion("Salir", "Estas seguro de salir ?")
    if resultado == "yes":
        root.destroy()
    resultado = tkMessageBox.askokcancel("Salir", "Sobreescribir el fichero actual ? ")
    if resultado:
        root.destroy()
    resultado = tkMessageBox.askyesno()
    if resultado:
        root.destroy()"""
    # tkMessageBox.askretrycancel("Reintentar", "No se puede conectar")
    # tkColorChooser.askcolor(title="Elige un color")
    #file = tkFileDialog.askopenfilename(title = "Abrir un fichero", initialdir="C:", filetype=(("Ficheros de texto", "*.txt"), ("Fichero de texto Avanzado", "*.txt2")))
    # print file

Button(root, text="Clicame", command=test).pack()

root.mainloop()