# └─$ sudo python3 network_scanner.py                                                                                                                                                               1 ⨯

import scapy.all as scapy

'''
                                        ------------- INFO ----------------

Network Scanner Algorithm 

Goal -> Discover clients on the same network

Steps:

    1. Create arp request directed to boradcast MAC asking for IP
        -> User ARP to ask who has target IP
        -> Set destination MAC to boradcast MAC
    
    2. Send packet and receive response

    3. Parse the response

    4. Print the result

    -------- > Listing the INFO methods that scapy comes with

    print(arp_request.summary()) # Gives us a summary about the requested object
    print(scapy.ls(scapy.ARP)) # scapy.ls function actuates as the man command, giving you valuable info about how the object that you pass in
    [object].show() # Returns full information about the object and it's attributes

'''

def scan(ip):

    arp_request = scapy.ARP(pdst = ip) # Use ARP to ask who has the target IP
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff') # Set destination MAC to broadcast MAC

    arp_request_broadcast =  broadcast/arp_request # This is the combination of both NET packages. Scapy let us to combine packages with '/'
    # arp_request_broadcast.show() 

    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1) # .srp (stands for send & receive) allows us to send packages with a custom Ether part

    for element in answered_list: #answered list it's a tuple. First elemnent is the package sent, second is the response
        #print(element[1].show()) #psrc stands for the IP of the package sender, and hwsrc is the hardware physical address of the client
        print(element[1].psrc)
        print(element[1].hwsrc)
    # return answered_list.summary(), answered_list.show()

scan('192.168.0.1/24')


