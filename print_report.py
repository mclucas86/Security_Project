import config


def print_host_info():
    hostname = config.hostname
    host_os = config.host_os
    ip_addr = config.ip_addr
    default_gateway = config.def_gateway
    netmask = config.netmask

    print("The hostname of the system is: " + hostname)
    print("The Operating System in use is: " + host_os)
    print(hostname + " is communicating with an IP address of :" + ip_addr + " and CIDR bits of " + netmask)
    print("The Default Gateway(Router) is on IP: " + default_gateway)


def print_system_info():
    import main_menu
    import os

    os.system("clear")
    print("****************************************************************")
    print("****************************************************************")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                                                          ***")
    print("***                     SYSTEM INFORMATION                   ***")
    print("***                                                          ***")
    print("")
    print(" + Operating System: " + config.host_os + " + ")
    print(" + Hostname: " + config.hostname + " + ")
    print(" + IP Address (w/ CIDR): " + config.ip_addr + config.netmask + " + ")
    print(" + Default Gateway: " + config.def_gateway + " + ")
    print("")
    print("***                                                          ***")
    print("***                                                          ***")
    print("****************************************************************")
    print("****************************************************************")

    input("Press enter to continue.")
    main_menu.menu()