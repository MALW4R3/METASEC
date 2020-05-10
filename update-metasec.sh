#!/bin/bash
cd 
rm -rf METASEC
git clone https://github.com/MALW4R3/METASEC
cd ..
cd usr
cd bin
rm -rf metasec
cd
cd METASEC
sh setup.sh
cat k.txt | lolcat
