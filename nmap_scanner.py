#  Modules for NMAP Scanning utilities
import nmap
import os
import config
import ip_address
import time


def populatehosts(ip, cidr):
    #  Method will scan the network looking for active hosts. Any hosts which are returned will
    #  be added to a list which is contained within the config.py file
    import main_menu
    target = ip + "/" + cidr
    print("Currently scanning for active hosts on:- " + target)
    print("Depending on the size of the network, this may take a few minutes")
    nm = nmap.PortScanner()
    nm.scan(hosts=target, ports='22-443', arguments='-sV')
    print("*************************************************")
    print("*            Active Hosts Detected:             *")
    print("*************************************************")
    for host in nm.all_hosts():
        if nm[host].state() == "up":
            config.activehosts.append(host)
    config.activehosts = sorted(config.activehosts, key=ip_address.ip_to_tuple)
    for i in config.activehosts:
        print(i)
    print("")
    input("Press Enter to continue")
    main_menu.nmap_menu()


def listactivehosts():
    #  Method which lists the active hosts discovered on the network
    import main_menu
    os.system("clear")
    if len(config.activehosts) != 0:
        print("*************************************************")
        print("*             Current Active Hosts:             *")
        print("*************************************************")
        for host in config.activehosts:
            print(" + " + host)
        print("")
        input("Press enter to return to menu")
        main_menu.nmap_menu()
    else:
        print("Sorry. No hosts have been scanned into the system. Please check the network, and try again")
        time.sleep(0.5)
        main_menu.nmap_menu()


def singlescanoption():
    import main_menu
    activehosts = len(config.activehosts)

    if activehosts == 0:
        answer = input("There are no hosts loaded. Do you wish to scan a specific IP? [Y/n]: ")
        if answer.lower() == "n":
            main_menu.nmap_menu()
        elif answer.lower() == "y":
            correct = False
            while not correct:
                ip = input("Please enter the IP you wish to scan: ")
                if ip_address.checkip(ip):
                    scansingleip(ip)
                    correct = True
                    input("Scan Complete - Press enter to continue")
                    main_menu.nmap_menu()
                else:
                    print("Incorrect IP Address - Try again.")
                    time.sleep(0.5)
        else:
            print("Sorry, incorrect option. Please try again")
            time.sleep(0.5)
            singlescanoption()
    else:
        answer = input("Do you wish to scan a specific host [1], select from the list of hosts [2],"
                       " or cancel [any key]? ")
        if answer == "1":
            correct = False
            while not correct:
                ip = input("Please enter the IP address you wish to scan: ")
                if ip_address.checkip(ip):
                    scansingleip(ip)
                    correct = True
            input("Press enter to return to NMAP Menu")
            main_menu.nmap_menu()
        elif answer == "2":
            os.system("clear")
            for host in config.activehosts:
                print("(" + str(config.activehosts.index(host) + 1) + ") - " + str(host))
            correct = False
            while not correct:
                ip_input = input("Please enter option to scan:- ")
                ip_input = int(ip_input)
                if ip_input <= activehosts:
                    scansingleip(config.activehosts[ip_input-1])
                    correct = True
                input("Press enter to return to NMAP Menu")
                main_menu.nmap_menu()
        else:
            main_menu.nmap_menu()


def scansingleip(ip):
    import main_menu
    os.system("clear")
    nm = nmap.PortScanner()
    hostname = ""
    print("Currently scanning IP:- " + ip)
    try:
        print(nm.scan(hosts=ip, ports='1-65535', arguments='-sV -O -T3 -sC'))
    except KeyError:
        print("Host offline......")
        pass
    try:
        hostname = nm[ip].hostname()
    except IndexError:
        hostname = "*** UNKNOWN ***"
    except KeyError:
        print("Host offline.......")
    try:
        mac = nm[ip]['addresses']['mac']
    except KeyError:
        mac = "*** UNKNOWN ***"
    try:
        opsys = nm[ip]['osclass']['osfamily']
    except KeyError:
        opsys = "*** UNKNOWN ***"
    try:
        import datetime
        uptime = nm[ip]['uptime']['seconds']
        uptime = int(uptime)
        uptime = str(datetime.timedelta(seconds=uptime))
    except KeyError:
        uptime = "*** UNKNOWN ***"
    try:
        lastboot = nm[ip]['uptime']['lastboot']
    except KeyError:
        lastboot = "*** UNKNOWN ***"
    print("*************************************************")
    print("         Host Scanned: - " + ip)
    print("         MAC Address: - " + mac)
    print("         Hostname: - " + hostname)
    print("         OS: - " + opsys)
    print("         Last Boot Up: - " + lastboot)
    print("         Uptime (HH:MM:SS): - " + uptime)
    print("*************************************************")
    cpe = ""
    for protocol in nm[ip].all_protocols():
        if protocol == "tcp":
            lport = nm[ip][protocol].keys()
            sorted(lport)
            if len(lport) != 0:
                for port in lport:
                    print("Port:- " + str(port))
                    print("Name:- " + nm[ip][protocol][port]['name'])
                    print("Product:- " + nm[ip][protocol][port]['product'])
                    print("Version:- " + nm[ip][protocol][port]['version'])
                    print("State:- " + nm[ip][protocol][port]['state'])
                    print("Extra Info:- " + nm[ip][protocol][port]['extrainfo'])
                    print("------------------------------------------------------")
                    if nm[ip][protocol][port]['cpe'] != "":
                        if cpe == "":
                            if nm[ip][protocol][port]['cpe'] != "":
                                cpe = nm[ip][protocol][port]['cpe']
                getcpe(cpe)
            else:
                print("No open ports detected.")


def scannetwork():
    import main_menu
    os.system("clear")
    print("Currently scanning the network. Hosts to scan:- " + str(len(config.activehosts)))
    print("")
    for host in config.activehosts:
        print("")
        scansingleip(host)
        print("")
        print("")
        input("Press enter to return to NMAP menu")
    main_menu.nmap_menu()


def getcpe(cpe):
    temp_cpe = cpe.split(":/")
    temp_cpe = temp_cpe[1]
    cpe_final = temp_cpe.split(":")
    print("               CPE (Common Platform Enumeration)")
    x = 0
    while x < len(cpe_final):
        if x == 0:
            part = cpe_final[0]
            switcher = {
                "a": "Application",
                "h": "Hardware",
                "o": "Operating System"
            }
            part = switcher.get(part, "UNKNOWN")
            print("Device Type:- " + part)
        if x == 1:
            vendor = cpe_final[1]
            print("Vendor:- " + vendor)
        if x == 2:
            product = cpe_final[2]
            print("Product:- " + product)
        if x == 3:
            version = cpe_final[3]
            print("Version:- " + version)

        x += 1
