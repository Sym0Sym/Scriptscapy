#!/usr/bin/python3

#MAC-IP Scanner

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

from scapy.all import *
conf.verb = 0
destino = input("Digite o IP de destino:  ")
print ("MAC:", getmacbyip(destino))# Retorna o MAC do IP de destino.
portas = [21,22,23,80,135,139,443,515,111,2005,2006,4000,8080,135,139,445,] #Colocar as portas que queira escanear
pacoteIP = IP(dst= destino)
pacoteTCP = TCP(dport=portas, flags="S")
pacote = pacoteIP/pacoteTCP
ans, unans = sr(pacote, inter=0.1, timeout=1)
print ("Porta\tEstado")
for pacoteRecebido in ans:
    print (pacoteRecebido[1][IP].sport, \
    "\t", pacoteRecebido[1][TCP].sprintf("%flags%"))
