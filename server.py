from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  entrada = bytes.decode(data)
  entrada = str.split(str(entrada))
  if len(entrada) == 3:
    ope, x, y= entrada
    x = float(x)
    y = float(y)
  if (ope == "add"):
    saida = x+y
  elif (ope == "subtract"):
    saida = x-y
  elif (ope == "multiply"):
    saida = x*y
  elif (ope == "divide"):
    if y==0:
      saida="Erro"
    else:
      saida=x/y
  else:
    saida="Entradas inválidas"
  conn.send(str.encode(str(saida))) # return sent data, com operações feitas
conn.close()               # close the connection
