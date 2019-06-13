contactos = [
    {"Juan", 873647382},
    {"Pedro", 99999999},
    {"Lucas", 88888888},
    {"Esteban", 777777777},
    {"Jorge", 666666666}
]

print contactos[0:]

for contacto in contactos:
    print("El nombre del contacto es {} y su numero de telefono es {}.").format(contacto[0], contacto[1])