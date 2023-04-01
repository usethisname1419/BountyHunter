import time
import requests
import socket
import random
import sys
import subprocess
from colorama import init, Fore, Back, Style
from datetime import datetime

init(autoreset=False)

subprocess.call('clear', shell=True)

ips = open('targets.txt')
with open('proxyf.txt', 'r') as f:
    proxy = f.read().splitlines()
proxies = {
    'http': (proxy,)
}
############################INTRO ANIMATE######################################
Corexital = False
t1 = datetime.now()
print(Style.BRIGHT + Back.YELLOW + "STARTED AT: ", str(datetime.now()))
print("")

time.sleep(1)
Corexital = True
print("")


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.015)


print_slow(Style.BRIGHT + Back.YELLOW + "PORT 22 BOUNTYHUNTER  --   COREXITAL DATA   -- 2023    ")
print(Style.RESET_ALL + "")


##########################################################TITLE##############
def title():
    print(Style.BRIGHT + Fore.GREEN + "==============COREXITAL DATA========================")
    print(Style.BRIGHT + Fore.GREEN + "==============BOUNTY HUNTER v1.2====================")
    print("")
    print(Style.BRIGHT + Fore.GREEN + "Written by:    DEREK JOHNSTON")
    print("")


title()

print(
    Style.BRIGHT + Fore.GREEN + "Populate target list by entering seed IP value. BountyHunter checks to see if port 22 is open.")
print(Style.BRIGHT + Fore.GREEN + "If port 22 is open BountyHunter will execute a bruteforce attack")
print(Style.RESET_ALL + "")
##################TARGET POPULATION####################################
tarlist = ('targets.txt')
seed = input("Enter First Octet (example'192' '172' '10'):   ")
print("LOADING...")


def make_list():
    for x in range(250):
        octet2 = (random.randrange(255))
        octet3 = (random.randrange(255))
        octet4 = (random.randrange(255))

        with open(tarlist, 'w+') as tl:
            ipadd = (seed, '.' + str(octet2), '.' + str(octet3), '.' + str(octet4).lstrip(' '))
            tl.writelines(ipadd)


for l in range(250):
    make_list()
print("INIT...")


##################ENDING LIST POPULATION##########################

def attack():
    
    
    port = 22
    address = x
    print(Style.BRIGHT + Fore.YELLOW + 'Scanning:', x)

    
    
    print(Style.RESET_ALL + "")
    

    try:
        
            requests.get(url='https://google.com', proxies=proxies)
            remoteaddr = socket.gethostname()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(2)
            result = s.connect((remoteaddr, port))
            print(Style.BRIGHT + Fore.GREEN + Back.RED + "AT: " + Style.BRIGHT + Fore.RED + Back.GREEN + "TIMESTAMP", str(datetime.now()))
            if result ==0:
                print(Style.RESET_ALL + "Port 22:OPEN")

            else:
                print(Style.RESET_ALL + "Port 22:CLOSED")
            s.close()
         
    except KeyboardInterrupt:
        print("Cancelled")
        sys.exit()
    except socket.gaierror:
        print("Not Resolving ")

    except socket.error:
        print("its fuked up man")

with open(tarlist, 'r') as rl:
        x = rl.readlines()

attack()

print(Style.RESET_ALL + "Stopping..")
print(Style.BRIGHT + Fore.RED + "Attack Stopped At:", str(datetime.now()))
