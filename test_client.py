import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 4433))
# while 1:
# data = client_socket.recv(512)
# if ( data == 'q' or data == 'Q'):
#    client_socket.close()
#    break;
# else:
data = 'CONNECT asdfasdf'
client_socket.send(data)
r=client_socket.recv(1024)
print ("RECEIVED:", r)

client_socket.close()
#        break;
#   else:
#      client_socket.send(data)
print ("socket colsed... END.")
