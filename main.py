import nmap
import requests

nm = nmap.PortScanner()
ips = open('targets.txt')
with open('proxyf.txt', 'r') as f:
    proxy = f.read().splitlines()
proxies = {
    'http': (proxy)
}

def attack():
    x = ips.readline()
    requests.get(url='https://google.com', proxies=proxies)
    results = nm.scan(x, '22')
    print('Scanning:', x)
    print(results)

for targets in range(100):
    attack()

