import socket
import threading

def receive_data(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        print(data)

def start_client():
    server_ip = '10.160.65.43'
    server_port = 5555
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    threading.Thread(target=receive_data, args=(client_socket,)).start()

    while True:
        command = input("Enter 'roll' to roll the dice: ")
        client_socket.send(command.encode())

if __name__ == "__main__":
    start_client()