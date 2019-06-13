from Tkinter import *

root = Tk()

lable = Label(root, text="Nombre muy largo")
lable.grid(row=0, column=0, sticky="e", padx=5, pady=5)

entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")# state = "disabled" no nos deja escribir

lable2 = Label(root, text="Apellido")
lable2.grid(row=1, column=0, sticky="e", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="left", show="*")# Muestra un * cuando se escribe, ejemplo contrasena



root.mainloop()