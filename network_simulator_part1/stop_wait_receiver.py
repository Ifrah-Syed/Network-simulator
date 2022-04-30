import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="localhost"
port =8000
s.connect((host,port))
while (1):
   data=s.recv(1024).decode()
   print("Received data"+data)
   str="Acknowledgement provided"
   s.send(str.encode())

s.close ()