from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM) 
s.bind((HOST, PORT))  #-
s.listen(1)           #-
(conn, addr) = s.accept()  # returns new socket and addr. client 
while True:                # forever
  data = conn.recv(1024)   # receive data from client
  if not data: break       # stop if client stopped
  entrada = bytes.decode(data))
  entrada = str.split(str(entrada))
  if len(entrada) = 3:
    ope, x, y= entrada
    x = float(x)
    y = float(y)
  if (ope == "add"):
    saida = a+b
  if (ope == "subtract"):
    saida = a-b
  if (ope == "multipli"):
    saida = a*b
  if (ope == "add"):
    saida = a/b
  conn.send(str.encode(bytes.decode(data)+"*")) # return sent data plus an "*"
conn.close()               # close the connection
