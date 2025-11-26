import socket


class ClientTasks:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(self.client_socket.recv(4096).decode())

    def send_command(self, command):
       
        self.client_socket.sendall(command.encode())
        response = self.client_socket.recv(4096).decode()
        return response

    def close(self):
        self.client_socket.close()





print("HI CLIENT !")
client = ClientTasks("server_cont", 12345)
client.menu()


