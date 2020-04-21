#  Module for NMAP Scanning, includes menu
import nmap
import os
import ip_address
import time
#  import nmap_device


def scan_ip():
    import main_menu
    os.system("clear")
    nm = nmap.PortScanner()
    ip = input("Please enter an IP address to scan: ")
    print("")

    if ip_address.check_ip(ip):
        print(nm.scan(ip, '22-443', '-v'))

        for host in nm.all_hosts():
            print('Host: %s is up' % host)
            print('State: %s' % nm[host].state())

        input("Please press enter to return to previous menu")
        main_menu.nmap_menu()
    else:
        print("Sorry, IP address is incorrect")
        time.sleep(1)
        scan_ip()


def scanactivehosts(ip):
    import main_menu
    os.system("clear")
    nm = nmap.PortScanner
    print("Scanning for active hosts")
    sca


def scan_network(ip):
    import main_menu
    os.system("clear")
    nm = nmap.PortScanner()
    print("Currently scanning the network range: " + ip)
    print("")
    time.sleep(1)
    nm.scan(ip, '22-443', '-v')
    hostlist = []
    host123 = []

    for host in nm.all_hosts():
        from nmap_device import NMAPDevice
        if nm[host].state() == "up":
            #  print("Host: '{0}' state is '{1}'".format(host, nm[host].state()))
            device = NMAPDevice(nm[host].hostname(), nm[host].state())
            host123.append(nm)
            hostlist.append(device)
    for x in hostlist:
        x.printhostname()
    input("Press enter to return to NMAP menu")
    main_menu.nmap_menu()
