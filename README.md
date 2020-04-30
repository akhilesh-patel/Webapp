# Create a blogging website
Use this repository to:-
1. Pull the _images_ form [DockerHub](https://hub.docker.com/). 
2. Create the _volumes_ for permanent storage.
3. Complete setup of _MYSQL_ database.
4. Get your own _wordpress_ site.

# Technology
* Linux
* Docker
* Wordpress
* Mysql

# Requirements 
-> Latest version of **Docker**.

-> latest version of **Docker-compose**.

# Installation
-> Use below commands to install docker on linux (any distro)
```
sudo apt-get update
```
-> after installing docker, Install docker-compose.
``` 
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
 ```

-> after installing both docker and docker-compose now execute this command
```
sudo systemctl status docker
```
-> As you can see the docker is inactive here. So, to start the docker services you have to first bring the docker in an active state and to do so use this commmand.
```
sudo systemctl start docker
```
-> Or to permanently activate your docker, use 
```
sudo systemctl enable docker
```

# About
This is a project, built mainly in **docker** that creates a **wordpress blogging site**.

# How to Use
-> To create your own webapp follow the following steps
Step 1 - Open a terminal
Step 2 - cd (change directory) to the folder where docker-compose.yml file is saved.
Step 3 - Execute the docker-compose.yml file.
```
docker-compose up 
```

:v: Everything is set, volumes created, Containers launched, Database connected.
Now, to access your wordpress site just go to your browser's address bar and enter the **Configured_IP and port number** `   http://192.--.--.--:8081 ` [Change it accordingly]

# Stop Service
-> To stop the service, Stop containers
```
docker-compose stop
```

# Start Service
-> To start the service again
```
docker-compose start
```

# License
[MIT](https://github.com/akhilesh-patel/Webapp/blob/master/LICENSE)

# Author 
[Akhilesh Patel](https://github.com/akhilesh-patel)
