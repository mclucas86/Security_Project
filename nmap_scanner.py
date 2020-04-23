#  Module for NMAP Scanning, includes menu
import nmap
import os
import ip_address
import time
#  import nmap_device


#  Method will scan the network looking for active hosts. Any hosts which are returned will
#  be added to a list which is contained within the config.py file
def populatehosts(ip):
    import main_menu
    import config
    os.system("clear")
    nm = nmap.PortScanner()
    print("Currently scanning for active hosts on: " + ip)
    nm.scan(ip, '22-443', '-v')

    for hosts in nm.all_hosts():
        if nm[hosts].state() == "up":
            config.listofhosts.append(hosts)
            print("Adding " + hosts + " to the list of hosts")

    if len(config.listofhosts) != 0:
        print("Added " + str(len(config.listofhosts)) + " devices to the list of active hosts")
    input("Press enter to return to NMAP menu")
    main_menu.menu()


def listactivehosts():
    print("              Current Active Hosts:              ")
    print("*************************************************")
    for 


