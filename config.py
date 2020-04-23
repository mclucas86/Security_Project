#  This module holds the global variables, as well as any data discovered by the application

#  Global Variables for main_menu
hostname = ""
ip_addr = ""
host_os = ""
netmask = ""
def_gateway = ""
listofhosts = []

#  Populates System Info on the Main Menu
def getsysinfo():
    import ip_address
    import sys

    global ip_addr
    global hostname
    global host_os
    global netmask
    global def_gateway

    ip_addr = ip_address.get_ip()
    hostname = ip_address.get_hostname()
    host_os = ip_address.get_os(sys.platform)
    netmask = ip_address.get_netmask(ip_addr)
    def_gateway = ip_address.get_default_gateway()
