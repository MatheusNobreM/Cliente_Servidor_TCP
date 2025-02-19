from socket import *
serverName = 'localhost'
serverPort = 12000

while 1:
    print("Digite a operação ou sair:")
    user_input = input()
    if user_input.lower() == 'sair':
        print("Encerrando cliente.")
        break
    break


clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
clientSocket.send(user_input.encode('utf-8'))

response = clientSocket.recv(1024).decode('utf-8')
print(f"Resposta do servidor: {response}")
clientSocket.close()