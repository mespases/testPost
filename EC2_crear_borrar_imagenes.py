import boto3

# Config boto3
region = ""
aws_key_id = ""
aws_secret_key = ""

# Connect AWS
client = boto3.client('ec2', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
client_res = boto3.resource('ec2', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
running_instances = client_res.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])


class CrearBorrar:
    """ Crea y borra imagenes de AWS """

    def __init__(self):
        self.menu()


    def info_crear(self):
        """ Pide la informacion para crear una AMI """
        nombre = raw_input("Introduce el nombre de la AMI: ")
        descripcion = raw_input("Introduce una descripcion: ")
        instanceId = raw_input("Introduce la id de la instancia: ")

        self.crear_imagen(nombre, descripcion, instanceId)


    def crear_imagen(self, nombre, descripcion, instanceId):
        """ Crea una AMI con la informacion proporcionada """
        client.create_image(
            Description=descripcion,
            InstanceId=instanceId,
            Name=nombre,
        )


    def info_borrar(self):
        """ Pide la id de la AMI para poder eliminarla """
        id = raw_input("Introduce la id del AMI a borrar: ")

        self.eliminar_imagen(id)


    def eliminar_imagen(self, id):
        """ Elimina una AMI"""
        client.deregister_image(
            ImageId=id,
        )


    def menu(self):
        print "Selecciona una opcion de las siguientes"
        opcion = raw_input("Crear o borrar: ")

        if opcion.title() in ["Crear", "Borrar"]:
            if opcion.title() == "Crear":
                self.info_crear()

            else:
                self.info_borrar()

        else:
            print "La opcion introducida es incorrecta"


if __name__ == "__main__":
    CrearBorrar()