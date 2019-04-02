# Docker cheatsheet

The cheatsheet from "Get Started" from [docker documentation](https://docs.docker.com/get-started/)

### List Docker CLI commands

```shell
docker
docker container --help
```

### Display Docker version and info

```shell
docker --version
docker version
docker info
```

## Docker container

### List Docker containers 

```shell
docker container ls     # List running containers
docker container ls --all   # List all containers
docker container ls -aq     # List all containers in quiet mode
docker container ls -q  # List container IDs
docker inspect <task or container>  # Inspect task or container
```

### Stop container

```shell
docker container stop <hash> # Gracefully stop the specified container
docker container kill <hash> # Force shutdown of the specified container
```

### Remove container

```shell
docker container rm <hash> # Remove specified container from this machine
docker container rm $(docker container ls -a -q) # Remove all containers
```

## Docker image

### Dockerfile example

Dockerfile example:
```Dockerfile
# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### Create image using this directory's Dockerfile

```shell
docker build -t <imagename>  # create an image with name <imagename>
docker build -t friendlyhello  # create an image with the name friendlyhello
```

### Run image

```shell
docker run helloworld  # execute docker image helloworld
docker run -p <host's port>:<container's published port> <imagename>
docker run -p 4000:80 friendlyhello  # Run "friendlyhello" mapping port 4000 to 80
docker run -d -p 4000:80 friendlyhello  # same as above, but in detached mode (run in backgroud)
```

### List Docker images

```shell
docker image ls
docker image ls -a # List all images on this machine
```

### Remove image

```shell
docker image rm <image id> # remove specified image from this machine
docker image rm $(docker image ls -a -q)    # remove all images from this machine
```

### Image registry

```shell
docker login    # log in this CLI session using your Docker credentials
docker tag <image> username/repository:tag  # Tag <image> for upload to registry
docker push username/repository:tag     # Upload tagged image to registry
docker run username/repository:tag      # Run image from a registry
```


## Service

### docker-compose example

`docker-compose.yml` example:
```yml
version: "3"
services:
  web:
    # replace username/repo:tag with your name and image details
    image: username/repo:tag
    deploy:
      replicas: 5
      restart_policy:
        condition: on-failure
      resources:
        limits:
          cpus: "0.1"
          memory: 50M
    ports:
      - "80:80"
    networks:
      - webnet
  visualizer:
    image: dockersamples/visualizer:stable
    ports:
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
    deploy:
      placement:
        constraints: [node.role == manager]
    networks:
      - webnet
networks:
  webnet:
```

### List services

```shell
docker service ls   # List running services associated with an app
docker service ps <service>     # List tasks associated with an app
```


## Swarm

### Create a Virtual Machine

```shell
docker-machine create --driver virtualbox <virtual-machine-name> # Create a VM
docker-machine create --driver virtualbox myvm1 # Create a VM with the name myvm1
```

### Talk to Nodes

```shell
docker-machine env myvm1    # View basic information about my node myvm1
docker-machine ls # list VMs, asterisk shows which VM this shell is talking to

# Talk to a node using ssh, scp
docker-machine ssh <nodename> "<command>"    # Execute <command> in the node <nodename>
docker-machine ssh myvm1 "docker node ls"   # List the nodes in your swarm
docker-machine ssh myvm1 "docker node inspect <node ID>"    # Inspect a node
docker-machine ssh myvm1 "docker swarm init --advertise-addr <myvm1 ip>"    # initialize swarm; myvm1 is manager
docker-machine ssh myvm1 "docker swarm join-token -q worker"    # View join token
docker-machine ssh myvm1    # Open an SSH session with the VM; type "exit" to end
docker-machine ssh myvm2 "docker swarm leave"   # Make the worker leave the swarm
docker-machine ssh myvm1 "docker swarm leave -f"    # Make master leave, kill swarm
docker-machine scp docker-compose.yml myvm1:~   # Copy file to node's home dir; only required if you use ssh to connect to manager and deploy the app
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"  # Deploy an app using ssh; first copy the Compose file to myvm1 

# Connect/Disconnect shell to a node
docker-machine env myvm1    # Show environment variables and command for myvm1
eval $(docker-machine env myvm1)    # Connect shell to myvm1
eval $(docker-machine env -u)   # Disconnect shell from VMs, use native docker

# When the shell is connected to manager (myvm1)
docker stack deploy -c <file> <app> # Deploy an app; uses local Compose file 
docker node ls  # View nodes in swarm (while logged on to manager)
```

### Start, Stop and Remove

```shell
docker-machine start myvm1  # Start myvm1
docker-machine stop $(docker-machine ls -q) # Stop all running VMs
docker-machine rm $(docker-machine ls -q) # Delete all VMs and their disk images
docker swarm leave --force # Take down a single node swarm from the manager
```


## Stack

```shell
docker stack deploy -c docker-compose.yml getstartedlab # deploy getstartedlab
docker stack ps getstartedlab
docker stack rm <appname>   # Tear down an application
docker stack ls # List stacks or apps
```
