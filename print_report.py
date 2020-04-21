import config


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