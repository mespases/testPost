import boto3

# Config boto3
region = ""
aws_key_id = ""
aws_secret_key = ""

# Connect AWS
client_autoscaling = boto3.client('autoscaling', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)

class Subir_Bajar:

    def __init__(self):
        self.info()


    def actualizar(self, autoscaling_sg, minsize, maxsize, desired):
        """ Actualiza la cantidad de servidores """
        client_autoscaling.update_auto_scaling_group(
            AutoScalingGroupName=autoscaling_sg,
            MinSize=minsize,
            MaxSize=maxsize,
            DesiredCapacity=desired
        )


    def info(self):
        """ Pide informacion para actualizar los servidores """
        autoscaling_sg = raw_input("Introduce el nombre del SG que quieres modificar: ")
        minsize = int(input("Introduce el numero minimo de instancias: "))
        maxsize = int(input("Introduce el numero maximo de instancias: "))
        desired = int(input("Introduce el numero deseado de instancias: "))

        self.actualizar(autoscaling_sg, minsize, maxsize, desired)

if __name__ == "__main__":
    Subir_Bajar()