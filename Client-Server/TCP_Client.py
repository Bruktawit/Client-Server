import socket

hostName=input("Enter the host:")
portNumber=eval(input("Enter the port number:"))
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
client_socket.connect((hostName, portNumber)) 

message = input("Please Enter the statement to be capitalized:")  

while True:
    client_socket.send(message.encode())  
    data = client_socket.recv(1024).decode() 
    print('Capitalized text from the server: ' + data) 
    message = input("Please Enter the statement to be capitalized:")  

client_socket.close()  


