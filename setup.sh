#!/bin/bash
cat l.txt
curl -LO https://github.com/termux/termux-packages/files/3995119/metasploit_5.0.65-1_all.deb.gz
gunzip metasploit_5.0.65-1_all.deb.gz
dpkg -i metasploit_5.0.65-1_all.deb
apt -f install
mv metasec /data/data/com.termux/files/usr/bin
cd ..
cd ..
cd usr
cd bin
chmod +x *
cd /$HOME/METASEC
clear
cat g.txt

