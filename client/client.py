import socket
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

    def menu(self):
        
        while True:
            print("\n_____________MENU_____________")
            print("1 _ ADD TASK")
            print("2 _ DELETE TASK")
            print("3 _ LIST TASKS")
            print("4 _ CHANGE STATUS")
            print("5 _ EXIT")
            cmd = input("Command: ").strip()

            if cmd == "1": 
                title = input("Task Title: ").strip()
                desc = input("Task Description: ").strip()
                auth = input("Task Author: ").strip()
                command = f"ADD:{title}:{desc}:{auth}"
                print(self.send_command(command))

            elif cmd == "2":  
                task_id = input("Task ID to delete: ").strip()
                command = f"DEL:{task_id}"
                print(self.send_command(command))

            elif cmd == "3": 
                print(self.send_command("LIST"))

            elif cmd == "4":  
                task_id = input("Task ID to change: ").strip()
                new_stat = input("New Status (ToDo/Doing/Done): ").strip()
                command = f"STAT:{task_id}:{new_stat}"
                print(self.send_command(command))

            elif cmd == "5":  
                self.send_command("EXIT")
                self.close()
                print("Disconnected from server.")
                break

            else:
                print("Invalid command! Choose 1-5.")





client = ClientTasks("server_cont", 12345)
client.menu()


