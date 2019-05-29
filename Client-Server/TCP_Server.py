import socket

hostName = socket.gethostname()
print("Host name is",hostName)
portNumber=eval(input("Enter a port number that is greater than 1024:"))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server_socket.bind((hostName, portNumber))
server_socket.listen(1)
con, address = server_socket.accept()  
while True:
    data = con.recv(1024).decode()
    data=data.upper()
    con.send(data.encode())  

con.close()  
