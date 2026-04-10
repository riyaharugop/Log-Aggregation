import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

message = input("Enter log message: ")
client.send(message.encode())

client.close()
