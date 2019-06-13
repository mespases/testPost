import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre varchar(20), edad int, email varchar(100))") # Crear una tabla
# cursor.execute("INSERT INTO usuarios VALUES ('Hector', 27, 'ejemplo1@gmail.com')")    # Insertar un solo usuario
# cursor.execute("SELECT * FROM usuarios") # Realizar consulta
# usuario = cursor.fetchone() # Recupera el resultado del primer usuario, "si se ponemos de nuevo fetchone, pasara al segundo usuario"

"""usuarios = [
    ('Mario', 51, 'mario@ejempli.com'),
    ('Sergio', 32, 'sergio@ejempli.com'),
    ('Paco', 45, 'paco@ejempli.com'),
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios) # Insertar usuarios de forma """

cursor.execute("select * from usuarios")

usuarios = cursor.fetchall() # Recupera todos los registros

for usuario in usuarios:
    print usuario[0]

conexion.commit()
conexion.close()