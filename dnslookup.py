import os
import sys
import threading
import socket
import termcolor as tm
import signal
import pyfiglet

def sig_handler(recieved_sig, frame):
	print("\nCtr-C detected, Exiting..............!")
	sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)
def print_banner():
	figfont = 'slscript' #you can list fonts by typing pyfiglet --list fonts
	figinit = pyfiglet.Figlet(font=figfont)
	aflab_banner = "LVSEC"
	print(tm.colored(figinit.renderText(aflab_banner),'yellow'))

print_banner()


def scan(h,dm):
	host = f"{h}.{dm}"
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		ip = socket.gethostbyname(host)
		print(tm.colored(host,'magenta')+f" {tm.colored('has address','green')} "+tm.colored(ip,'yellow'))
	except Exception as e:
		pass
	
	

if __name__ == "__main__":
	domain_name = str(input(f"{tm.colored('Domain','yellow')}:"))
	t = list()
	with open("domains_big.txt",'r') as dom:
		for i in dom.readlines():
			if not i == " ":
				t1 = threading.Thread(target=scan(i.strip(),domain_name),name="h")
				t.append(t1)
				t1.start()
