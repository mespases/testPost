import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("""
create table if not exists usuarios ( 
    dni char(9) primary key,
    nombre varchar(50),
    edad int,
    email varchar(100)
)
""")

usuarios = [
    ('11111111A', 'Hector', 48, 'mario@ejempli.com'),
    ('11111111B', 'Mario', 51, 'mario@ejempli.com'),
    ('11111111C', 'Sergio', 32, 'sergio@ejempli.com'),
    ('11111111D', 'Paco', 45, 'paco@ejempli.com'),
]

#cursor.executemany("insert into usuarios values (?,?,?,?)", usuarios)

cursor.execute("drop table profesores")
cursor.execute('''
    create table if not exists profesores(
        id_prof integer primary key autoincrement,
        dni char(9) unique,
        nombre varchar(50),
        edad integer,
        email varchar(100)
        )
        ''')

profesores = [
    ('22222222A', 'Xavi', 48, 'xavi@ejemplo.com'),
    ('33333333B', 'Miguel', 51, 'miguel@ejemplo.com'),
    ('44444444C', 'Jaume', 32, 'jaume@ejemplo.com'),
    ('55555555D', 'Fernando', 45, 'fernando@ejemplo.com'),
]


cursor.execute("insert into profesores values(null,?,?,?,?)", profesores)

conexion.commit()
conexion.close()