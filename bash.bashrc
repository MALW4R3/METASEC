if [ -x /data/data/com.termux/files/usr/libexec/termux/command-not-found ]; then
	command_not_found_handle() {
		/data/data/com.termux/files/usr/libexec/termux/command-not-found "$1"
	}
fi

PS1='\033[01;34m\]┌──\[\033[01;46m\]HACKER\[\033[01;31m\]@\[\033[01;31m\]\t\[\033[00;34m\]\[\033[01;34m\]\w\[\033[00;34m\]\[\033[01;32m\]:
\[\033[01;34m\]└╼\[\033[01;31m\]•>\[\033[01;36m\]'
clear
figlet HACK3R | lolcat
neofetch --ascii_distro Kali
