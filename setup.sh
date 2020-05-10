#!/bin/bash
pkg install figlet
pkg install ruby
gem install lolcat
pkg install neofetch
pkg install toilet
mv update-metasec /data/data/com.termux/files/usr/bin
cd
cd ..
cd usr
cd bin
chmod +x update-metasec
cd
cd METASEC
unzip ngrok.zip
mv ngrok /$HOME
rm -rf ngrok.zip
cd
cd ..
cd usr
cd etc
rm -rf bash.bashrc
cd 
cd METASEC
mv bash.bashrc /data/data/com.termux/files/usr/etc
clear
cat l.txt | lolcat
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
cat g.txt | lolcat
