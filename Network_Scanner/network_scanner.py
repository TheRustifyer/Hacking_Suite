# └─$ sudo python3 network_scanner.py                                                                                                                                                               1 ⨯

import scapy.all as scapy

def scan(ip):
#     scapy.arping(ip)

    arp_request = scapy.ARP(pdst = ip)
    # arp_request.pdst = ip
    print(arp_request.summary()) # Gives you a summary about the requested object
    print(scapy.ls(scapy.ARP)) # scapy.ls function actuates as the man command, giving you valuable info about how the object that you pass in

scan('192.168.0.1/24')