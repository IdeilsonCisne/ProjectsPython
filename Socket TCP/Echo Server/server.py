import socket
import time
import platform

#criando socket server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Resolve problema de "socket.error: [Errno 98] Address already in use"
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#nome da maquina
host = socket.gethostname()
port = 6666

# bind to port

serversocket.bind((host, port))

# colocar em queue 10 requisições
serversocket.listen(10)

def OP0():
    get_processador = platform.processor()
    clientsocket.send(get_processador.encode('ascii'))

#Função para retornar hora
def OP1():
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    #clientsocket.close()

#Função para retornar informações do Sistema Operacional
def OP2():
    get_det = platform.platform()
    clientsocket.send(get_det.encode('ascii'))
    #clientsocket.close()

def OP3():
    NM = platform.node()
    clientsocket.send(NM.encode('ascii'))
    #clientsocket.close()

def OP4():
    get_py = platform.python_version()
    clientsocket.send(get_py.encode('ascii'))
    #clientsocket.close()

def OP5():
    get_ip = socket.gethostbyname(socket.gethostname())
    clientsocket.send(get_ip.encode('ascii'))

def OPFechar():
    clientsocket.close()
    print('Conexão fechada')

if __name__ == '__main__':
    print('Aguardando conexao')
    clientsocket, addr = serversocket.accept()  # Estabelecendo uma conexão
    print("Conectado com  client %s" % str(addr))
    A = True

    while ( A ):
        #print('Aguardando conexao')
        #clientsocket, addr = serversocket.accept()  # Estabelecendo uma conexão
        #print("Conectado com  client %s" % str(addr))

        # Receber dado do Client
        recebe = clientsocket.recv(1024)
        recebe = recebe.decode('ascii')
        print("Valor recebido é ")
        print(recebe)
        # OP1()
        if (recebe == "0"):
            OP0()
        if (recebe == "1"):
            OP1()
        elif (recebe == "2"):
            OP2()
        elif (recebe == "3"):
            OP3()
        elif (recebe == "4"):
            OP4()
        elif (recebe == "5"):
            OP5()

        else:
            OPFechar()