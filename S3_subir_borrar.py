import boto3

# Config boto3
region = ""
aws_key_id = ""
aws_secret_key = ""

# Connect AWS
client = boto3.client('ec2', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
client_res = boto3.resource('ec2', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
running_instances = client_res.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
s3 = boto3.resource('s3', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)
client_s3 = boto3.client('s3', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)


class Bucket:

    def __init__(self):
        self.menu()


    def crear(self, acl, bucket, location, lock):
        """ Crea un nuevo bucket """
        client_s3.create_bucket(
            ACL=acl,
            Bucket=bucket,
            CreateBucketConfiguration={
                'LocationConstraint': location
            },
            ObjectLockEnabledForBucket=lock
        )


    def borrar(self, bucket):
        client_s3.delete_bucket(
            Bucket=bucket
        )


    def info_borrar(self):
        bucket = raw_input("Introduce le nombre del bucket a borrar: ")
        self.borrar(bucket)


    def info_crear(self):
        """ Pide la informacion necesaria para crear un bucket """
        acl = raw_input("Indica que ACL quieres: ")
        if acl in ['private', 'public-read', 'public-read-write', 'authenticated-read']:
            pass
        else:
            print "ACL seleccionada incorrecta, se selecciona 'private' por defecto"
            acl = "private"

        bucket = raw_input("Introduce el nombre del bucket: ").lower()
        location = raw_input("Introduce la localicacion del bucket: ").upper()
        if location in ['EU', 'eu-west-1', 'us-west-1', 'us-west-2', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1', 'sa-east-1', 'cn-north-1', 'eu-central-1']:
            pass
        else:
            print "La localizacion es incorrecta"
            exit()

        lock = raw_input("Especifica si quieres el bloqueo de Amazon para el S3, True o False: ")
        if lock.title() in ["True", "False"]:
            lock = bool(lock)
        else:
            print "Bloqueo mal introducido, por defecto se selecciona a 'False'"
            lock = False

        self.crear(acl, bucket, location, lock)


    def menu(self):
        print "Elige una de las siguientes opciones"
        opcion = raw_input("Crear o Borrar: ").title()

        if opcion == "Crear":
            self.info_crear()

        elif opcion == "Borrar":
            self.info_borrar()

        else:
            print "La opcion introducida es incorrecta"



if __name__ == "__main__":
    Bucket()