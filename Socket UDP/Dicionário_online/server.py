import socket
MAX_BYTES = 65535

# criando um socket objeto UDP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#nome da máquina
host = socket.gethostname()
port = 6667
destino = (host, port)

# bind to port
serversocket.bind((host, port))
print("Aguardando conexão...")

# #Dicionário

DicionarioCapital = {
    'Acre':               'Rio Branco',
    'Alagoas':            'Maceió',
    'Amapar':             'Macapá',
    'Amazonas':           'Manaus',
    'Bahia':              'Salvador',
    'Ceará':              'Fortaleza',
    'Distrito Federal':   'Brasília',
    'Goiás':              'Goiânia',
    'Maranhão':           'São Luís',
    'Mato Grosso':        'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais':       'Belo Horinzonte',
    'Pará':               'Belém',
    'Paraíba':            'João Pessoa',
    'Paraná':             'Curitiba',
    'Pernambuco':         'Recife',
    'Piauí':              'Teresina',
    'Rio de Janeiro':     'Rio de Janeiro',
    'Rio Grande do Norte':'Natal',
    'Rio Grande do Sul':  'Porto Alegre',
    'Rondônia':           'Porto Velho',
    'Roraima':            'Boa Vista',
    'Santa Catarina':     'Florianópolis',
    'São Paulo':          'São Paulo',
    'Sergipe':            'Aracaju',
    'Tocantins':          'Palmas',

}

def accept_connection():
    #Receber dado do cliente
    #mensagem = mensagems recebida pelo cliente
    #client = socket, variável com ip e porta do cliente
    mensagem, client = serversocket.recvfrom(MAX_BYTES)
    mensagem_deco = mensagem.decode('utf-8')
    print(mensagem_deco)

    #Enviar dado para o cliente
    msg_enviar = "Conexão estabelecida... Servidor {}".format(destino)
    msg_enviar = msg_enviar.encode('utf-8')
    serversocket.sendto(msg_enviar, client)
    print("Solicitação aceita")
    print("Conexão estabelecida... Cliente", client)


def OP1():
    print("Pesquisando termo...")
    # Esperando receber termo a ser pesquisado no dicionário
    termo_recebido, client = serversocket.recvfrom(MAX_BYTES)
    termo_recebido = termo_recebido.decode('utf-8')

    #Pesquisa no dicionário
    if (DicionarioCapital.get(termo_recebido)):
        termo_pesquisado = DicionarioCapital.get(termo_recebido)
        termo_pesquisado = termo_pesquisado.encode('utf-8')
        serversocket.sendto(termo_pesquisado, client)
    #Caso não encontrado no dicionario
    else:
        msg = "Termo não encontrado no dicionário"
        msg = msg.encode('utf-8')
        serversocket.sendto(msg, client)

def OP2():
    print("Incluindo novo termo...")
    #Recendo novo termo
    termo_recebido1, client = serversocket.recvfrom(MAX_BYTES)
    termo_recebido1 = termo_recebido1.decode('utf-8')

    #Recendo significado do termo
    termo_recebido2, client = serversocket.recvfrom(MAX_BYTES)
    termo_recebido2 = termo_recebido2.decode('utf-8')

    DicionarioCapital[termo_recebido1] = str(termo_recebido2)

    enviar_retorno = "Novo termo add com sucesso!"
    enviar_retorno = enviar_retorno.encode('utf-8')
    serversocket.sendto(enviar_retorno, client)


def OP3():
    print("Fechando conexão...")
    serversocket.close()

if __name__ == '__main__':

    accept_connection()
    while True:
        #accept_connection()

        #Esperando receber uma opção do cliente
        mensagem, client = serversocket.recvfrom(MAX_BYTES)
        mensagem_deco = mensagem.decode('utf-8')

        if (mensagem_deco == "1"):
            OP1()

        elif (mensagem_deco == "2"):
            OP2()

        elif (mensagem_deco == "3"):
            OP3()
            break
