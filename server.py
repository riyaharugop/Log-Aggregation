import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(5)

print("Server is listening...")

while True:
    client_socket, addr = server.accept()
    print(f"Connected to {addr}")

    data = client_socket.recv(1024).decode()

    print("Log received:", data)

    with open("logs.txt", "a") as file:
        file.write(data + "\n")

    client_socket.close()
