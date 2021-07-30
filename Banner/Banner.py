#!/usr/bin/python3

#Retorna o Banner de APLICAÇÃO


print ('\033[32m'"Port-Scanner"'\033[32m')
print ('\033[37m'"          _     _ _         _                    _  "'\033[37m')
print ('\033[37m'"         | |   (_) |       | |                  | | "'\033[37m')
print ('\033[37m'"__      _| |__  _| |_ ___  | |__   ___  __ _  __| | "'\033[37m')
print ('\033[37m'"\ \ /\ / / '_ \| | __/ _ \ | '_ \ / _ \/ _` |/ _` | "'\033[37m')
print ('\033[37m'" \ V  V /| | | | | ||  __/ | | | |  __/ (_| | (_| | "'\033[37m')
print ('\033[37m'"  \_/\_/ |_| |_|_|\__\___| |_| |_|\___|\__,_|\__,_| "'\033[37m')
print ("")
print ("                     $$ BY:Sym0Sym $$                                   ")
print ("")



import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("0.0.0.0", 00))#IP e Porta
print ("Banner: ")
print (sock.recv(2048))
sock.close()
