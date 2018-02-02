# Script feito por Matheus Silva
# 01/02/2018 23:57 programado para GNU/LINUX
# Depencias airodump-ng instalado +python3 + rede wireless
# Obs:script totalmente funcianal e destinado a uso publico
# sendo que qualquer alteração na interface de rede tem que ser mudada a mão . 

import os
import time
print("Listar redes wireless: ")
time.sleep(5)
os.system("ifconfig")
print("airmon-ng check kill")
os.system("airmon-ng check")
time.sleep(5)
print("Criando interface mon0 ")
os.system("iw dev wlan0 interface add mon0 type monitor")
os.system("ifconfig mon0 up")
print("Rede mon0 ativada")
time.sleep(5)
os.system("airodump-ng mon0")
print("Rede mon0 desativada")
os.system("ifconfig mon0 down")






