#  Import Statements for project modules
import os
import time
import config
import ip_address


def startup():
    #  This application uses Python NMAP, which requires NMAP to be installed on the OS. Currently this runs on Linux,
    #  so any command here is designed for the Linux OS. The first check is if NMAP is already installed.
    import subprocess

    os.system("clear")
    if not os.getuid() == 0:
        print("Sorry, this software can only be run as root. Please run again using SUDO")
        time.sleep(1)
        exit()
    else:
        nmap_install = subprocess.call(['which', 'nmap'])
        if nmap_install == 0:
            config.getsysinfo()
            main_menu()
        else:
            print("NMAP is NOT installed. This needs to be installed to continue. Do you wish to install?")
            answer = input("Install NMAP? [Y/n")
            if answer.lower() == "y":
                os.system("sudo apt-get install nmap -y")
                time.sleep(1)
                startup()
            else:
                print("Sorry, NMAP is required to run this application. Please install NMAP to continue")
                time.sleep(1)
                exit()


def main_menu():
    local_ip = config.ip_addr
    local_netmask = config.netmask
    local_cidr = config.cidr_prefix
    local_gw = config.def_gateway
    os.system("clear")
    print("****************************************************************")
    print("****************************************************************")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***             NETWORK MAPPER AND REPORTING TOOL            ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***             A: Ping IP                                   ***")
    print("***             B: NMAP Menu                                 ***")
    print("***             C: Print Report                              ***")
    print("***             Q: Quit                                      ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("****************************************************************")
    print("****************************************************************")
    print("")
    print(" + IP Address:- " + local_ip)
    print(" + Netmask:- " + local_netmask)
    print(" + CIDR Prefix:- " + local_cidr)
    print(" + Default Gateway:- " + local_gw)
    print("")
    menu_option = input("Please enter an option: ")
    menu_option = menu_option.lower()
    if menu_option == "a":
        ip_address.ping()
    elif menu_option == "b":
        os.system("clear")
        nmap_menu()
    elif menu_option == "c":
        print("Print Report")
        time.sleep(1)
        main_menu()
    elif menu_option == "q":
        os.system("clear")
        exit()
    else:
        print("Incorrect option selected. Please select an option from the menu")
        time.sleep(1)
        main_menu()


def nmap_menu():
    import nmap_scanner

    ip = config.def_gateway
    cidr = config.cidr_prefix
    activehosts = len(config.activehosts)
    if activehosts == 0:
        os.system("clear")
        answer = input("There are no hosts scanned into the system. Would you like to run an initial scan? [Y/n]:- ")
        if answer.lower() == "y":
            nmap_scanner.populatehosts(ip, cidr)
    os.system("clear")
    print("****************************************************************")
    print("****************************************************************")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***             NMAP Scanner Main Menu                       ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***             (1) - List Active Host IP's                  ***")
    print("***             (2) - Scan a SINGLE IP                       ***")
    print("***             (3) - Scan Network                           ***")
    if activehosts == 0:
        print("***             (S) - Scan For Active Hosts                  ***")
    print("***             (H) - Help                                   ***")
    print("***             (Q) - Quit NMAP                              ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("****************************************************************")
    print("****************************************************************")
    print("")
    print(" + Current Active Hosts:- " + str(activehosts))
    print("")
    nmap_answer = input("Choose an option from the above menu:- ")
    if nmap_answer == "1":
        nmap_scanner.listactivehosts()
    elif nmap_answer == "2":
        nmap_scanner.singlescanoption()
    elif nmap_answer == "3":
        if len(config.activehosts) != 0:
            nmap_scanner.scannetwork()
        else:
            print("Sorry, no active hosts detected. Please scan the network")
            time.sleep(1)
            nmap_menu()
    elif nmap_answer.lower() == "h":
        print("HELP")
        time.sleep(1)
        nmap_menu()
    elif nmap_answer.lower() == "s":
        nmap_scanner.populatehosts(config.def_gateway, config.cidr_prefix)
    elif nmap_answer.lower() == "q":
        main_menu()
    else:
        print("Incorrect option. Please try again.")
        time.sleep(1)
        nmap_menu()
    main_menu()


startup()

