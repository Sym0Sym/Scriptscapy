#!/usr/bin/python3

#IP MAC and Scanner

print ("          _     _ _         _                    _  ")
print ("         | |   (_) |       | |                  | | ")
print ("__      _| |__  _| |_ ___  | |__   ___  __ _  __| | ")
print ("\ \ /\ / / '_ \| | __/ _ \ | '_ \ / _ \/ _` |/ _` | ")
print (" \ V  V /| | | | | ||  __/ | | | |  __/ (_| | (_| | ")
print ("  \_/\_/ |_| |_|_|\__\___| |_| |_|\___|\__,_|\__,_| ")
print ("")
print ("$$BY Sym0SYm$$")
print ("")

from scapy.all import *
conf.verb = 0
destino = input("Digite o IP de destino:  ")
print ("MAC:", getmacbyip(destino))
portas = [22,80]
pacoteIP = IP(dst= destino)
pacoteTCP = TCP(dport=portas, flags="S")
pacote = pacoteIP/pacoteTCP
ans, unans = sr(pacote, inter=0.1, timeout=1)
print ("Porta\tEstado")
for pacoteRecebido in ans:
    print (pacoteRecebido[1][IP].sport, \
    "\t", pacoteRecebido[1][TCP].sprintf("%flags%"))
