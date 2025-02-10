import boto3

def create_ecs_cluster(cluster_name):
    ecs_client = boto3.client('ecs')
    response = ecs_client.create_cluster(clusterName=cluster_name)
    return response

def register_task_definition(task_definition_name, container_name, image, memory, cpu):
    ecs_client = boto3.client('ecs')
    response = ecs_client.register_task_definition(
        family=task_definition_name,
        containerDefinitions=[
            {
                'name': container_name,
                'image': image,
                'memory': memory,
                'cpu': cpu,
                'essential': True,
                'portMappings': [
                    {
                        'containerPort': 80,
                        'hostPort': 80,
                        'protocol': 'tcp'
                    }
                ]
            }
        ]
    )
    return response

def create_service(cluster_name, service_name, task_definition, desired_count):
    ecs_client = boto3.client('ecs')
    response = ecs_client.create_service(
        cluster=cluster_name,
        serviceName=service_name,
        taskDefinition=task_definition,
        desiredCount=desired_count,
        launchType='EC2'
    )
    return response

if __name__ == "__main__":
    cluster_name = "mindful-sounds-cluster"
    task_definition_name = "mindful-sounds-task"
    container_name = "mindful-sounds-container"
    image = "mindful-sounds-image:latest"
    memory = 512
    cpu = 256
    service_name = "mindful-sounds-service"
    desired_count = 1

    create_ecs_cluster(cluster_name)
    register_task_definition(task_definition_name, container_name, image, memory, cpu)
    create_service(cluster_name, service_name, task_definition_name, desired_count)