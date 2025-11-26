import socket
import threading

class task :
    def __init__(self,id,title,desc,stat,auth):
        self.id=id
        self.title=title
        self.desc=desc
        self.stat=stat
        self.auth=auth 


class server :
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.task_manager=task_manager()

    def server_on(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print("Server On ! ")
        print("Listening ...")
        while True :
            conn,adr=self.server_socket.accept()
            print(f"{adr} Is Connected ")
            conn.sendall(("Welcome To Task Manger Server :D").encode())
            client_thread=threading.Thread(target=self.handle_client, args=(conn,adr)).start()
    
        


task_manager_server=server("0.0.0.0",12345)
task_manager_server.server_on()
                






