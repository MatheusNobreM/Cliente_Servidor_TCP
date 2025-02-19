import time
from socket import *
import threading

def handle_client(connectionSocket):
     try:
          request = connectionSocket.recv(1024).decode('utf-8')
          print(f"Requisição recebida: {request}")

          parts = request.split()
          if len(parts) != 3:
               response = "Erro: formato inválido"
          else:
               opr1, opd, opr2 = parts
               try:
                    opr1 = float(opr1)
                    opr2 = float(opr2)

                    if opd == '+':
                         res = opr1 + opr2
                    elif opd == '-':
                         res = opr1 - opr2
                    elif opd == '*':
                         res = opr1 * opr2
                    elif opd == '/':
                         if opr2 == 0:
                              response = "Erro: divisão por zero"
                         else:
                              res = opr1 / opr2
                    else:
                         response = "Erro: operador inválido"

                    if 'response' not in locals():
                         response = str(res)
               except ValueError:
                    response = "Erro: operandos inválidos"
          
          connectionSocket.send(response.encode('utf-8'))
     except Exception as e:
        print(f"Erro no processamento: {e}")
     finally:
        connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print("The server is ready to receive")
while 1:
     connectionSocket, addr = serverSocket.accept()
     threading.Thread(target=handle_client, args=(connectionSocket,)).start()