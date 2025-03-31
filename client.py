from socket  import *
from constCS import * #-

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)
entradas = ["add 3 2" , "subtract 3 2", "multiply 3 2", "divide 3 2"]
for input in entradas:
  s.send(str.encode(input))
  result = bytes.decode(s.recv(1024))
  print (input+" results in "+str(result))# print the result
s.close()               # close the connection
