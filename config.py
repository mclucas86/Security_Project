#  This module holds the global variables, as well as any data discovered by the application

#  Global Variables for main_menu
hostname = ""
ip_addr = ""
host_os = ""
cidr_prefix = ""
netmask = ""
def_gateway = ""
activehosts = []
listofhosts = []
#  Populates System Info on the Main Menu
def getsysinfo():
    import ip_address
    import sys

    global ip_addr
    global hostname
    global host_os
    global cidr_prefix
    global def_gateway
    global netmask

    ip_addr = ip_address.get_ip()
    hostname = ip_address.get_hostname()
    host_os = ip_address.getos(sys.platform)
    cidr_prefix = ip_address.getcidrprefix(ip_addr)
    netmask = ip_address.getnetmask(cidr_prefix)
    def_gateway = ip_address.get_default_gateway()
