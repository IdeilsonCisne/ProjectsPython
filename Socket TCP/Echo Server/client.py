# coding=utf-8
import os
import socket
import time
import sys


#Criando um socket Objeto

#serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Get Local machine name

host = socket.gethostname()
port = 6666
destino = (host, port)

#conectando ao servidor

#s.connect((host, port))
#s.connect(destino)

def menu(NumEscolha):
    NumEscolha = int(input('''
    Menu
    0 - Solicitar informação de Processador do Servidor
    1 - Solicitar informação do Data/Hora do Servidor
    2 - Solicitar informação de SO do Servidor
    3 - Solicitar informação Nome do Host
    4 - Solicitar informações Versão Python
    5 - Solicitar informações IP do Servidor
    6 - Solicitar detalhes do SO
    7 - Solicitar da arquitetura do processador
    8 - Solicitar
    9 - Solicitar
    10 - Fechar conexão com Servidor Socket
    Escolha uma das opções: '''))

    #if (NumEscolha != '0123456789'):

    return NumEscolha

def escolha(escolha):
    #s.connect(destino)

    if (escolha == 0):
        print('Opção 0 escolhida - detalhe do processador')

        mensagem = "0"
        s.send(mensagem.encode('ascii'))
        get_pro = s.recv(1024)
        print("O processador da máquina é %s" % get_pro.decode('ascii'))

    elif (escolha == 1):
        print('Opção 1 escolhida - Data/Hora')

        mensagem = "1"
        s.send(mensagem.encode('ascii')) # enviar mensagem para o servidor
        tempo = s.recv(1024) #resposta da mensagem do servidor
        print("A hora Recebida do Servidor é %s" % tempo.decode('ascii'))


    elif (escolha == 2):
        print('Opção 2 escolhida - Sistema Operacional')

        mensagem = "2"
        s.send(mensagem.encode('ascii'))
        GetSO = s.recv(1024)
        print("Detalhes sobre o SO : %s" % GetSO.decode('ascii'))


    elif (escolha == 3):
        print('Opção 3 escolhida - Nome da Host')

        mensagem = "3"
        s.send(mensagem.encode('ascii'))
        get_Nome = s.recv(1024)
        print("O nome da máquina é %s" % get_Nome.decode('ascii'))

    elif (escolha == 4):
        print('Opção 4 escolhida - ')

        mensagem = "4"
        s.send(mensagem.encode('ascii'))
        get_py = s.recv(1024)
        print("A versão do Python é %s" % get_py.decode('ascii'))

    elif (escolha == 5):
        print('Opção 5 escolhida - IP do servidor')

        mensagem = "5"
        s.send(mensagem.encode('ascii'))
        get_ip = s.recv(1024)
        print("O ip da máquina é %s " % get_ip.decode('ascii'))

    elif (escolha == 6):
        print('Opção 6 escolhida - detalhe do Sistema Operacional')

        mensagem = "6"
        s.send(mensagem.encode('ascii'))


    elif (escolha == 7):
        print('Opção 7 escolhida - Socket')

    elif (escolha == 8):
        print('Opção 8 escolhida - Socket')

    elif (escolha == 9):
        print('Opção 9 escolhida - Socket')


    elif (escolha != '0123456789'):
        print('Opção 10 escolhida - Fechar conexão Socket')
        mensagem = "10"
        s.send(mensagem.encode('ascii'))

        s.close()

    else:
        print('Escolha inválida, tente novamente')


if __name__ == '__main__':

    s.connect(destino)
    while True:
        Num = menu(NumEscolha=int)
        escolha(Num)
