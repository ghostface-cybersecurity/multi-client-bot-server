import sys
import socket

serverName = sys.argv[1] # first arg - server IP
serverPort = 8000 

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create socket IPv4 & TCP-port

clientSocket.connect((serverName,serverPort))
mes = 'Connected'.encode('utf-8')

clientSocket.sendall(mes)
response = clientSocket.recv(1024)
print('From server:',response.decode('utf-8'))

clientSocket.close()
