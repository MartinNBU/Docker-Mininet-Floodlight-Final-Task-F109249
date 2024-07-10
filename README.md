# Docker-Mininet-Floodlight-Final-Task-F109249
This is my attempt at writing a mininet python script that creates a network with a topology of 419 switches and 19 hosts connected in a linear topology and configure traffic rules between hosts.
Tasks : - Write a sample mininet python script that creates a network with a topology of <419> switches and <19> hosts connected in a linear topology.

- Make your own docker-compose setup in the repo that contains:

    mininet
    floodlight
    Your script

Demonstrate how you configure bidirectional traffic rules between the two most remote hosts in your network with a script to the floodlight api interface.
University : New Bulgarian Univercity
Course : TCMB029 Introduction to Network Engineering - Part II
Lecturer : Dr. N. Milovanov
Name : Martin Rinkov F109249

# Mininet and Floodlight SDN Setup

## Requirements
- Docker
- Docker Compose
- Mininet
- Floodlight

## Getting Started
1. Clone the repo:
   ```bash
   git clone https://github.com/MartinNBU/Docker-Mininet-Floodlight-Final-Task-F109249.git
   cd Docker-Mininet-Floodlight-Final-Task-F109249

docker-compose up

python/python3 configure_flows.py

mininet> pingall

https://youtu.be/ZgdPXyvzwbs - Quick reminder about the video, its only an example of how a docker-mininet-floodlight setup( in tree topology , 4 swiches , 9 hosts) is suppose to work, because I had many problems with setting up floodlight on my device and running the python scrips. Pulled the floodlight via docker (Had problems with setting up floodlight normally beacuse of thrift/netty incompatibility (checked the build.xml file aslo) then ran into pyhton problems where I can't run my own scripts even with sudo mn --custom command. 





