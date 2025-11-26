import socket
import threading


class task :
    def __init__(self,id,title,desc,stat,auth):
        self.id=id
        self.title=title
        self.desc=desc
        self.stat=stat
        self.auth=auth 


class task_manager :
    def __init__(self):
        self.task_list=[]

    def generate_id(self):
        task_list=self.task_list
        if not task_list :
            return 0
        i=0
        while i != task_list[i].id:
            i+=1
        return i

    def add_task(self,title,desc,auth):
        id_task=self.generate_id()
        new_task=task(id=id_task, title=title, desc=desc, stat="ToDo", auth=auth)
        self.task_list.append(new_task)

    def del_task(self,id):
        for t in self.task_list:
            if t.id == id:
                self.task_list.remove(t)
                break

    def list_tasks(self):
        mssg=""
        if not self.task_list:
            mssg="No Task Available !"
        else:
            for t in self.task_list:
                mssg+=f"{t.id} | {t.title} | {t.stat} | {t.auth}\n"
        return mssg



    def change_stat(self,id,stat):
        for t in self.task_list:
            if t.id == id:
                t.stat=stat 
    




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
    
    def handle_client(self,conn,adr):
        while True :
            command=conn.recv(1024).decode().strip()
            if not command :
                print(f"{adr} has Disconected ")
                break
            data=command.split(":")
            if data[0]=="ADD" :
                if len(data)!=4:
                    conn.sendall(("Error Requires 3 Arguments ! ").encode())
                else :
                    title=data[1]
                    desc=data[2]
                    auth=data[3]
                    self.task_manager.add_task(title,desc,auth)
                    conn.sendall(("Task Added ! ").encode())
            elif data[0]=="LIST":
                tasks=self.task_manager.list_tasks()
                conn.sendall(tasks.encode())

            elif data[0]=="DEL" :
                if len(data)!=2:
                    conn.sendall(("Error Require 1 Argument ! ").encode())
                else :
                    id=int(data[1])
                    self.task_manager.del_task(id)
                    conn.sendall(("Task Deleted ! ").encode())
            elif data[0]=="EXIT":
                conn.close()
                print(f"{adr} has Disconected ")
                break
            
            elif data[0] == "STAT":
                if len(data) != 3:
                    conn.sendall(("Error Require 2 Arguments: id and new_status!").encode())
                else:
                    task_id = int(data[1])
                    new_stat = data[2]
                    self.task_manager.change_stat(task_id, new_stat)
                    conn.sendall((f"Task {task_id} status changed to {new_stat}!").encode())
    
            else:
                conn.sendall(("Unkown Command ! ").encode())


        conn.close()

print("WElCOME TO TASK MANAGER SERVER :D")
task_manager_server=server("0.0.0.0",12345)
task_manager_server.server_on()
                






