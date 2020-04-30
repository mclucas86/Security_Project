# Import statements for the Security Project
import os
import time
import config
import ip_address


def onload():
    import subprocess

    os.system("clear")
    result = subprocess.call(['which', 'nmap'])
    if result == 0:
        if not os.getuid() == 0:
            print("Sorry, only can be run as root")
            time.sleep(2)
            exit()
        else:
            config.getsysinfo()
            menu()
    else:
        print("NMAP is NOT installed. This needs to be installed to continue. Do you wish to install?")
        print("Note: This will be run as a SUDO user. Please ensure you are sudo to continue.")
        answer = input("Install NMAP [Y/n]")

        if answer.lower() == "y":
            os.system("sudo apt-get install nmap -y")
            time.sleep(1)
            onload()
        else:
            print("Sorry, without NMAP this program cannot run. Goodbye")
            exit()


def menu():
    os.system('clear')
    print("****************************************************************")
    print("****************************************************************")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***             NETWORK MAPPER AND REPORTING TOOL            ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***             A: System Information                        ***")
    print("***             B: Ping IP                                   ***")
    print("***             C: NMAP Scan                                 ***")
    print("***             D: Print Results                             ***")
    print("***             Q: Quit                                      ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("****************************************************************")
    print("****************************************************************")
    print(" + No. of Single Scan Hosts stored:- " + str(config.singlehostcount))
    print(" + No. of Multi Scan Hosts stored:- " + str(config.networkhostcount))
    print("")
    option = input("Please enter a choice:  ")
    option = option.lower()

    if option == "a":
        import print_report
        print_report.print_system_info()
    elif option == "b":
        ip_address.ping_ip()
        time.sleep(2)
        os.system('clear')
        menu()
    elif option == "c":
        nmap_menu()
    elif option == "d":
        import print_report
        print("View Reports Here")
        input("Press Enter to continue...")
        menu()
    elif option == "q":
        os.system('clear')
        exit()
    else:
        print("Please select an option from the list.")
        print("Please try again.")
        time.sleep(1)
        menu()


def nmap_menu():
    import nmap_scanner
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
    print("***             (1) - Scan For Active Hosts                  ***")
    print("***             (2) - List Active Host IP's                  ***")
    print("***             (3) - Scan a SINGLE IP                       ***")
    print("***             (4) - Scan Network                           ***")
    print("***             (H) - Help                                   ***")
    print("***             (Q) - Quit NMAP                              ***")
    print("***                                                          ***")
    print("****************************************************************")
    print("****************************************************************")
    print("")
    nmap_option = input("Please select an option: ")

    if nmap_option == "1":
        ip = config.def_gateway + config.netmask
        nmap_scanner.populatehosts(ip)
    elif nmap_option == "2":
        nmap_scanner.listactivehosts()
    elif nmap_option == "3":
        ip = input("Please enter an IP address to scan: ")
        nmap_scanner.scansingleip(ip)
        time.sleep(1)
        nmap_menu()
    elif nmap_option == "4":
        print("NMAP Scan Entire Network")
        time.sleep(1)
        nmap_menu()
    elif nmap_option.lower() == "h":
        import help
        os.system("clear")
        help.nmaphelp()
    elif nmap_option.lower() == "q":
        menu()
    else:
        os.system("clear")
        nmap_menu()


onload()
