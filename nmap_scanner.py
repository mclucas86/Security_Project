#  Module for NMAP Scanning, includes menu
import nmap
import os
import ip_address
import time


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


def scan_network(ip):
    import main_menu
    os.system("clear")
    nm = nmap.PortScanner()
    print("Currently scanning the network range: " + ip)
    print("")
    print(nm.scan(ip, '22-443', '-v'))

    for host in nm.all_hosts():
        if nm[host].state() == "up":
            print("Host: '{0}' state is '{1}'".format(host, nm[host].state()))

    input("Press enter to return to NMAP menu")
    main_menu.nmap_menu()
