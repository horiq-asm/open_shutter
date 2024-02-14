#!/usr/bin/python3
from __future__ import print_function
from struct import *

import socket
import subprocess

print( "Content-Type: text/html")
print( "")

#UDP_IP = "ff02::1%eth0"                 # LINK LOCAL MULTI CAST ADDRESS
#R_UDP_IP = "::"

shell_command = 'ip n | grep xx:yy:ff:02:xx:yy | cut -f 1 -d " "'
output = subprocess.check_output(shell_command, shell=True, text=True)
UDP_IP = output.strip()
R_UDP_IP = '0.0.0.0'

UDP_PORT = 3610

#sockr = socket.socket(socket.AF_INET6, type=socket.SOCK_DGRAM)
sockr = socket.socket(socket.AF_INET, type=socket.SOCK_DGRAM)
sockr.bind((R_UDP_IP, UDP_PORT))

#print "UDP target IP:", UDP_IP
#print "UDP target port:", UDP_PORT

echonetLiteFrame = ""
echonetLiteFrame += "1081"      # EHD (EL p.3-2)
echonetLiteFrame += "0000"      # TID (EL p.3-3)
# EDATA
echonetLiteFrame += "05FF01"  # SEOJ (EL p.3-3 AppH p.3-408)
echonetLiteFrame += "05FD01"  # DEOJ (EL p.3-3 AppH p.3-274)
echonetLiteFrame += "61"          # ESV(62:) (:EL p.3-5)
echonetLiteFrame += "01"          # OPC(1)(EL p.3-7)
echonetLiteFrame += "80"          # EPC(:EL p.3-7 AppH p.3-275)
echonetLiteFrame += "01"          # PDC(EL p.3-9)
echonetLiteFrame += "31"          # EDT(EL p.3-9)

MESSAGE = echonetLiteFrame

#sock = socket.socket(socket.AF_INET6,socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.sendto(bytes.fromhex(MESSAGE), (UDP_IP, UDP_PORT))
#print( "send message:",UDP_IP," ", MESSAGE.encode('hex'))

sock.close()

sockr.settimeout(10)

data, addr = sockr.recvfrom(1024) # buffer size is 1024 bytes
seoj = data[4:4+3]
#print( seoj.encode('hex') )
#print( "received message:", addr[0], data.encode('hex'))
print( seoj.hex() )
print( "received message:", addr[0], data.hex())
print(  "")

sockr.close()
