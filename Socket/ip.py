import socket
hostN=socket.gethostname()
print('Hostname : ',hostN)
IPAdd=socket.gethostbyname(hostN)
print('IP Address : ',IPAdd)
