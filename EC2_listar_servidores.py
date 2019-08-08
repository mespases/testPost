import boto3

# Config boto3
region = ""
aws_key_id = ""
aws_secret_key = ""

# Connect AWS
client = boto3.client('ec2', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
client_res = boto3.resource('ec2', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
running_instances = client_res.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Informacion de las instancias
Id = []
Nombre = []
Tipo_instancia = []
Ip = []
Grupo_SG = []
AMI_id = []

class Listar:

    """ Obtiene una lista de todos los sevidores de AWS, ensenando
        su id, nombre, tipo de instancia, ip, grupo de seguridad
        y la id de la ami """

    def __init__(self):
        self.get_lista()
        self.print_all()


    def get_lista(self):
        """ Obtiene la informacion y la gurada en una array """
        response = client.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                    Id.append(instance["InstanceId"])
                    Nombre.append(self.get_nombre(instance))
                    Tipo_instancia.append(instance["InstanceType"])
                    try:
                        Ip.append(instance["PrivateIpAddress"])
                    except:
                        pass
                    Grupo_SG.append(self.get_SG(instance))
                    AMI_id.append(instance["ImageId"])

    def get_nombre(self, instance):
        """ Obtiene el nombre de la instancia """
        try:
            for tag in instance["Tags"]:
                return tag["Value"]
        except:
            pass


    def get_SG(self, instance):
        """ Obtiene el nombre del grupo de seguridad """
        for SG in instance["SecurityGroups"]:
            return SG["GroupName"]


    def print_all(self):
        """ Muestra toda la informacion por pantalla """
        for i in range(len(Nombre)):
            print "La id de la instancia es: ", Id[i]
            print "El nombre de la instancia es: ", Nombre[i]
            print "El tipo de instancia es: ", Tipo_instancia[i]
            try:
                print "La ip de la instancia es: ", Ip[i]
            except:
                pass
            print "El grupo de seguridad es: ", Grupo_SG[i]
            print "La id del AMI es: ", AMI_id[i]
            print "=============================================="

if __name__ == "__main__":
    Listar()