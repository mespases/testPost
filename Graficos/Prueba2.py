from Tkinter import *

root  = Tk()


root.title("Prueba2")
root.resizable(1,1)
root.iconbitmap('hola.ico')

frame = Frame(root, width=480, height=320)
# frame.pack(side="bottom", anchor="s") # e = este, w = oeste
frame.pack(fill='both', expand=1) # Rellena el el ancho y "y" rellena en alto, "both" rellana tanto en alto como en ancho
# Tipo de cursor
frame.config(cursor="pirate")
# Color de fondo
frame.config(bg='lightblue')
# Borde
frame.config(bd=25)
# Tipo de borde
frame.config(relief="sunken")

root.config(cursor="arrow")
root.config(bg='blue')
root.config(bd=15)
root.config(relief="ridge")

root.mainloop()