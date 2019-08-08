import wmi
import psutil
import boto3
import datetime


# Config boto3
region = ""
aws_key_id = ""
aws_secret_key = ""


c = wmi.WMI()
client = boto3.client('cloudwatch', region_name=region, aws_access_key_id=aws_key_id, aws_secret_access_key=aws_secret_key)

cpu_percent = []
ram_percent = []
disk_percent = []

class Metrics:

    def __init__(self):
        try:
            self.get_metrics()
            self.push_metrics_cpu()
            self.push_metrics_ram()
            self.push_metrics_disk()
            print "."
        except:
            print "Error"


    def get_metrics(self):
        """ Obtiene las metricas y las imprime por pantalla"""
        try:
            self.delete_elements_in_array()
        except:
            pass

        for i in range(5):
            utilizations = [cpu.LoadPercentage for cpu in c.Win32_Processor()]
            percent_used_cpu = int(sum(utilizations) / len(utilizations))
            ram = psutil.virtual_memory()[2]
            disk = psutil.disk_usage('/')[3]

            self.save_metrics(percent_used_cpu, ram, disk)

            # print "CPU: {}%".format(percent_used_cpu)
            # print "RAM: {}%".format(ram)
            # print "Disk: {}% ".format(disk)
            # print "============"


    def delete_elements_in_array(self):
        """ Elimina todos los elementos de dentro de la array """
        for i in range(len(cpu_percent)):
            cpu_percent.pop()
            ram_percent.pop()
            disk_percent.pop()


    def save_metrics(self, cpu, ram, disk):
        """ Guarda las metricas en las array"""
        cpu_percent.append(cpu)
        ram_percent.append(ram)
        disk_percent.append(disk)


    def push_metrics_cpu(self):
        """ Sube las metricas de cpu a AWS """
        actual_date = datetime.datetime.utcnow()

        response = client.put_metric_data(
            Namespace='Metricas',
            MetricData=[
                {
                    'MetricName': 'CPUUtilization',
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': 'i-015d868e1a67641ae'
                        },
                    ],
                    'Timestamp': actual_date,
                    'StatisticValues': {
                        'SampleCount': 5,
                        'Sum': sum(cpu_percent),
                        'Minimum': min(cpu_percent),
                        'Maximum': max(cpu_percent)
                     },
                },
            ]
        )

    def push_metrics_ram(self):
        """ Sube las metricas de ram a AWS """
        actual_date = datetime.datetime.utcnow()

        response = client.put_metric_data(
            Namespace='Metricas',
            MetricData=[
                {
                    'MetricName': 'MemoryUtilization',
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': 'i-015d868e1a67641ae'
                        },
                    ],
                    'Timestamp': actual_date,
                    'StatisticValues': {
                        'SampleCount': 5,
                        'Sum': sum(ram_percent),
                        'Minimum': min(ram_percent),
                        'Maximum': max(ram_percent)
                    },
                },
            ]
        )

    def push_metrics_disk(self):
        """ Sube las metricas de dicso a AWS """
        actual_date = datetime.datetime.utcnow()

        response = client.put_metric_data(
            Namespace='Metricas',
            MetricData=[
                {
                    'MetricName': 'C: DISK SPACE',
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': 'i-015d868e1a67641ae'
                        },
                    ],
                    'Timestamp': actual_date,
                    'StatisticValues': {
                        'SampleCount': 5,
                        'Sum': sum(disk_percent),
                        'Minimum': min(disk_percent),
                        'Maximum': max(disk_percent)
                    },
                },
            ]
        )


Metrics()