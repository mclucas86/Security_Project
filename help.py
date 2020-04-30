#


def nmaphelp():
    import main_menu
    print("****************************************************************")
    print("****************************************************************")
    print("***                                                          ***")
    print("*** + (1) scans the entire network, and will return a list   ***")
    print("***   of IP addresses which are active.                      ***")
    print("***                                                          ***")
    print("*** + (2) lists the IP Addresses which were discovered by    ***")
    print("***   option 1                                               ***")
    print("***                                                          ***")
    print("*** + (3) scans an individual IP address, and returns any    ***")
    print("***   ports which are open.                                  ***")
    print("***                                                          ***")
    print("*** + (4) scans the entire network, and will return a        ***")
    print("***   list of any open ports, with information, for each     ***")
    print("***   host. This is then stored in a list.                   ***")
    print("***                                                          ***")
    print("****************************************************************")
    print("****************************************************************")
    print("")
    input("Press enter to return to NMAP Menu")
    main_menu.nmap_menu()
