# Network-simulator

Flask 
pip install Flask

Introduction: 

The data transmission in the network is done by flask which is a web application written in python. We chose it because Flask lets us focus on what the users are requesting and what sort of response to give back since our network would include clients rejecting data if it was not meant for them, or clients giving acknowledgement when they receive the message intended for them.

For the purpose of developing dedicated connections between devices/clients, we are using HTTP connections between clients and network devices running on different ports. The IP address remains the same for all applications as we have implemented it in a single system.  The network consists of clients and servers as flask web servers in separate files. The network consists of five client devices and a server which incorporates the networking devices,i.e hub, switch and bridge. There is also a client sender that is used to control the various functionalities during run time, like configuring various network devices in a topology based on the user’s choice, choosing layer 2 devices to be used, and finally sending data taken from the user to the chosen devices/flask servers. The access control protocol(here, pure Aloha) and flow control protocols are implemented in separate files.
Language and framework used: Python and Flask(a micro web framework written in Python) 


Assumptions:

 Although the local area network (as our project) considers mac addresses for the client to client delivery, we are considering the combination of IP address and port no. as our address for the identification of the targetted device. This is because flask servers are connected via these IP addresses. Therefore, the tables are populated with one entry as port no. and the other as (IP address + port no.)


Input/output format:

The input is taken from the user in integer and string formats. The choice of modality, sender and receiver are taken in form of integers. String data, that is to be sent,  is also taken from the user during run time.

The output is displayed as the received message in string format and a success message at the client sender terminal. The output may also consist of the table maintained by the devices depending on the modality.



Various flask servers as devices/clients:

1)Server.py - 
Here we are importing the Flask module and creating a Flask web server from the Flask module. 
The request module is imported to create a request session
From urlib3.util.reply, we are importing ‘retry’ by virtue of which each retry attempt will create a new Retry object with updated values, so they can be safely reused.
From requests.adapters, we are importing HTTPAdapter which sends an HTTP or HTTPS request to a URL and processes the response to return the web page in XML format.
Server.py will be running on http://127.0.0.1:5000/
__name__ means this current file. In this case, it will be main.py. This current file will represent our web server.
It includes the IP address and port number of the devices available to us.
It includes the address tables named as CAM_table and B_table required for switches and bridges.
We are creating instances of the Flask class and calling it an app, that has a route decorator to URL to the functions. These functions are hub_world, switch_world, bridge_world and direct including functionalities of a hub, switch, bridge and a direct connection respectively. These functions will print the responses sent by clients, whether they accepted or rejected the message.

2)Client1.py, Client2.py, Client3.py, Client4.py and Client5.py -

These are, again, flask servers running on ports 5001,5002,5003,5004 and 5005 respectively.
These also have functions for each client that sends the response to the server after they receive the data.

               
3)Client_sender.py -
            
It's primarily for receiving the user’s input for setting up the topology(here, star) using different layer 2 devices.
The modules and some of the functionalities used here is similar to the server.py
It also includes the IP addresses and port numbers of layer 2 devices like the hub, switch, etc.

4)Pure_Aloha.py

This file is implemented separately from the flask servers.
It demonstrates the working model of pure aloha by randomly selecting ‘R’ to generate backoff time that is used the change the time slots of the transmissions by altering the starting and finishing time in the lists st[] and ft[].


5)Stop_and_wait_sender.py and stop_wait_receiver.py -
                 Stop and wait protocol using python and socket programming.

How to run the code:

The first step is to execute the python files on different terminals so that they can run parallelly
Client_sender.py will ask for user inputs at runtime and the whole system is controlled through this file.
After giving the desired values the user can check outputs in multiple clients or check the server for overall understanding. 

