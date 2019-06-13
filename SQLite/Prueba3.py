import sqlite3

conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

# cursor.execute("select * from usuarios where id=1")
conexion.execute("update usuarios set nombre='Carlos' where edad=32")
conexion.execute("delete from usuarios where nombre='Paco'")

conexion.commit()
conexion.close()