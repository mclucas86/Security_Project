import socket
import os
import re
import subprocess
import time

#  ip_check is a regular expression for validating an IP address is of the correct format.
ip_check = re.compile(r'(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.('
                      r'25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.('
                      r'25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.('
                      r'25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)')


def checkip(ip):
    #  Uses the regular expression above, ensures the IP address entered meets the criteria for formatting.
    if re.search(ip_check, ip):
        return True
    else:
        return False


def getcidrprefix(ip):
    #  Reads the IP address via a parameter, and strips out the CIDR prefix (i.e. /24, or /32 etc.)
    cidr = subprocess.check_output(["ip", "-o", "addr", "show"], stderr=subprocess.STDOUT).decode()
    cidrprefix_output = re.findall(str(ip) + r"/[0-9][0-9]", cidr)
    temp_ip = "".join(cidrprefix_output)
    cidrprefix = re.sub(ip_check, "", temp_ip)
    cidrprefix = cidrprefix.replace("/", "")
    return cidrprefix


def get_default_gateway():
    gw_output = ""
    ps = subprocess.Popen(("ip", "r"), stdout=subprocess.PIPE)
    gw = subprocess.check_output(["grep", "default"], stdin=ps.stdout).decode()
    temp_output = re.findall(ip_check, gw)
    for x in temp_output:
        gw_output = ".".join(x)
    return gw_output


#  Method to organise a list of IP address in numerical order
def ip_to_tuple(ip_str):
    ip = ip_str.split(':')[0]
    ip = ip.split('.')
    return tuple(map(int, ip))


def getnetmask(cidr):
    cidr = int(cidr)
    mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
    return (str( (0xff000000 & mask) >> 24) + '.' +
            str( (0x00ff0000 & mask) >> 16) + '.' +
            str( (0x0000ff00 & mask) >> 8) + '.' +
            str( (0x000000ff & mask)))


def get_ip():
    # get_IP uses the socket import and connects to the IP 10.255.255.255. The IP which is used to connect
    # to this socket is the IP address of the local machine. This is then returned to the user for further
    # use in the application.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.connect(('10.255.255.255', 1))
        ip = sock.getsockname()[0]
        return ip
    except:
        print("Sorry, unable to detect the IP address from the host")
        return '127.0.0.1'
    finally:
        sock.close()


def get_hostname():
    # get_Hostname acquires the hostname of the computer running the application. This is used in the final
    # report of the results.
    try:
        hostname = socket.gethostname()
        return hostname
    except:
        print("Unable to retrieve hostname")


def getos(option):
    # Using the module OS, the name of the operating system is devised as either: nt (Windows), posix (Linux) or other.
    # This method discovers this and returns it to the user.
    switcher = {
        "win32": "Windows",
        "linux": "Linux",
        "darwin": "Mac OS",
        "aix": "AIX",
        "cygwin": "Windows / Cygiwin"
    }
    return switcher.get(option, "Unknown OS")


def ping():
    # Pings an IP which is presented by the user. Calls the OS.System, and uses the command line utility ping
    import main_menu
    os.system("clear")
    print("Please enter an IP address to ping (In the format of aaa.bbb.ccc.ddd)")
    ip = input("IP:- ")

    if checkip(ip):
        iterations = input("How many ping iterations to carry out (Default: [4]):- ")
        try:
            if iterations == "":
                iterations = 4
            else:
                iterations = int(iterations)
            os.system(f'ping -c {iterations} {ip}')
            print("")
            input("Please press enter to return to the main menu")
            main_menu.main_menu()
        except ValueError:
            print("Sorry, an integer hasn't been entered. Please try again.")
            time.sleep(1)
            ping()
    else:
        print("Sorry, IP address entered is incorrect. Please try again.")
        time.sleep(1)
        ping()
