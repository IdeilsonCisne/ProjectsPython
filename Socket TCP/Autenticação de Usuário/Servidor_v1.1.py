# coding = utf-8
import socket

''' Nome da máquina '''
host = socket.gethostname()
port = 6767

''' criando socket server '''
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

''' Resolve problema de "socket.error: [Errno 98] Address already in use '''
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

''' bind to the port '''
serversocket.bind((host, port))

''' Colocar em queue 10 requisições '''
serversocket.listen(10)

db = {'João': 1234, 'Mateus': 4321, 'Lucas': 1122, 'Pedro': 2211}


def autenticacao(recebe_l, recebe_s):
    # conferindo se usuário e senha existe
    print('Valores digitados pelo usuário ', recebe_l, recebe_s)
    v1, v2 = 0, 0
    for usuario in db.keys():
        if (usuario == recebe_l):
            #print(usuario)
            v1 = 1
            for senha in db.values():
                if (senha == recebe_s):
                    #print(senha)
                    v2 = 1
    if v1 + v2 == 2:
        print('Usuário e senha conferem')
        mensagem_confirm = 'Bem Vindo ao Servidor\n'
        clientsocket.send(mensagem_confirm.encode('utf-8'))
    else:
        print('Senha não confere')


if __name__ == '__main__':
    print('Aguardando conexão...')
    clientsocket, addr = serversocket.accept()  # Estabelecendo uma conexão
    print('Conectado com {}'.format(addr))

    mensagem_login = 'Login:'
    mensagem_senha = 'Senha:'
    menu = '*******************************************\n****       Digite login e senha.       ****\n*******************************************\n'

    clientsocket.send(menu.encode('utf-8'))
    recebe_confir = clientsocket.recv(1024) #só para receber confirmação
    #print(recebe_confir)

    clientsocket.send(mensagem_login.encode('utf-8'))  # envia string Login ao cliente
    recebe_login = clientsocket.recv(1024)  # recebe resposta do cliente
    recebe_login = recebe_login.decode('utf-8')
    print(recebe_login)

    clientsocket.send(mensagem_senha.encode('utf-8'))  # envia string Senha ao cliente
    recebe_senha = clientsocket.recv(1024)  # recebe resposta senha do cliente
    recebe_senha = int(recebe_senha.decode('utf-8'))

    autenticacao(recebe_login, recebe_senha)

    recebe_close = clientsocket.recv(1024)
    recebe_close = int(recebe_close.decode('utf-8'))

    while 1:
         if recebe_close == 1:
             serversocket.close()
             break








