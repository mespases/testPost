import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("""CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)""")

        cursor.execute("""CREATE TABLE plato(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL, 
                    categoria_id INTEGER NOT NULL,
                    FOREIGN KEY(categoria_id) REFERENCES categoria(id))
        """)
    except:
        print("Las tablas ya existe.")
    else:
        print("Las tablas se han creado correctamente")

    conexion.close()

def agragar_categoria():
    categoria = raw_input("Nombre de la nueva categoria ? \n> ")

    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    cursor.execute('insert into categoria values(null,{})'.format(categoria))

    conexion.commit()
    conexion.close()

# Crear base de datos
crear_bd()

# Menu
while True:
    print("\nBienvenido al gesotr del restaurante")
    opcion = int(input("Introduce una opcion\n1) Agregar una categoria \n2) Salir del programa "))

    if opcion == 1:
        agragar_categoria()
    elif opcion == 2:
        print("Saliendo del programa")
        break
    else:
        print("Opcion incorrecta")