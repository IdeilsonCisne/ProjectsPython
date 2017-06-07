# coding = utf-8
import socket
MAX_BYTES = 65535

# criando um socket objeto UDP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = socket.gethostname()
port = 6667
destino = (host, port)

def menu():
    print("\n******************************")
    print("**           MENU           **")
    print("******************************\n")
    print("** 1 - Consultar capitais   **")
    print("** 2 - Incluir novo termo   **")
    print("** 3 - Sair do programa     **")
    print("******************************")

    global NumEscolha
    NumEscolha = int(input("** Escolha uma opção:  "))
    print('\n\n')

def conectar():
    print("\nPara conectar ao servidor você precisa pressionar Qualquer Tecla...")
    guarda_tecla = input("aperte uma tecla...")
    print(guarda_tecla)

    #Enviando dado para o servidor
    print("Iniciando conexão...")
    msg_envia = "Cliente solicitando conexão..."
    msg_envia = msg_envia.encode('utf-8')
    clientsocket.sendto(msg_envia, destino)

    #recendo dado do servidor
    msg_recebe, addr = clientsocket.recvfrom(MAX_BYTES)
    msg_recebe = msg_recebe.decode('utf-8')

    print(msg_recebe)

def escolha(num):

    # Consultar Capitais
    if (num == 1):
        mensagem = "1"
        mensagem = mensagem.encode('utf-8')
        clientsocket.sendto(mensagem, destino)

        print("Qual estado você gostaria de saber a capital?")
        estado = input("Digite o nome do estado do Brasil: ")
        estado2 = estado.encode('utf-8')
        clientsocket.sendto(estado2, destino)

        recebe, addr = clientsocket.recvfrom(MAX_BYTES)
        recebe = recebe.decode('utf-8')
        print('A capital do Estado do "{}" é "{}" '.format(estado, recebe))

    #Incluir termo
    elif (num == 2):
        print("Incluíndo novo termo...")
        mensagem = "2"
        mensagem = mensagem.encode('utf-8')
        clientsocket.sendto(mensagem, destino)

        novo_termo = input("Digite o nome do novo termo: ")
        novo_termo = novo_termo.encode('utf-8')

        significado_termo = input("Digite agora o significado do novo termo: ")
        significado_termo = significado_termo.encode('utf-8')

        clientsocket.sendto(novo_termo, destino)
        clientsocket.sendto(significado_termo, destino)

        recebe, addr = clientsocket.recvfrom(MAX_BYTES)
        recebe = recebe.decode('utf-8')
        print(recebe)

    #Sair do programa
    elif (num == 3):
        msg_envia = "3"
        msg_envia = msg_envia.encode('utf-8')
        clientsocket.sendto(msg_envia, destino)
        print("Conexão fechada...")
        clientsocket.close()


if __name__ == '__main__':

    conectar()
    while True:
        #conectar()
        menu()
        escolha(NumEscolha)
        if (NumEscolha == 3):
            break