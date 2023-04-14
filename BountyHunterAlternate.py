import socket
import sys
from datetime import datetime





############# Import Modules. Modules are installed by using " pip install (pkname)"###############
#############Modules are other pieces if code available with python. very helpful to sav time##########

print("=====================COREXITAL SSH BOUNTY HUNTER=======================")
############## Saving input value as a variable####################



fp = open("targetlist.txt", "r")
val = fp.readline().split()
print("GETTING BOUNTY:     ", "HOSTNAME", val)

str1 = val

for ele in val:
    str1 += ele

hack = val

t1 = datetime.now()
print(t1)
##############We use the modules datime to print the current time#################

def starthack():
    ######################### Fuctions: def means Define. functions are called with the () characters##############
        try:
            port = 22
    ####################### This is a loop, targeting all ports in that range.####################
            hacking = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            hacking.settimeout(10)
            result = hacking.connect_ex((hack, port))
            if result ==0:
                print(hack)
                print("PORT:", port,"    OPEN           AT IP:", val)
                hacking.close()
                print(t1)
            else:
                print(hack)
                print("PORT:", port, "    CLOSED        AT IP:", val)
                hacking.close()
                print(t1)
        except KeyboardInterrupt:
            print(t1)
            print("Canceled")
            sys.exit()

        except socket.gaierror:
            print(t1)
            print("Hostname could not be resolved. Exiting")
            sys.exit()
        except socket.error:
            print(t1)
            print("Error")
            print("ERROR")
            sys.exit()
for lines in fp.readlines():
    starthack()

###########Calling a fuction##################33

print("END OF REPORT")
print("Corexital")
