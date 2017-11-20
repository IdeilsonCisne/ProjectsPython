#coding = utf-8

import socket

host = socket.gethostname()
port = 6767
destino = (host, port)

''' criando socket cliente '''
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def menu():
    print('**************************')
    print('****       MENU       ****')
    print('**************************')
    print('*** Escolha uma opção: ***')
    print('1 . Encerrar conexão....')
    global a
    a = input()


if __name__ == '__main__':

    print("Conectando...")
    clientsocket.connect(destino)
    print("Conexão efetuada com servidor {}".format(destino))

    #recebe menu do servidor
    recebe = clientsocket.recv(1024)
    recebe = recebe.decode('utf-8')
    print(recebe)
    confir = 'Confirmado'
    clientsocket.send(confir.encode('utf-8')) #confirmar recebimento

    # Servidor solicita login ao cliente e o mesmo envia ao servidor o login
    recebe = clientsocket.recv(1024)
    recebe = recebe.decode('utf-8')
    print(recebe)
    envia = input()
    clientsocket.send(envia.encode('utf-8'))

    # Servidor solicita senha ao cliente e o mesmo envia ao servidor a senha
    recebe = clientsocket.recv(1024)
    recebe = recebe.decode('utf-8')
    print(recebe)
    envia = input()
    clientsocket.send(envia.encode('utf-8'))

    # Recebe confirmação do servidor
    recebe = clientsocket.recv(1024)
    recebe = recebe.decode('utf-8')
    print(recebe)

    while 1:
        menu()
        if a == '1':
            # enviar ao servidor desconexão
            clientsocket.send(a.encode('utf-8'))
            print('Encerrando conexão...')
            clientsocket.close()
            break
