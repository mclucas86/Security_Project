#  Module for NMAP Scanning, includes menu
import nmap
import os
import ip_address
#  import time


#  Method will scan the network looking for active hosts. Any hosts which are returned will
#  be added to a list which is contained within the config.py file
def populatehosts(ip):
    import main_menu
    import config
    os.system("clear")
    nm = nmap.PortScanner()
    print("Currently scanning for active hosts on: " + ip)
    print(nm.scan(ip, '22-443', '--stats-every 10s'))
    os.system("clear")
    print("*************************************************")
    print("*            Active Hosts Detected:             *")
    print("*************************************************")
    for hosts in nm.all_hosts():
        if nm[hosts].state() == "up":
            config.listofhosts.append(hosts)
            print("Adding " + hosts + " to the list of hosts")
    config.listofhosts = sorted(config.listofhosts, key=ip_address.ip_to_tuple)
    if len(config.listofhosts) != 0:
        print("Added " + str(len(config.listofhosts)) + " devices to the list of active hosts")
    input("Press enter to return to NMAP menu")
    main_menu.nmap_menu()


def listactivehosts():
    import config
    import main_menu
    os.system("clear")
    print("*************************************************")
    print("*             Current Active Hosts:             *")
    print("*************************************************")
    for device in config.listofhosts:
        print("*** - " + device + " - ***")
    print("")
    input("Press enter to return to NMAP Menu")
    main_menu.nmap_menu()


def scansingleip(ip):
    import main_menu
    from nmap_device import NMAPDevice
    import config
    os.system("clear")
    nm = nmap.PortScanner()
    print("Current IP being scanned:- " + ip)
    nm.scan(ip, '1-1000', '-sV')
    #  mac = nm[ip]['addresses']['mac']
    hostname = nm[ip].hostname()
    print("*************************************************")
    print("         Host Scanned: - " + ip)
    print("         MAC Address: - " + 'mac')
    print("         Hostname: - " + hostname)
    print("*************************************************")
    #  print(mac)
    for x in nm[ip].keys():
        print(nm[ip][x])
    print(nm[ip].get('osclass', 'unknown'))
    for protocol in nm[ip].all_protocols():
        print("Protocol:- %s" % protocol)
        lport = nm[ip][protocol].keys()
        print(lport)
        sorted(lport)
        for port in lport:

            print("Port : %s \tname : %s \tproduct | %s \tstate : %s" %
                  (port, nm[ip][protocol][port]['name'], nm[ip][protocol][port]['product'], nm[ip][protocol][port]['state']))
    host = NMAPDevice(hostname, nm[ip].state(), ip, 'mac')
    config.singlescannedhosts.append(host)
    config.singlehostcount = len(config.singlescannedhosts)
    print("*************************************************")
    print("")
    print("")
    input("Press enter to return to the NMAP Menu")
    main_menu.nmap_menu()
