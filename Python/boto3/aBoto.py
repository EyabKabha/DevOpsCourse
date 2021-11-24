import boto3


# for instance in response['Reservations'][0]['Instances']:
#     print(instance['InstanceId'])

#3 functins

#1 create serviceQ
#2 prints service
#3 stop service




def create_instance(instance_type,image_id,max_count,min_count):
    ec2 = boto3.resource("ec2")
    response = ec2.create_instances(InstanceType=instance_type, ImageId=image_id, MaxCount=max_count, MinCount=min_count)
    print(response)

def print_instances():
    client = boto3.client("ec2")
    response = client.describe_instances()
    for instance in response["Reservations"][0]["Instances"]:
        print(instance["InstanceId"])


# def stop_server():
